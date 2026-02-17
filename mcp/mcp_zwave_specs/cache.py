"""Disk cache for extracted Z-Wave specification data."""

from __future__ import annotations

import hashlib
import json
import logging
from pathlib import Path
from typing import Any

from mcp_zwave_specs.config import Config

logger = logging.getLogger(__name__)

CACHE_VERSION = 1


_HASH_EXTENSIONS = frozenset({".pdf", ".xlsx", ".xls", ".h", ".rst"})
_HASH_SKIP_DIRS = frozenset({".git", "__pycache__", ".venv", "node_modules"})


def _compute_specs_hash(specs_dir: Path, extra_dirs: list[Path] | None = None) -> str:
    """Hash specs directory contents by file sizes and mtimes for invalidation.

    Only hashes files with relevant extensions (.pdf, .xlsx, .h, .rst) and
    skips common non-spec directories (.git, __pycache__, etc.).

    When extra_dirs are provided (e.g. an RST source directory), their contents
    are included in the hash so cache is invalidated when they change.
    """
    h = hashlib.sha256()
    dirs_to_hash = [specs_dir] + (extra_dirs or [])
    for d in dirs_to_hash:
        if not d.is_dir():
            h.update(f"missing:{d}".encode())
            continue
        for p in sorted(d.rglob("*")):
            if any(part in _HASH_SKIP_DIRS for part in p.parts):
                continue
            if p.is_file() and p.suffix.lower() in _HASH_EXTENSIONS:
                stat = p.stat()
                h.update(f"{p.relative_to(d)}:{stat.st_size}:{stat.st_mtime_ns}".encode())
    return h.hexdigest()[:16]


class CacheManager:
    """Manages disk cache for extracted spec data.

    Cache is invalidated when specs directory contents change (based on
    file sizes and modification times).
    """

    def __init__(self, config: Config) -> None:
        """Initialize with config; no directories are created until needed."""
        self.config = config
        self.cache_dir = config.cache_dir
        self._manifest: dict[str, Any] | None = None
        self._specs_hash: str | None = None

    @property
    def manifest_path(self) -> Path:
        """Path to the cache manifest file."""
        return self.cache_dir / "manifest.json"

    def ensure_dirs(self) -> None:
        """Create the cache directory tree if it doesn't exist."""
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        for subdir in ("app_layer_sections", "supplementary", "registries"):
            (self.cache_dir / subdir).mkdir(exist_ok=True)

    def _load_manifest(self) -> dict[str, Any]:
        """Load the manifest from disk, or return an empty dict on first call."""
        if self._manifest is not None:
            return self._manifest
        if self.manifest_path.exists():
            try:
                self._manifest = json.loads(self.manifest_path.read_text())
                return self._manifest
            except (json.JSONDecodeError, KeyError):
                logger.warning("Corrupted cache manifest, rebuilding")
        self._manifest = {}
        return self._manifest

    def _save_manifest(self) -> None:
        """Flush the in-memory manifest to disk."""
        self.ensure_dirs()
        self.manifest_path.write_text(json.dumps(self._manifest or {}, indent=2))

    def _extra_dirs(self) -> list[Path] | None:
        """Return extra directories to include in hash computation."""
        if self.config.app_layer_rst_available:
            return [self.config.app_layer_rst_dir]
        return None

    def _get_specs_hash(self) -> str:
        """Return the current specs hash, computing and caching it once per process."""
        if self._specs_hash is None:
            self._specs_hash = _compute_specs_hash(self.config.specs_dir, self._extra_dirs())
        return self._specs_hash

    def is_valid(self) -> bool:
        """Check if the cache is valid against the current specs directory."""
        manifest = self._load_manifest()
        if manifest.get("version") != CACHE_VERSION:
            return False
        return manifest.get("specs_hash") == self._get_specs_hash()

    def mark_valid(self) -> None:
        """Update manifest with current specs hash."""
        self._manifest = self._load_manifest()
        self._manifest["version"] = CACHE_VERSION
        self._manifest["specs_hash"] = self._get_specs_hash()
        self._save_manifest()

    def has_category(self, category: str) -> bool:
        """Return True if the given data category has been cached."""
        manifest = self._load_manifest()
        return category in manifest.get("categories", {})

    def mark_category(self, category: str) -> None:
        """Record that a data category has been fully cached."""
        manifest = self._load_manifest()
        manifest.setdefault("categories", {})[category] = True
        self._save_manifest()

    # --- JSON read/write helpers ---

    def read_json(self, relative_path: str) -> Any | None:
        """Read and deserialize a JSON cache file, or return None on miss."""
        path = self.cache_dir / relative_path
        if not path.exists():
            return None
        try:
            return json.loads(path.read_text())
        except (json.JSONDecodeError, OSError):
            logger.warning("Failed to read cache file %s, ignoring", relative_path)
            return None

    def write_json(self, relative_path: str, data: Any) -> None:
        """Serialize data as JSON and write to a cache file."""
        self.ensure_dirs()
        path = self.cache_dir / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(data, indent=2, ensure_ascii=False))

    def read_text(self, relative_path: str) -> str | None:
        """Read a text cache file, or return None on miss."""
        path = self.cache_dir / relative_path
        if not path.exists():
            return None
        try:
            return path.read_text()
        except OSError:
            return None

    def write_text(self, relative_path: str, text: str) -> None:
        """Write a string to a text cache file."""
        self.ensure_dirs()
        path = self.cache_dir / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def clear(self) -> None:
        """Remove all cached data."""
        import shutil

        if self.cache_dir.exists():
            shutil.rmtree(self.cache_dir)
        self._manifest = None
        logger.info("Cache cleared: %s", self.cache_dir)
