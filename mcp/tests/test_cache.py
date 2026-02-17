"""Tests for the content-addressable two-layer cache."""

from __future__ import annotations

import json
import time
from pathlib import Path

import pytest

from mcp_zwave_specs.cache import (
    CACHE_VERSION,
    CacheManager,
    composite_hash,
    dir_hash,
    file_hash,
)
from mcp_zwave_specs.config import Config

# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture()
def tmp_specs(tmp_path: Path) -> Path:
    """Create a minimal specs directory with a few files."""
    specs = tmp_path / "specs"
    specs.mkdir()
    (specs / "a.pdf").write_text("pdf-a")
    (specs / "b.pdf").write_text("pdf-b")
    sub = specs / "sub"
    sub.mkdir()
    (sub / "c.h").write_text("header-c")
    return specs


@pytest.fixture()
def config(tmp_path: Path, tmp_specs: Path) -> Config:
    """Return a Config that points at temporary directories."""
    return Config(specs_dir=tmp_specs, cache_dir=tmp_path / "cache" / "zwave-specs")


@pytest.fixture()
def cache(config: Config) -> CacheManager:
    return CacheManager(config)


# ---------------------------------------------------------------------------
# file_hash
# ---------------------------------------------------------------------------


class TestFileHash:
    def test_consistent(self, tmp_specs: Path) -> None:
        """Same file produces the same hash on repeated calls."""
        p = tmp_specs / "a.pdf"
        assert file_hash(p) == file_hash(p)

    def test_length(self, tmp_specs: Path) -> None:
        """Hash is 16 hex characters."""
        h = file_hash(tmp_specs / "a.pdf")
        assert len(h) == 16
        assert all(c in "0123456789abcdef" for c in h)

    def test_changes_on_content_change(self, tmp_specs: Path) -> None:
        """Hash changes when file content (and thus mtime/size) changes."""
        p = tmp_specs / "a.pdf"
        h1 = file_hash(p)
        time.sleep(0.05)  # ensure mtime differs
        p.write_text("different content")
        h2 = file_hash(p)
        assert h1 != h2

    def test_different_files_differ(self, tmp_specs: Path) -> None:
        """Two distinct files produce different hashes."""
        assert file_hash(tmp_specs / "a.pdf") != file_hash(tmp_specs / "b.pdf")


# ---------------------------------------------------------------------------
# dir_hash
# ---------------------------------------------------------------------------


class TestDirHash:
    def test_consistent(self, tmp_specs: Path) -> None:
        assert dir_hash(tmp_specs) == dir_hash(tmp_specs)

    def test_length(self, tmp_specs: Path) -> None:
        h = dir_hash(tmp_specs)
        assert len(h) == 16

    def test_changes_on_file_change(self, tmp_specs: Path) -> None:
        h1 = dir_hash(tmp_specs)
        time.sleep(0.05)
        (tmp_specs / "a.pdf").write_text("changed")
        h2 = dir_hash(tmp_specs)
        assert h1 != h2

    def test_extensions_filter(self, tmp_specs: Path) -> None:
        """When extensions are given, only matching files contribute."""
        h_all = dir_hash(tmp_specs)
        h_pdf = dir_hash(tmp_specs, extensions=frozenset({".pdf"}))
        h_h = dir_hash(tmp_specs, extensions=frozenset({".h"}))
        # All three should be different because different files are included
        assert h_all != h_pdf
        assert h_pdf != h_h

    def test_skips_pycache(self, tmp_specs: Path) -> None:
        """__pycache__ directories are excluded from hashing."""
        h1 = dir_hash(tmp_specs)
        pycache = tmp_specs / "__pycache__"
        pycache.mkdir()
        (pycache / "junk.pyc").write_bytes(b"\x00" * 100)
        h2 = dir_hash(tmp_specs)
        assert h1 == h2


# ---------------------------------------------------------------------------
# composite_hash
# ---------------------------------------------------------------------------


class TestCompositeHash:
    def test_deterministic(self) -> None:
        assert composite_hash(["aaa", "bbb"]) == composite_hash(["aaa", "bbb"])

    def test_order_independent(self) -> None:
        """Input hashes are sorted internally, so order doesn't matter."""
        assert composite_hash(["aaa", "bbb"]) == composite_hash(["bbb", "aaa"])

    def test_length(self) -> None:
        assert len(composite_hash(["x"])) == 16

    def test_config_hash_changes_result(self) -> None:
        h1 = composite_hash(["aaa"], config_hash="v1")
        h2 = composite_hash(["aaa"], config_hash="v2")
        assert h1 != h2

    def test_different_inputs_differ(self) -> None:
        assert composite_hash(["aaa"]) != composite_hash(["bbb"])


# ---------------------------------------------------------------------------
# Blob read/write round-trip
# ---------------------------------------------------------------------------


