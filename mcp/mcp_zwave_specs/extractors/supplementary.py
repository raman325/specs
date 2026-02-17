"""Extract supplementary (non-CC/application layer) spec PDFs by chapter headings."""

from __future__ import annotations

import logging
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

from mcp_zwave_specs.config import Config
from mcp_zwave_specs.extractors.pdf import PageChunk, extract_pages
from mcp_zwave_specs.models import SpecSection

logger = logging.getLogger(__name__)


def _split_by_toc(
    pages: list[PageChunk],
    pdf_name: str,
    min_level: int = 1,
    max_level: int = 2,
) -> list[SpecSection]:
    """Split pages into sections using TOC entries at the specified levels."""
    # Collect TOC entries at the desired levels
    toc_entries: list[tuple[str, int]] = []  # (title, page_number)
    for page in pages:
        for level, title, page_num in page.toc_items:
            if min_level <= level <= max_level:
                toc_entries.append((title, page_num))

    if not toc_entries:
        # No TOC — return as a single section
        content = "\n".join(p.text for p in pages)
        return [SpecSection(title=pdf_name, content=content, pdf_name=pdf_name)]

    sections: list[SpecSection] = []
    for i, (title, start_page) in enumerate(toc_entries):
        end_page = toc_entries[i + 1][1] if i + 1 < len(toc_entries) else pages[-1].page_number + 1

        parts: list[str] = []
        for page in pages:
            if page.page_number < start_page:
                continue
            if page.page_number >= end_page:
                break
            parts.append(f"\n<!-- PAGE {page.page_number + 1} -->\n")
            parts.append(page.text)

        content = "\n".join(parts).strip()
        if not content:
            continue

        sections.append(
            SpecSection(
                title=title,
                content=content,
                pdf_name=pdf_name,
                section_number=str(i + 1),
                page_start=start_page + 1,
                page_end=end_page,
            )
        )

    return sections


def _extract_pdf_safe(pdf_path: Path, key: str) -> tuple[str, list[SpecSection] | None]:
    """Extract and split a single PDF, returning (key, sections) or (key, None) on failure."""
    try:
        pages = extract_pages(pdf_path)
    except Exception:
        logger.exception("Failed to extract PDF: %s", pdf_path)
        return key, None
    sections = _split_by_toc(pages, key)
    logger.info("Split %s into %d sections (%d pages)", key, len(sections), len(pages))
    return key, sections


def _collect_pdf_paths(config: Config) -> list[tuple[str, Path]]:
    """Collect all (key, pdf_path) pairs for supplementary PDFs."""
    pairs: list[tuple[str, Path]] = []
    stack_dir = config.specs_dir / "Z-Wave Stack Specifications"

    # Stack specification PDFs
    for key, filename in config.supplementary_pdfs.items():
        pdf_path = stack_dir / filename
        if pdf_path.exists():
            pairs.append((key, pdf_path))
        else:
            logger.warning("PDF not found: %s", pdf_path)

    # Test specification PDFs (in Stack Specs dir)
    for key, filename in config.test_pdfs.items():
        pdf_path = stack_dir / filename
        if pdf_path.exists():
            pairs.append((key, pdf_path))
        else:
            logger.warning("PDF not found: %s", pdf_path)

    # CC Control Test Spec (different directory)
    cc_test_path = (
        config.specs_dir
        / "Z-Wave Command Classes Specifications"
        / "Z-Wave Command Class Control Test Specification.pdf"
    )
    if cc_test_path.exists():
        pairs.append(("test_cc_control", cc_test_path))

    # Z-Wave Plus v2 Device Type Test Spec
    zwp_test = config.specs_dir / "Z-Wave Plus v2 Specifications"
    if zwp_test.is_dir():
        pdf_path = zwp_test / "Z-Wave Plus v2 Device Type Test Specification.pdf"
        if pdf_path.exists():
            pairs.append(("test_device_type", pdf_path))

    # Standalone PDFs (top-level)
    for key, filename in config.standalone_pdfs.items():
        pdf_path = config.specs_dir / filename
        if pdf_path.exists():
            pairs.append((key, pdf_path))
        else:
            logger.warning("PDF not found: %s", pdf_path)

    # Legacy specification PDFs
    legacy_dir = config.specs_dir / "Legacy Specifications"
    if legacy_dir.is_dir():
        for key, filename in config.legacy_pdfs.items():
            pdf_path = legacy_dir / filename
            if pdf_path.exists():
                pairs.append((key, pdf_path))
            else:
                logger.warning("PDF not found: %s", pdf_path)

    # SmartStart PDFs
    smartstart_dir = config.smartstart_dir
    if smartstart_dir.is_dir():
        for pdf_path in sorted(smartstart_dir.glob("*.pdf")):
            key = "smartstart_" + pdf_path.stem.lower().replace(" ", "_").replace("-", "_")
            pairs.append((key, pdf_path))

    # Application Notes (Z-Wave specific only)
    app_notes_dir = config.app_notes_dir
    if app_notes_dir.is_dir():
        for pdf_path in sorted(app_notes_dir.glob("*.pdf")):
            if not pdf_path.stem.startswith(("APL", "INS")):
                continue
            key = "appnote_" + pdf_path.stem.lower().replace(" ", "_").replace("-", "_")
            pairs.append((key, pdf_path))

    return pairs


def extract_supplementary(
    config: Config,
) -> tuple[dict[str, list[SpecSection]], dict[str, Path]]:
    """Extract and split all supplementary PDFs in parallel.

    Returns (sections_by_key, paths_by_key) where:
      - sections_by_key: pdf_key → list of SpecSection
      - paths_by_key: pdf_key → resolved filesystem Path
    """
    pairs = _collect_pdf_paths(config)
    if not pairs:
        return {}, {}

    # Build path lookup from all collected pairs
    paths: dict[str, Path] = {key: pdf_path for key, pdf_path in pairs}

    logger.info("Extracting %d supplementary PDFs in parallel...", len(pairs))
    start = time.monotonic()
    result: dict[str, list[SpecSection]] = {}

    with ProcessPoolExecutor() as executor:
        futures = {
            executor.submit(_extract_pdf_safe, pdf_path, key): key for key, pdf_path in pairs
        }
        for future in as_completed(futures):
            key, sections = future.result()
            if sections is not None:
                result[key] = sections

    elapsed = time.monotonic() - start
    logger.info(
        "Extracted %d supplementary PDFs (%d total sections) in %.1fs",
        len(result),
        sum(len(s) for s in result.values()),
        elapsed,
    )
    return result, paths
