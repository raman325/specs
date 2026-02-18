"""FastMCP server creation and lifespan management."""

from __future__ import annotations

import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastmcp import FastMCP

from mcp_zwave_specs.cache import CacheManager
from mcp_zwave_specs.config import Config
from mcp_zwave_specs.state import AppState
from mcp_zwave_specs.tools import ALL_TOOLS

logger = logging.getLogger(__name__)


def create_server(config: Config) -> FastMCP:
    """Create and configure the FastMCP server with all Z-Wave tools."""

    @asynccontextmanager
    async def lifespan(server: FastMCP) -> AsyncIterator[dict]:
        """Initialize AppState and CacheManager for the server's lifetime."""
        cache = CacheManager(config)
        if not config.specs_available:
            logger.warning("Specs directory not found: %s", config.specs_dir)

        yield {"app_state": AppState(config=config, cache=cache)}

    mcp = FastMCP(
        "Z-Wave MCP",
        instructions="Query the Z-Wave specification — Command Classes, registries, and more",
        lifespan=lifespan,
    )

    for func in ALL_TOOLS:
        mcp.tool()(func)

    return mcp


mcp = create_server(Config.from_env())