class TestBlob:
    def test_write_read_json(self, cache: CacheManager) -> None:
        data = {"command_classes": [1, 2, 3]}
        cache.write_blob("abc123", data)
        assert cache.has_blob("abc123")
        assert cache.read_blob("abc123") == data

    def test_read_missing_returns_none(self, cache: CacheManager) -> None:
        assert cache.read_blob("nonexistent") is None
        assert cache.has_blob("nonexistent") is False

    def test_write_with_meta(self, cache: CacheManager) -> None:
        data = [1, 2]
        meta = {"source": "test.pdf", "timestamp": 12345}
        cache.write_blob("meta1", data, meta=meta)
        blob_dir = cache.cache_dir / "blobs" / "meta1"
        assert json.loads((blob_dir / "meta.json").read_text()) == meta

    def test_text_write_read(self, cache: CacheManager) -> None:
        cache.write_blob_text("txt1", "section/intro.md", "# Hello")
        result = cache.read_blob_text("txt1", "section/intro.md")
        assert result == "# Hello"

    def test_text_missing_returns_none(self, cache: CacheManager) -> None:
        assert cache.read_blob_text("txt1", "nope.md") is None


# ---------------------------------------------------------------------------
# Composite read/write round-trip
# ---------------------------------------------------------------------------


class TestComposite:
    def test_write_read_json(self, cache: CacheManager) -> None:
        data = {"merged": True, "items": [10, 20]}
        cache.write_composite("comp1", data)
        assert cache.has_composite("comp1")
        assert cache.read_composite("comp1") == data

    def test_read_missing_returns_none(self, cache: CacheManager) -> None:
        assert cache.read_composite("nonexistent") is None
        assert cache.has_composite("nonexistent") is False

    def test_write_with_meta(self, cache: CacheManager) -> None:
        data = {"ok": True}
        meta = {"inputs": ["h1", "h2"]}
        cache.write_composite("comp_m", data, meta=meta)
        comp_dir = cache.cache_dir / "composites" / "comp_m"
        assert json.loads((comp_dir / "meta.json").read_text()) == meta

    def test_text_write_read(self, cache: CacheManager) -> None:
        cache.write_composite_text("comp_t", "report.txt", "All good")
        result = cache.read_composite_text("comp_t", "report.txt")
        assert result == "All good"

    def test_text_missing_returns_none(self, cache: CacheManager) -> None:
        assert cache.read_composite_text("comp_t", "nope.txt") is None


# ---------------------------------------------------------------------------
# Migration
# ---------------------------------------------------------------------------


class TestMigration:
    def test_old_v1_cache_cleared(self, config: Config) -> None:
        """When a v1 manifest exists, the cache is wiped on init."""
        config.cache_dir.mkdir(parents=True, exist_ok=True)
        manifest = config.cache_dir / "manifest.json"
        manifest.write_text(json.dumps({"version": 1, "specs_hash": "old"}))
        # Also place a stale file to prove it gets removed
        stale = config.cache_dir / "stale.json"
        stale.write_text("{}")

        cm = CacheManager(config)
        assert not manifest.exists()
        assert not stale.exists()
        # Manager is still usable
        cm.write_blob("fresh", {"new": True})
        assert cm.read_blob("fresh") == {"new": True}

    def test_corrupted_manifest_cleared(self, config: Config) -> None:
        """Corrupted manifest triggers a full clear."""
        config.cache_dir.mkdir(parents=True, exist_ok=True)
        manifest = config.cache_dir / "manifest.json"
        manifest.write_text("NOT JSON")

        cm = CacheManager(config)
        assert not manifest.exists()
        cm.write_blob("ok", [1])
        assert cm.read_blob("ok") == [1]

    def test_no_manifest_no_migration(self, config: Config) -> None:
        """Without a manifest file, no migration occurs and cache works."""
        cm = CacheManager(config)
        cm.write_blob("x", "data")
        assert cm.read_blob("x") == "data"

    def test_current_version_not_cleared(self, config: Config) -> None:
        """A manifest at current version should NOT trigger migration."""
        config.cache_dir.mkdir(parents=True, exist_ok=True)
        manifest = config.cache_dir / "manifest.json"
        manifest.write_text(json.dumps({"version": CACHE_VERSION}))
        sentinel = config.cache_dir / "keep_me.txt"
        sentinel.write_text("important")

        CacheManager(config)
        # manifest and sentinel should still exist
        assert manifest.exists()
        assert sentinel.exists()


# ---------------------------------------------------------------------------
# clear()
# ---------------------------------------------------------------------------


class TestClear:
    def test_clear_removes_everything(self, cache: CacheManager) -> None:
        cache.write_blob("b1", {"x": 1})
        cache.write_composite("c1", {"y": 2})
        cache.write_blob_text("b1", "f.txt", "hello")
        assert cache.cache_dir.exists()

        cache.clear()
        assert not cache.cache_dir.exists()

    def test_clear_idempotent(self, cache: CacheManager) -> None:
        """Clearing when nothing exists does not error."""
        cache.clear()
        cache.clear()

    def test_usable_after_clear(self, cache: CacheManager) -> None:
        cache.write_blob("b1", [1])
        cache.clear()
        cache.write_blob("b2", [2])
        assert cache.read_blob("b2") == [2]
        assert cache.read_blob("b1") is None
