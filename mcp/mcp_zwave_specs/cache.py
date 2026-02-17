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
# Public hash helpers (used by server.py and other modules)
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
        self._maybe_migrate()

    # -- migration ----------------------------------------------------------

    def _maybe_migrate(self) -> None:
        """If an old v1 cache is detected, clear it."""
        manifest_path = self.cache_dir / "manifest.json"
        if manifest_path.exists():
            try:
                data = json.loads(manifest_path.read_text())
                if data.get("version", 0) < CACHE_VERSION:
                    logger.info(
                        "Migrating cache from v%d to v%d",
                        data.get("version", 0),
                        CACHE_VERSION,
                    )
                    self.clear()
            except (json.JSONDecodeError, OSError):
                self.clear()

    # -- Layer 1: blobs -----------------------------------------------------

    def _blob_dir(self, file_hash: str) -> Path:
        return self.cache_dir / "blobs" / file_hash

    def has_blob(self, file_hash: str) -> bool:
        """Return True if a blob slot exists for *file_hash*."""
        return self._blob_dir(file_hash).is_dir()

    def read_blob(self, file_hash: str) -> Any | None:
        """Read ``data.json`` from a blob slot, or ``None`` on miss."""
        path = self._blob_dir(file_hash) / "data.json"
        if not path.exists():
            return None
        try:
            return json.loads(path.read_text())
        except (json.JSONDecodeError, OSError):
            logger.warning("Failed to read blob %s/data.json, ignoring", file_hash)
            return None

    def write_blob(self, file_hash: str, data: Any, meta: dict | None = None) -> None:
        """Write ``data.json`` (and optional ``meta.json``) into a blob slot."""
        slot = self._blob_dir(file_hash)
        slot.mkdir(parents=True, exist_ok=True)
        (slot / "data.json").write_text(json.dumps(data, indent=2, ensure_ascii=False))
        if meta is not None:
            (slot / "meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False))

    def read_blob_text(self, file_hash: str, rel_path: str) -> str | None:
        """Read ``data/<rel_path>`` from a blob slot, or ``None`` on miss."""
        path = self._blob_dir(file_hash) / "data" / rel_path
        if not path.exists():
            return None
        try:
            return path.read_text()
        except OSError:
            return None

    def write_blob_text(self, file_hash: str, rel_path: str, text: str) -> None:
        """Write ``data/<rel_path>`` into a blob slot."""
        path = self._blob_dir(file_hash) / "data" / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    # -- Layer 2: composites ------------------------------------------------

    def _composite_dir(self, comp_hash: str) -> Path:
        return self.cache_dir / "composites" / comp_hash

    def has_composite(self, comp_hash: str) -> bool:
        """Return True if a composite slot exists for *comp_hash*."""
        return self._composite_dir(comp_hash).is_dir()

    def read_composite(self, comp_hash: str) -> Any | None:
        """Read ``data.json`` from a composite slot, or ``None`` on miss."""
        path = self._composite_dir(comp_hash) / "data.json"
        if not path.exists():
            return None
        try:
            return json.loads(path.read_text())
        except (json.JSONDecodeError, OSError):
            logger.warning("Failed to read composite %s/data.json, ignoring", comp_hash)
            return None

    def write_composite(self, comp_hash: str, data: Any, meta: dict | None = None) -> None:
        """Write ``data.json`` (and optional ``meta.json``) into a composite slot."""
        slot = self._composite_dir(comp_hash)
        slot.mkdir(parents=True, exist_ok=True)
        (slot / "data.json").write_text(json.dumps(data, indent=2, ensure_ascii=False))
        if meta is not None:
            (slot / "meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False))

    def read_composite_text(self, comp_hash: str, rel_path: str) -> str | None:
        """Read ``data/<rel_path>`` from a composite slot, or ``None`` on miss."""
        path = self._composite_dir(comp_hash) / "data" / rel_path
        if not path.exists():
            return None
        try:
            return path.read_text()
        except OSError:
            return None

    def write_composite_text(self, comp_hash: str, rel_path: str, text: str) -> None:
        """Write ``data/<rel_path>`` into a composite slot."""
        path = self._composite_dir(comp_hash) / "data" / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    # -- utility ------------------------------------------------------------

    def clear(self) -> None:
        """Remove all cached data."""
        if self.cache_dir.exists():
            shutil.rmtree(self.cache_dir)
        logger.info("Cache cleared: %s", self.cache_dir)
