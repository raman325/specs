"""Content-addressable two-layer disk cache for extracted Z-Wave specification data.

Layer 1 (blobs): keyed by a hash of a single input file or directory.
Layer 2 (composites): keyed by a hash of multiple blob hashes + optional config.
"""

from __future__ import annotations

import hashlib
import json
import logging
import shutil
from pathlib import Path
from typing import Any

from mcp_zwave_specs.config import Config

logger = logging.getLogger(__name__)

CACHE_VERSION = 2

_HASH_SKIP_DIRS = frozenset({".git", "__pycache__", ".venv", "node_modules"})


# ---------------------------------------------------------------------------
# Public hash helpers
# ---------------------------------------------------------------------------


def file_hash(path: Path) -> str:
    """16-char hex hash of a single file (name + size + mtime)."""
    stat = path.stat()
    h = hashlib.sha256(f"{path.name}:{stat.st_size}:{stat.st_mtime_ns}".encode())
    return h.hexdigest()[:16]


def dir_hash(dir_path: Path, extensions: frozenset[str] | None = None) -> str:
    """16-char hex hash of all matching files in a directory.

    Skips directories listed in ``_HASH_SKIP_DIRS``.
    """
    h = hashlib.sha256()
    for p in sorted(dir_path.rglob("*")):
        if any(part in _HASH_SKIP_DIRS for part in p.parts):
            continue
        if p.is_file() and (extensions is None or p.suffix.lower() in extensions):
            stat = p.stat()
            h.update(f"{p.relative_to(dir_path)}:{stat.st_size}:{stat.st_mtime_ns}".encode())
    return h.hexdigest()[:16]


def composite_hash(input_hashes: list[str], config_hash: str = "") -> str:
    """16-char hex hash of sorted input hashes + config hash."""
    h = hashlib.sha256()
    for ih in sorted(input_hashes):
        h.update(ih.encode())
    if config_hash:
        h.update(config_hash.encode())
    return h.hexdigest()[:16]


# ---------------------------------------------------------------------------
# CacheLayer — shared read/write logic for blob and composite slots
# ---------------------------------------------------------------------------


class _CacheLayer:
    """A single cache layer (blobs or composites) under a parent directory."""

    def __init__(self, root: Path, label: str) -> None:
        self._root = root
        self._label = label

    def _slot(self, key: str) -> Path:
        return self._root / key

    def has(self, key: str) -> bool:
        return self._slot(key).is_dir()

    def read_json(self, key: str) -> Any | None:
        path = self._slot(key) / "data.json"
        if not path.exists():
            return None
        try:
            return json.loads(path.read_text())
        except (json.JSONDecodeError, OSError):
            logger.warning("Failed to read %s %s/data.json, ignoring", self._label, key)
            return None

    def write_json(self, key: str, data: Any, meta: dict | None = None) -> None:
        slot = self._slot(key)
        slot.mkdir(parents=True, exist_ok=True)
        (slot / "data.json").write_text(json.dumps(data, indent=2, ensure_ascii=False))
        if meta is not None:
            (slot / "meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False))

    def read_text(self, key: str, rel_path: str) -> str | None:
        path = self._slot(key) / "data" / rel_path
        if not path.exists():
            return None
        try:
            return path.read_text()
        except OSError:
            return None

    def write_text(self, key: str, rel_path: str, text: str) -> None:
        path = self._slot(key) / "data" / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)


# ---------------------------------------------------------------------------
# CacheManager
# ---------------------------------------------------------------------------


class CacheManager:
    """Content-addressable two-layer disk cache.

    * **blobs** live under ``cache_dir/blobs/<hash16>/``
    * **composites** live under ``cache_dir/composites/<hash16>/``

    Each slot can hold:
    * ``data.json`` -- primary JSON payload
    * ``meta.json`` -- optional metadata
    * ``data/``     -- arbitrary sub-files (text)
    """

    def __init__(self, config: Config) -> None:
        self.config = config
        self.cache_dir = config.cache_dir
        self._clear_legacy_cache()
        self._blobs = _CacheLayer(self.cache_dir / "blobs", "blob")
        self._composites = _CacheLayer(self.cache_dir / "composites", "composite")

    def _clear_legacy_cache(self) -> None:
        """Clear old v1 caches that used manifest.json (one-time migration)."""
        manifest = self.cache_dir / "manifest.json"
        if not manifest.exists():
            return
        try:
            data = json.loads(manifest.read_text())
            if data.get("version", 0) >= CACHE_VERSION:
                return
        except (json.JSONDecodeError, OSError):
            pass
        logger.info("Clearing legacy v1 cache at %s", self.cache_dir)
        self.clear()

    # -- Layer 1: blobs -----------------------------------------------------

    def has_blob(self, file_hash: str) -> bool:
        """Return True if a blob slot exists for *file_hash*."""
        return self._blobs.has(file_hash)

    def read_blob(self, file_hash: str) -> Any | None:
        """Read ``data.json`` from a blob slot, or ``None`` on miss."""
        return self._blobs.read_json(file_hash)

    def write_blob(self, file_hash: str, data: Any, meta: dict | None = None) -> None:
        """Write ``data.json`` (and optional ``meta.json``) into a blob slot."""
        self._blobs.write_json(file_hash, data, meta)

    def read_blob_text(self, file_hash: str, rel_path: str) -> str | None:
        """Read ``data/<rel_path>`` from a blob slot, or ``None`` on miss."""
        return self._blobs.read_text(file_hash, rel_path)

    def write_blob_text(self, file_hash: str, rel_path: str, text: str) -> None:
        """Write ``data/<rel_path>`` into a blob slot."""
        self._blobs.write_text(file_hash, rel_path, text)

    # -- Layer 2: composites ------------------------------------------------

    def has_composite(self, comp_hash: str) -> bool:
        """Return True if a composite slot exists for *comp_hash*."""
        return self._composites.has(comp_hash)

    def read_composite(self, comp_hash: str) -> Any | None:
        """Read ``data.json`` from a composite slot, or ``None`` on miss."""
        return self._composites.read_json(comp_hash)

    def write_composite(self, comp_hash: str, data: Any, meta: dict | None = None) -> None:
        """Write ``data.json`` (and optional ``meta.json``) into a composite slot."""
        self._composites.write_json(comp_hash, data, meta)

    def read_composite_text(self, comp_hash: str, rel_path: str) -> str | None:
        """Read ``data/<rel_path>`` from a composite slot, or ``None`` on miss."""
        return self._composites.read_text(comp_hash, rel_path)

    def write_composite_text(self, comp_hash: str, rel_path: str, text: str) -> None:
        """Write ``data/<rel_path>`` into a composite slot."""
        self._composites.write_text(comp_hash, rel_path, text)

    # -- utility ------------------------------------------------------------

    def clear(self) -> None:
        """Remove all cached data."""
        if self.cache_dir.exists():
            shutil.rmtree(self.cache_dir)
        logger.info("Cache cleared: %s", self.cache_dir)
