"""Tests for the content-addressable blob cache."""

from __future__ import annotations

import time
from pathlib import Path

import pytest

from mcp_zwave_specs.cache import (
    CacheManager,
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
        """Hash changes when file content changes."""
        p = tmp_specs / "a.pdf"
        h1 = file_hash(p)
        p.write_text("different content")
        h2 = file_hash(p)
        assert h1 != h2

    def test_different_files_differ(self, tmp_specs: Path) -> None:
        """Two distinct files produce different hashes."""
        assert file_hash(tmp_specs / "a.pdf") != file_hash(tmp_specs / "b.pdf")

    def test_stable_across_rewrite(self, tmp_specs: Path) -> None:
        """Same content rewritten produces the same hash (mtime-independent)."""
        p = tmp_specs / "a.pdf"
        h1 = file_hash(p)
        time.sleep(0.05)  # ensure mtime differs
        p.write_text("pdf-a")  # same content
        h2 = file_hash(p)
        assert h1 == h2


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

    def test_stable_across_rewrite(self, tmp_specs: Path) -> None:
        """Same content rewritten produces the same hash (mtime-independent)."""
        h1 = dir_hash(tmp_specs)
        time.sleep(0.05)
        (tmp_specs / "a.pdf").write_text("pdf-a")  # same content
        h2 = dir_hash(tmp_specs)
        assert h1 == h2


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
        import json

        data = [1, 2]
        meta = {"source": "test.pdf", "timestamp": 12345}
        cache.write_blob("meta1", data, meta=meta)
        blob_dir = cache.cache_dir / "meta1"
        assert json.loads((blob_dir / "meta.json").read_text()) == meta

    def test_text_write_read(self, cache: CacheManager) -> None:
        cache.write_blob_text("txt1", "section/intro.md", "# Hello")
        result = cache.read_blob_text("txt1", "section/intro.md")
        assert result == "# Hello"

    def test_text_missing_returns_none(self, cache: CacheManager) -> None:
        assert cache.read_blob_text("txt1", "nope.md") is None


# ---------------------------------------------------------------------------
# clear()
# ---------------------------------------------------------------------------


class TestClear:
    def test_clear_removes_everything(self, cache: CacheManager) -> None:
        cache.write_blob("b1", {"x": 1})
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


# ---------------------------------------------------------------------------
# write_gitignore()
# ---------------------------------------------------------------------------


class TestGitignore:
    def test_write_creates_file(self, cache: CacheManager) -> None:
        """write_gitignore() creates .gitignore in the cache dir."""
        cache.write_blob("a1b2c3d4e5f67890", {"x": 1})
        cache.write_gitignore()
        gi = cache.cache_dir / ".gitignore"
        assert gi.exists()
        content = gi.read_text()
        assert "*" in content
        assert "!.gitignore" in content

    def test_includes_blob_dirs(self, cache: CacheManager) -> None:
        """16-char hex dirs are negated in .gitignore."""
        cache.write_blob("a1b2c3d4e5f67890", {"x": 1})
        cache.write_blob("0123456789abcdef", {"y": 2})
        cache.write_gitignore()
        content = (cache.cache_dir / ".gitignore").read_text()
        assert "!0123456789abcdef/" in content
        assert "!0123456789abcdef/**" in content
        assert "!a1b2c3d4e5f67890/" in content
        assert "!a1b2c3d4e5f67890/**" in content

    def test_ignores_non_blob_dirs(self, cache: CacheManager) -> None:
        """Directories that aren't 16-char hex are not included."""
        cache.write_blob("a1b2c3d4e5f67890", {"x": 1})
        # Create a non-hex directory
        (cache.cache_dir / "__pycache__").mkdir()
        (cache.cache_dir / "short").mkdir()
        cache.write_gitignore()
        content = (cache.cache_dir / ".gitignore").read_text()
        assert "__pycache__" not in content
        assert "short" not in content
        assert "!a1b2c3d4e5f67890/" in content

    def test_noop_no_cache_dir(self, cache: CacheManager) -> None:
        """No error when cache directory doesn't exist."""
        assert not cache.cache_dir.exists()
        cache.write_gitignore()  # should not raise
