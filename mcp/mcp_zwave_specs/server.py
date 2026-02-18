"""FastMCP server creation and lifespan management."""

from __future__ import annotations

import asyncio
import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastmcp import FastMCP
from fastmcp.tools import Tool

from mcp_zwave_specs.cache import CacheManager
from mcp_zwave_specs.config import Config
from mcp_zwave_specs.state import AppState
from mcp_zwave_specs.tools import ALL_TOOLS

logger = logging.getLogger(__name__)


def create_server(config: Config) -> FastMCP:
    """Create and configure the FastMCP server with all Z-Wave tools."""

    @asynccontextmanager
    async def lifespan(_: FastMCP) -> AsyncIterator[dict]:
        """Initialize AppState, CacheManager, and background cache warming."""
        cache = CacheManager(config)
        if not config.specs_available:
            logger.warning("Specs directory not found: %s", config.specs_dir)

        state = AppState(config=config, cache=cache)

        async def _warm() -> None:
            try:
                await asyncio.to_thread(state.build_all)
            except Exception:
                logger.exception("Background cache warming failed")

        task = asyncio.create_task(_warm())
        try:
            yield {"app_state": state, "cache_build_task": task}
        finally:
            task.cancel()

    return FastMCP(
        "Z-Wave MCP",
        instructions="Query the Z-Wave specification — Command Classes, registries, and more",
        lifespan=lifespan,
        tools=[Tool.from_function(func) for func in ALL_TOOLS],
    )


mcp = create_server(Config.from_env())
