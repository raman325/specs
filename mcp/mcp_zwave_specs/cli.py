"""CLI entry point for zwave-specs-mcp server."""

from __future__ import annotations

import argparse
import logging
import shutil
import time
from pathlib import Path

from mcp_zwave_specs.cache import CacheManager
from mcp_zwave_specs.config import CACHE_SUBDIR, Config
from mcp_zwave_specs.server import create_server
from mcp_zwave_specs.state import AppState

logger = logging.getLogger(__name__)


def _clear_cache(cache_dir: Path) -> None:
    """Remove the cache directory after basic safety checks."""
    resolved = cache_dir.resolve()
    # Safety: only clear directories that end with our cache subdir name
    if resolved.name != CACHE_SUBDIR:
        logger.error(
            "Refusing to clear cache: path does not end with %s: %s", CACHE_SUBDIR, resolved
        )
        return
    if not resolved.exists():
        return
    shutil.rmtree(resolved)
    logger.info("Cache cleared: %s", resolved)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse CLI arguments for the MCP server."""
    parser = argparse.ArgumentParser(
        prog="zwave-specs-mcp",
        description="MCP server for querying the Z-Wave specification",
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=None,
        help="Path to TOML config file",
    )
    parser.add_argument(
        "--specs-dir",
        type=Path,
        default=None,
        help=(
            "Path to zwave-js/specs checkout"
            " (default: $ZWAVE_SPECS_MCP_SPECS_DIR or auto-detected from package location)"
        ),
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=None,
        help="Cache directory (default: $ZWAVE_SPECS_MCP_CACHE_DIR or <specs-dir>/.cache)",
    )
    parser.add_argument(
        "--app-layer-rst-dir",
        type=Path,
        default=None,
        help="Path to RST source directory for the application layer spec (alternative to PDF)",
    )
    parser.add_argument(
        "--clear-cache",
        action="store_true",
        help="Clear the cache directory before starting",
    )
    parser.add_argument(
        "--build-cache",
        action="store_true",
        help="Build/warm the cache and exit (does not start the server)",
    )
    return parser.parse_args(argv)


def build_config(args: argparse.Namespace) -> Config:
    """Build a Config with precedence: CLI flags > TOML file > env vars > defaults."""
    config = Config.from_env()
    if args.config is not None:
        if not args.config.exists():
            raise SystemExit(f"Config file not found: {args.config}")
        try:
            config.merge_toml(args.config)
        except Exception as exc:
            raise SystemExit(f"Invalid config file {args.config}: {exc}") from exc
    if args.specs_dir is not None:
        config.specs_dir = args.specs_dir.expanduser().resolve()
    if args.cache_dir is not None:
        cache_dir = args.cache_dir.expanduser().resolve()
        if cache_dir.name != CACHE_SUBDIR:
            cache_dir = cache_dir / CACHE_SUBDIR
        config.cache_dir = cache_dir
    if args.app_layer_rst_dir is not None:
        config.app_layer_rst_dir = args.app_layer_rst_dir.expanduser().resolve()
    return config


def _build_cache(config: Config) -> None:
    """Eagerly load all data categories to warm the disk cache."""
    start = time.monotonic()
    cache = CacheManager(config)
    state = AppState(config=config, cache=cache)
    state.build_all()
    elapsed = time.monotonic() - start
    logger.info("Cache built in %.1fs: %s", elapsed, config.cache_dir)


def main(argv: list[str] | None = None) -> None:
    """Entry point: parse args, build config, and run the MCP server."""
    logging.basicConfig(level=logging.INFO)
    args = parse_args(argv)
    config = build_config(args)

    if args.clear_cache:
        _clear_cache(config.cache_dir)

    if args.build_cache:
        _build_cache(config)
        return

    server = create_server(config)
    server.run()
