"""CLI entry point for zwave-specs-mcp server."""

from __future__ import annotations

import argparse
import logging
import shutil
from pathlib import Path

from mcp_zwave_specs.config import DEFAULT_CACHE_DIR, Config

logger = logging.getLogger(__name__)

# Refuse to delete these directories even if configured as cache_dir.
_UNSAFE_CACHE_PATHS = {Path("/"), Path.home(), Path.home() / "Documents"}


def _clear_cache(cache_dir: Path) -> None:
    """Remove the cache directory with safety checks against dangerous paths."""
    resolved = cache_dir.resolve()
    if resolved in _UNSAFE_CACHE_PATHS or resolved == Path.home():
        logger.error("Refusing to delete unsafe cache path: %s", resolved)
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
        help=f"Cache directory (default: $ZWAVE_SPECS_MCP_CACHE_DIR or {DEFAULT_CACHE_DIR})",
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
    return parser.parse_args(argv)


def build_config(args: argparse.Namespace) -> Config:
    """Build a Config with precedence: CLI flags > TOML file > env vars > defaults."""
    config = Config.from_env()
    if args.config is not None:
        config.merge_toml(args.config)
    if args.specs_dir is not None:
        config.specs_dir = args.specs_dir.expanduser().resolve()
    if args.cache_dir is not None:
        config.cache_dir = args.cache_dir.expanduser().resolve()
    if args.app_layer_rst_dir is not None:
        config.app_layer_rst_dir = args.app_layer_rst_dir.expanduser().resolve()
    return config


def main(argv: list[str] | None = None) -> None:
    """Entry point: parse args, build config, and run the MCP server."""
    args = parse_args(argv)
    config = build_config(args)

    if args.clear_cache:
        _clear_cache(config.cache_dir)

    from mcp_zwave_specs.server import create_server

    server = create_server(config)
    server.run()
