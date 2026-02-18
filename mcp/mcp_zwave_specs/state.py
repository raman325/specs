"""Application state with lazy-loaded Z-Wave spec data."""

from __future__ import annotations

import logging
import threading
import time
from collections import defaultdict
from collections.abc import Callable
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import asdict, dataclass, field
from difflib import get_close_matches
from pathlib import Path

from mcp_zwave_specs.cache import CacheManager, dir_hash, file_hash
from mcp_zwave_specs.config import Config
from mcp_zwave_specs.extractors.app_layer import (
    APP_LAYER_CHAPTERS,
    extract_app_layer_chapter_sections,
    group_cc_versions,
    split_app_layer_sections,
)
from mcp_zwave_specs.extractors.app_layer_rst import (
    extract_app_layer_chapter_sections_rst,
    split_app_layer_sections_rst,
)
from mcp_zwave_specs.extractors.header import (
    DeviceClass,
    HeaderConstant,
    parse_device_classes,
    parse_header,
    parse_header_constants,
)
from mcp_zwave_specs.extractors.pdf import extract_pages
from mcp_zwave_specs.extractors.registry import parse_cc_list, parse_registries
from mcp_zwave_specs.extractors.supplementary import collect_pdf_paths, extract_pdf_safe
from mcp_zwave_specs.models import (
    CCHeaderData,
    CommandClassInfo,
    RegistryData,
    SpecSection,
)
from mcp_zwave_specs.search import SearchIndex
from mcp_zwave_specs.serialization import (
    deserialize_cc,
    deserialize_header_data,
    serialize_cc,
)

logger = logging.getLogger(__name__)


