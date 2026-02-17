"""CLI entry point for zwave-specs-mcp server."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from mcp_zwave_specs.config import DEFAULT_CACHE_DIR, Config


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
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
        help="Path to zwave-js/specs checkout (default: $ZWAVE_SPECS_MCP_SPECS_DIR or auto-detected from package location)",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=None,
        help=f"Cache directory (default: $ZWAVE_SPECS_MCP_CACHE_DIR or {DEFAULT_CACHE_DIR})",
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
        config.specs_dir = args.specs_dir.resolve()
    if args.cache_dir is not None:
        config.cache_dir = args.cache_dir.resolve()
    return config


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    config = build_config(args)

    if args.clear_cache and config.cache_dir.exists():
        shutil.rmtree(config.cache_dir)

    from mcp_zwave_specs.server import create_server

    server = create_server(config)
    server.run()