@dataclass
class AppState:
    """Lazily-loaded application state."""

    config: Config
    cache: CacheManager

    # Loaded on demand
    cc_sections: dict[str, CommandClassInfo] = field(default_factory=dict)
    header_data: dict[str, CCHeaderData] = field(default_factory=dict)
    registries: dict[str, RegistryData] = field(default_factory=dict)
    supplementary: dict[str, list[SpecSection]] = field(default_factory=dict)
    search_index: SearchIndex = field(default_factory=SearchIndex)

    # CC spec chapter sections (device types, role types, cc control)
    app_layer_chapters: dict[str, list[SpecSection]] = field(default_factory=dict)
    # Device classes from ZW_classcmd.h
    device_classes: list[DeviceClass] = field(default_factory=list)
    # Constants from all header files (keyed by header filename)
    header_constants: dict[str, list[HeaderConstant]] = field(default_factory=dict)
    # Map pdf_key → resolved filesystem Path (for supplementary PDFs)
    supplementary_paths: dict[str, Path] = field(default_factory=dict)

    _loaded: set[str] = field(default_factory=set)
    _locks: dict[str, threading.Lock] = field(default_factory=lambda: defaultdict(threading.Lock))

    # -- generic ensure helper ------------------------------------------------

    def _ensure(self, category: str, loader: Callable[[], None]) -> None:
        """Acquire the per-category lock, skip if already loaded, else run *loader*."""
        with self._locks[category]:
            if category in self._loaded:
                return
            loader()
            self._loaded.add(category)

    # -- ensure_app_layer_blob (shared extraction for PDF path) ----------------

    def ensure_app_layer_blob(self) -> str | None:
        """Extract app-layer PDF into a blob (CC sections + chapter sections).

        Returns the blob's file_hash, or None if RST source is being used.
        """
        with self._locks["app_layer_blob"]:
            if self.config.app_layer_rst_available:
                return None

            fh = file_hash(self.config.app_layer_pdf)
            if self.cache.has_blob(fh):
                return fh

            logger.info("Extracting application layer PDF (this may take a moment)...")
            pages = extract_pages(self.config.app_layer_pdf)

            # CC sections
            raw_sections = split_app_layer_sections(pages)
            cc_sections = group_cc_versions(raw_sections)

            cc_data: dict[str, dict] = {}
            for name, cc in cc_sections.items():
                cc_data[name] = serialize_cc(cc)
                safe_name = name.replace("/", "_")
                self.cache.write_blob_text(fh, f"cc/{safe_name}.md", cc.content)

            # Chapter sections
            chapter_data: dict[str, list[dict]] = {}
            for chapter_title, key in APP_LAYER_CHAPTERS.items():
                sections = extract_app_layer_chapter_sections(pages, chapter_title)
                if sections:
                    chapter_data[key] = [asdict(s) for s in sections]

            blob_data = {
                "cc_sections": cc_data,
                "chapter_sections": chapter_data,
            }
            self.cache.write_blob(fh, blob_data, meta={"source": str(self.config.app_layer_pdf)})
            logger.info(
                "Cached app-layer blob: %d CC sections, %d chapter groups",
                len(cc_data),
                len(chapter_data),
            )
            return fh

    # -- ensure_app_layer ------------------------------------------------------

    def ensure_app_layer(self) -> None:
        """Load CC sections from cache or extract from RST source / PDF."""
        self._ensure("app_layer", self._load_app_layer)

    def _load_app_layer(self) -> None:
        if not self.config.specs_available and not self.config.app_layer_rst_available:
            return

        if self.config.app_layer_rst_available:
            logger.info("Extracting CC sections from RST source...")
            sections = split_app_layer_sections_rst(self.config.app_layer_rst_dir)
            self.cc_sections = group_cc_versions(sections)
            self._merge_header_ids()
            self._build_search_index()
            logger.info("Extracted %d CC sections from RST", len(self.cc_sections))
            return

        # PDF path: load from blob, merge header IDs in-memory
        fh = self.ensure_app_layer_blob()
        if fh is None:
            return

        blob_data = self.cache.read_blob(fh)
        if blob_data and "cc_sections" in blob_data:
            for name, data in blob_data["cc_sections"].items():
                safe_name = name.replace("/", "_")
                content = self.cache.read_blob_text(fh, f"cc/{safe_name}.md") or ""
                self.cc_sections[name] = deserialize_cc(data, content)

        self._merge_header_ids()
        self._build_search_index()
        logger.info("Loaded %d CC sections", len(self.cc_sections))

    def _merge_header_ids(self) -> None:
        """Merge CC IDs from header data into loaded CC sections."""
        self.ensure_header()
        for name, cc in self.cc_sections.items():
            base_name = name.removesuffix(" (Control)")
            if base_name in self.header_data:
                cc.cc_id = self.header_data[base_name].cc_id

    def _build_search_index(self) -> None:
        """Rebuild the full-text search index from loaded CC sections."""
        self.search_index = SearchIndex()
        for name, cc in self.cc_sections.items():
            self.search_index.add(name, name, cc.content)

    # -- ensure_header ---------------------------------------------------------

    def ensure_header(self) -> None:
        """Load CC header data and device classes from cache or ZW_classcmd.h."""
        self._ensure("header", self._load_header)

    def _load_header(self) -> None:
        if not self.config.specs_available:
            return

        fh = file_hash(self.config.header_file)

        cached = self.cache.read_blob(fh)
        if cached:
            for name, data in cached.get("header_data", {}).items():
                self.header_data[name] = deserialize_header_data(data)
            for d in cached.get("device_classes", []):
                self.device_classes.append(
                    DeviceClass(
                        generic_name=d["generic_name"],
                        generic_id=d["generic_id"],
                        comment=d.get("comment", ""),
                        specific_types=[tuple(s) for s in d.get("specific_types", [])],
                    )
                )
            logger.info("Loaded %d CC header entries from cache", len(self.header_data))
            return

        self.header_data = parse_header(self.config.header_file)
        self.device_classes = parse_device_classes(self.config.header_file)

        blob_data = {
            "header_data": {name: asdict(hd) for name, hd in self.header_data.items()},
            "device_classes": [asdict(dc) for dc in self.device_classes],
        }
        self.cache.write_blob(fh, blob_data, meta={"source": str(self.config.header_file)})

    # -- ensure_registries -----------------------------------------------------

    def ensure_registries(self) -> None:
        """Load registry data from cache or parse Excel files."""
        self._ensure("registries", self._load_registries)

    def _cache_or_extract_registries(
        self,
        fh: str,
        extract: Callable[[], dict[str, RegistryData]],
        source: Path,
        label: str,
    ) -> None:
        """Load registries from cache or extract and cache them."""
        cached = self.cache.read_blob(fh)
        if cached:
            for key, data in cached.items():
                self.registries[key] = RegistryData(**data)
            logger.info("Loaded %d %s from cache", len(cached), label)
        else:
            extracted = extract()
            self.registries.update(extracted)
            self.cache.write_blob(
                fh,
                {k: asdict(r) for k, r in extracted.items()},
                meta={"source": str(source)},
            )
            logger.info("Extracted and cached %d %s", len(extracted), label)

    def _load_registries(self) -> None:
        if not self.config.specs_available:
            return

        reg_dir = self.config.registries_dir
        cc_xlsx = self.config.cc_list_xlsx

        if reg_dir.is_dir():
            self._cache_or_extract_registries(
                dir_hash(reg_dir, frozenset({".xlsx", ".xls"})),
                lambda: parse_registries(reg_dir),
                reg_dir,
                "registries",
            )
        if cc_xlsx.exists():
            self._cache_or_extract_registries(
                file_hash(cc_xlsx),
                lambda: parse_cc_list(cc_xlsx),
                cc_xlsx,
                "CC list registries",
            )

    # -- ensure_supplementary --------------------------------------------------

    def ensure_supplementary(self) -> None:
        """Load supplementary PDF sections from per-file blobs."""
        self._ensure("supplementary", self._load_supplementary)

    def _load_supplementary(self) -> None:
        if not self.config.specs_available:
            return

        # Collect all (key, path) pairs and populate path lookup
        pairs = collect_pdf_paths(self.config)
        for key, pdf_path in pairs:
            self.supplementary_paths[key] = pdf_path

        if not pairs:
            return

        # Compute per-file hashes
        blob_hashes: dict[str, str] = {}
        for key, pdf_path in pairs:
            blob_hashes[key] = file_hash(pdf_path)

        # Load from individual blobs or extract missing
        loaded: dict[str, list[SpecSection]] = {}
        to_extract: list[tuple[str, Path]] = []

        for key, pdf_path in pairs:
            fh = blob_hashes[key]
            blob_data = self.cache.read_blob(fh)
            if blob_data:
                loaded[key] = [SpecSection(**s) for s in blob_data]
            else:
                to_extract.append((key, pdf_path))

        # Extract missing in parallel
        if to_extract:
            logger.info("Extracting %d supplementary PDFs in parallel...", len(to_extract))
            t0 = time.monotonic()
            with ProcessPoolExecutor() as executor:
                futures = {
                    executor.submit(extract_pdf_safe, pdf_path, key): key
                    for key, pdf_path in to_extract
                }
                for future in as_completed(futures):
                    key, sections = future.result()
                    if sections is not None:
                        loaded[key] = sections
                        fh = blob_hashes[key]
                        self.cache.write_blob(
                            fh,
                            [asdict(s) for s in sections],
                            meta={
                                "key": key,
                                "source": str(self.supplementary_paths.get(key)),
                            },
                        )
            elapsed = time.monotonic() - t0
            logger.info(
                "Extracted %d supplementary PDFs in %.1fs",
                len(to_extract),
                elapsed,
            )

        self.supplementary = loaded
        logger.info("Loaded %d supplementary PDFs", len(self.supplementary))

    # -- ensure_app_layer_chapters ---------------------------------------------

    def ensure_app_layer_chapters(self) -> None:
        """Load application layer chapter sections from cache, RST source, or PDF."""
        self._ensure("app_layer_chapters", self._load_app_layer_chapters)

    def _load_app_layer_chapters(self) -> None:
        if not self.config.specs_available and not self.config.app_layer_rst_available:
            return

        if self.config.app_layer_rst_available:
            logger.info("Extracting chapter sections from RST source...")
            self.app_layer_chapters = extract_app_layer_chapter_sections_rst(
                self.config.app_layer_rst_dir
            )
            logger.info(
                "Extracted %d CC spec chapter groups from RST",
                len(self.app_layer_chapters),
            )
            return

        # PDF path: load chapter sections from shared blob
        fh = self.ensure_app_layer_blob()
        if fh is None:
            return

        blob_data = self.cache.read_blob(fh)
        if blob_data and "chapter_sections" in blob_data:
            for key, sections_data in blob_data["chapter_sections"].items():
                self.app_layer_chapters[key] = [SpecSection(**s) for s in sections_data]
            logger.info(
                "Loaded %d CC spec chapter groups from blob cache",
                len(self.app_layer_chapters),
            )

    # -- ensure_header_constants -----------------------------------------------

    def ensure_header_constants(self) -> None:
        """Load header constants from cache or parse .h files."""
        self._ensure("header_constants", self._load_header_constants)

    def _load_header_constants(self) -> None:
        if not self.config.specs_available:
            return

        api_dir = self.config.api_includes_dir
        if not api_dir.is_dir():
            return

        fh = dir_hash(api_dir, frozenset({".h"}))

        cached = self.cache.read_blob(fh)
        if cached:
            for fname, items in cached.items():
                self.header_constants[fname] = [HeaderConstant(**c) for c in items]
            logger.info(
                "Loaded constants from %d header files from cache",
                len(self.header_constants),
            )
            return

        # Parse all .h files (except ZW_classcmd.h which is handled by ensure_header)
        for h_file in sorted(api_dir.glob("*.h")):
            if h_file.name == "ZW_classcmd.h":
                continue
            constants = parse_header_constants(h_file)
            if constants:
                self.header_constants[h_file.name] = constants

        blob_data = {
            fname: [asdict(c) for c in consts] for fname, consts in self.header_constants.items()
        }
        self.cache.write_blob(fh, blob_data, meta={"source": str(api_dir)})

    # -- build_all --------------------------------------------------------------

    def build_all(self) -> None:
        """Eagerly load all data categories (for cache warming)."""
        steps = [
            ("header", self.ensure_header),
            ("app_layer", self.ensure_app_layer),
            ("app_layer_chapters", self.ensure_app_layer_chapters),
            ("registries", self.ensure_registries),
            ("supplementary", self.ensure_supplementary),
            ("header_constants", self.ensure_header_constants),
        ]
        for name, fn in steps:
            t0 = time.monotonic()
            fn()
            logger.info("build_all: %s completed in %.1fs", name, time.monotonic() - t0)

    def find_cc(self, name: str | None, cc_id: int | None) -> CommandClassInfo | None:
        """Find a CC by name or ID, with fuzzy matching."""
        self.ensure_app_layer()

        if cc_id is not None:
            for cc in self.cc_sections.values():
                if cc.cc_id == cc_id:
                    return cc
            return None

        if name is None:
            return None

        # Exact match
        if name in self.cc_sections:
            return self.cc_sections[name]

        # Case-insensitive match
        lower_map = {k.lower(): k for k in self.cc_sections}
        if name.lower() in lower_map:
            return self.cc_sections[lower_map[name.lower()]]

        # Fuzzy match
        matches = get_close_matches(name.lower(), lower_map.keys(), n=1, cutoff=0.6)
        if matches:
            return self.cc_sections[lower_map[matches[0]]]

        return None

    def suggest_cc_names(self, name: str) -> list[str]:
        """Return close CC name matches for error messages."""
        self.ensure_app_layer()
        lower_map = {k.lower(): k for k in self.cc_sections}
        matches = get_close_matches(name.lower(), lower_map.keys(), n=5, cutoff=0.4)
        return [lower_map[m] for m in matches]
