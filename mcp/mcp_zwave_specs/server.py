"""FastMCP server with Z-Wave specification tools."""

from __future__ import annotations

import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from difflib import get_close_matches

from fastmcp import Context, FastMCP

from mcp_zwave_specs.cache import CacheManager
from mcp_zwave_specs.config import Config
from mcp_zwave_specs.formatters import (
    format_cc_header,
    format_device_class,
    format_pdf_source,
    format_registry_search,
    search_app_layer_chapter,
    search_supplementary_group,
)
from mcp_zwave_specs.state import AppState

logger = logging.getLogger(__name__)

CLONE_INSTRUCTIONS = (
    "The zwave-js/specs repository is required but was not found.\n"
    "Clone it with:\n"
    "  git clone https://github.com/zwave-js/specs.git\n"
    "Then start the server with:\n"
    "  zwave-specs-mcp --specs-dir /path/to/specs"
)


def _get_state(ctx: Context) -> AppState:
    """Get the AppState from the server."""
    return ctx.fastmcp._app_state


@asynccontextmanager
async def lifespan(server: FastMCP) -> AsyncIterator[dict]:
    """Initialize AppState and CacheManager for the server's lifetime."""
    config = server._app_config
    cache = CacheManager(config)

    if not config.specs_available:
        logger.warning("Specs directory not found: %s", config.specs_dir)

    server._app_state = AppState(config=config, cache=cache)
    yield {}


def create_server(config: Config) -> FastMCP:
    """Create and configure the FastMCP server with all Z-Wave tools."""
    mcp = FastMCP(
        "Z-Wave MCP",
        instructions="Query the Z-Wave specification — Command Classes, registries, and more",
        lifespan=lifespan,
    )
    mcp._app_config = config

    # --- Command Class Tools ---

    @mcp.tool()
    async def list_command_classes(
        ctx: Context,
        category: str | None = None,
        include_deprecated: bool = False,
    ) -> str:
        """List all Z-Wave Command Classes with their IDs, versions, and status.

        Args:
            category: Filter by category (application, management, transport, network, control)
            include_deprecated: Include deprecated/obsoleted CCs (default: False)
        """
        state = _get_state(ctx)
        if not state.config.specs_available and not state.config.app_layer_rst_available:
            return CLONE_INSTRUCTIONS

        state.ensure_app_layer()
        state.ensure_header()

        lines = ["# Z-Wave Command Classes\n"]
        lines.append("| CC Name | CC ID | Versions | Status | Category |")
        lines.append("|---------|-------|----------|--------|----------|")

        for name in sorted(state.cc_sections):
            cc = state.cc_sections[name]
            if category and cc.category != category:
                continue
            status = cc.status.lower()
            if not include_deprecated and (
                status.startswith("deprecat") or status.startswith("obsolet")
            ):
                continue
            lines.append(
                f"| {cc.name} | {cc.id_hex} | {cc.version_str} | {cc.status} | {cc.category} |"
            )

        return "\n".join(lines)

    @mcp.tool()
    async def get_command_class(
        ctx: Context,
        name: str | None = None,
        cc_id: int | None = None,
    ) -> str:
        """Get the full specification text for a Z-Wave Command Class.

        Args:
            name: CC name (e.g., "Door Lock", "Notification"). Fuzzy-matched.
            cc_id: CC ID as integer (e.g., 98 for 0x62). Alternative to name.
        """
        state = _get_state(ctx)
        if not state.config.specs_available and not state.config.app_layer_rst_available:
            return CLONE_INSTRUCTIONS

        cc = state.find_cc(name, cc_id)
        if cc is None:
            search_term = name or (f"0x{cc_id:02X}" if cc_id else "unknown")
            suggestions = state.suggest_cc_names(search_term) if name else []
            msg = f"Command Class '{search_term}' not found."
            if suggestions:
                msg += f"\n\nDid you mean: {', '.join(suggestions)}?"
            return msg

        header = format_cc_header(cc, state.config)
        return f"{header}\n\n---\n\n{cc.content}"

    @mcp.tool()
    async def search_command_classes(
        ctx: Context,
        query: str,
        max_results: int = 5,
    ) -> str:
        """Search across all Command Class specifications.

        Args:
            query: Search terms (e.g., "thermostat setpoint", "door lock operation")
            max_results: Maximum results to return (default: 5)
        """
        state = _get_state(ctx)
        if not state.config.specs_available and not state.config.app_layer_rst_available:
            return CLONE_INSTRUCTIONS

        state.ensure_app_layer()

        results = state.search_index.search(query, max_results=max_results)
        if not results:
            return f"No results found for '{query}'."

        lines = [f"# Search Results for '{query}'\n"]
        for r in results:
            cc = state.cc_sections.get(r.key)
            if cc:
                lines.append(f"## {cc.name} ({cc.id_hex}, {cc.version_str})")
                lines.append(f"- Section: {cc.section_number}")
                lines.append(f"- Score: {r.score:.1f}")
                lines.append(f"- Snippet: {r.snippet}")
                lines.append("")

        return "\n".join(lines)

    @mcp.tool()
    async def get_cc_commands(
        ctx: Context,
        name: str | None = None,
        cc_id: int | None = None,
    ) -> str:
        """Get commands, opcodes, and frame struct definitions for a CC from the C header.

        Args:
            name: CC name (e.g., "Door Lock"). Fuzzy-matched.
            cc_id: CC ID as integer. Alternative to name.
        """
        state = _get_state(ctx)
        if not state.config.specs_available:
            return CLONE_INSTRUCTIONS

        state.ensure_header()

        # Find by ID or name
        hd = None
        if cc_id is not None:
            for h in state.header_data.values():
                if h.cc_id == cc_id:
                    hd = h
                    break
        elif name:
            hd = state.header_data.get(name)
            if not hd:
                lower_map = {k.lower(): k for k in state.header_data}
                matches = get_close_matches(name.lower(), lower_map.keys(), n=1, cutoff=0.6)
                if matches:
                    hd = state.header_data[lower_map[matches[0]]]

        if hd is None:
            return f"No header data found for '{name or cc_id}'."

        lines = [f"# {hd.name} Command Class ({hd.id_hex})"]
        lines.append("\nSource: `ZW_classcmd.h`\n")

        if hd.commands:
            lines.append("## Commands\n")
            lines.append("| Command | Opcode |")
            lines.append("|---------|--------|")
            for cmd in sorted(hd.commands, key=lambda c: c.opcode):
                lines.append(f"| {cmd.name} | {cmd.opcode_hex} |")

        if hd.structs:
            lines.append("\n## Frame Structures\n")
            for struct in hd.structs[:10]:  # Limit to avoid huge responses
                lines.append(f"### {struct.name}\n")
                lines.append("| Field | Type |")
                lines.append("|-------|------|")
                for f in struct.fields:
                    lines.append(f"| {f.name} | {f.type} |")
                lines.append("")

            if len(hd.structs) > 10:
                lines.append(f"\n*...and {len(hd.structs) - 10} more structs*")

        return "\n".join(lines)

    # --- Registry Tools ---

    @mcp.tool()
    async def lookup_notification(
        ctx: Context,
        search: str | None = None,
    ) -> str:
        """Look up Notification CC types and events.

        Args:
            search: Search by type name (e.g., "Smoke", "Access Control") or
                event text (e.g., "door", "intrusion"). Omit to list all.
        """
        state = _get_state(ctx)
        if not state.config.specs_available:
            return CLONE_INSTRUCTIONS

        state.ensure_registries()
        reg = state.registries.get("notification_types")
        if not reg:
            return "Notification registry not available."

        return format_registry_search(reg, search, ["Notification Type", "col_1"])

    @mcp.tool()
    async def lookup_sensor_type(
        ctx: Context,
        sensor_type: str | None = None,
    ) -> str:
        """Look up Multilevel Sensor types, scales, and units.

        Args:
            sensor_type: Filter by sensor type name (e.g., "Temperature", "Humidity")
        """
        state = _get_state(ctx)
        if not state.config.specs_available:
            return CLONE_INSTRUCTIONS

        state.ensure_registries()
        reg = state.registries.get("sensor_types")
        if not reg:
            return "Sensor type registry not available."

        return format_registry_search(reg, sensor_type)

    @mcp.tool()
    async def lookup_manufacturer(
        ctx: Context,
        name: str | None = None,
        manufacturer_id: str | None = None,
    ) -> str:
        """Look up Z-Wave manufacturer name or ID.

        Args:
            name: Manufacturer name to search for
            manufacturer_id: Manufacturer ID (hex string like "0x0086")
        """
        state = _get_state(ctx)
        if not state.config.specs_available:
            return CLONE_INSTRUCTIONS

        state.ensure_registries()
        reg = state.registries.get("manufacturers")
        if not reg:
            return "Manufacturer registry not available."

        search = name or manufacturer_id
        return format_registry_search(reg, search, ["Customer", "ID"])

    @mcp.tool()
    async def lookup_registry(
        ctx: Context,
        registry: str,
        search: str | None = None,
    ) -> str:
        """Generic lookup for any Z-Wave registry.

        Args:
            registry: Registry key (e.g., "icon_types", "av_control_codes",
                "indicator_types", "command_classes", "cc_commands").
                Use list_spec_documents() to see available registries.
            search: Optional search text to filter rows
        """
        state = _get_state(ctx)
        if not state.config.specs_available:
            return CLONE_INSTRUCTIONS

        state.ensure_registries()
        reg = state.registries.get(registry)
        if not reg:
            available = ", ".join(sorted(state.registries.keys()))
            return f"Registry '{registry}' not found. Available: {available}"

        return format_registry_search(reg, search)

    @mcp.tool()
    async def get_lifeline_requirements(
        ctx: Context,
        command_class: str | None = None,
    ) -> str:
        """Get mandatory Lifeline Association Group commands for a Command Class.

        Lists the commands a device MUST send via the Lifeline when state changes.
        Essential for device configuration and integration development.

        Args:
            command_class: CC name (e.g., "Door Lock", "Battery"). Omit to list all.
        """
        state = _get_state(ctx)
        if not state.config.specs_available:
            return CLONE_INSTRUCTIONS

        state.ensure_registries()
        reg = state.registries.get("lifeline_association_commands")
        if not reg:
            return "Lifeline association registry not available."

        if command_class:
            return format_registry_search(reg, command_class, ["Command Class"])
        return format_registry_search(reg, None)

    # --- Spec Reference Tools ---

    @mcp.tool()
    async def get_spec_section(
        ctx: Context,
        pdf: str,
        section: str | None = None,
        search: str | None = None,
    ) -> str:
        """Read a section from supplementary (non-CC) spec documents.

        Args:
            pdf: PDF key (e.g., "network_layer", "host_api")
            section: Section title or number to retrieve
            search: Search text to find relevant section
        """
        state = _get_state(ctx)
        if not state.config.specs_available:
            return CLONE_INSTRUCTIONS

        state.ensure_supplementary()
        sections = state.supplementary.get(pdf)
        if not sections:
            available = ", ".join(sorted(state.supplementary.keys()))
            return f"PDF '{pdf}' not found. Available: {available}"

        source = format_pdf_source(pdf, state.supplementary_paths.get(pdf), state.config)

        if section:
            for s in sections:
                if section.lower() in s.title.lower() or s.section_number == section:
                    return (
                        f"# {s.title}\n"
                        f"- Source: {source}\n"
                        f"- Pages: {s.page_start}-{s.page_end}\n\n"
                        f"---\n\n{s.content}"
                    )
            titles = [f"  - {s.section_number}: {s.title}" for s in sections]
            return f"Section '{section}' not found in {pdf}.\nAvailable sections:\n" + "\n".join(
                titles
            )

        if search:
            search_lower = search.lower()
            best = None
            best_count = 0
            for s in sections:
                count = s.content.lower().count(search_lower)
                if count > best_count:
                    best = s
                    best_count = count
            if best:
                return (
                    f"# {best.title}\n"
                    f"- Source: {source}\n"
                    f"- Pages: {best.page_start}-{best.page_end}\n"
                    f"- Matches: {best_count} occurrences of '{search}'\n\n"
                    f"---\n\n{best.content}"
                )
            return f"No results for '{search}' in {pdf}."

        # No filter — return TOC
        lines = [f"# {pdf} — Table of Contents\n"]
        for s in sections:
            lines.append(
                f"- **{s.section_number}**: {s.title} (pages {s.page_start}-{s.page_end})"
            )
        return "\n".join(lines)

    @mcp.tool()
    async def list_spec_documents(ctx: Context) -> str:
        """List all available Z-Wave spec documents, registries, and their contents."""
        state = _get_state(ctx)
        if not state.config.specs_available:
            return CLONE_INSTRUCTIONS

        lines = ["# Available Z-Wave Specification Documents\n"]

        # CC Specs from application layer document
        lines.append("## Command Class Specifications (Application Layer V5.0)")
        lines.append("Use `get_command_class()` or `list_command_classes()` to access.\n")

        # CC spec chapters (device types, role types, CC control)
        state.ensure_app_layer_chapters()
        if state.app_layer_chapters:
            lines.append("## Application Layer Chapters")
            for key, sections in sorted(state.app_layer_chapters.items()):
                tool_name = {
                    "device_types": "get_device_type()",
                    "role_types": "get_role_type()",
                    "cc_control": "get_cc_interview_steps()",
                }.get(key, f"(key: {key})")
                lines.append(f"- **{key}**: {len(sections)} sections — use `{tool_name}`")
            lines.append("")

        # Supplementary PDFs — grouped by category
        state.ensure_supplementary()
        if state.supplementary:
            # Group by prefix
            categories = {
                "Stack Specifications": lambda k: (
                    k
                    in (
                        "network_layer",
                        "host_api",
                        "long_range_phy_mac",
                    )
                ),
                "Security": lambda k: k.startswith("security_"),
                "Test Specifications (get_test_spec)": lambda k: k.startswith("test_"),
                "Legacy Specifications (get_legacy_spec)": lambda k: k.startswith("legacy_"),
                "SmartStart": lambda k: k.startswith("smartstart_"),
                "Application Notes (search_application_notes)": lambda k: k.startswith("appnote_"),
                "Other": lambda k: True,  # catch-all
            }
            assigned: set[str] = set()
            for cat_name, matcher in categories.items():
                matched = {
                    k: v
                    for k, v in state.supplementary.items()
                    if matcher(k) and k not in assigned
                }
                if not matched:
                    continue
                assigned.update(matched)
                lines.append(f"## {cat_name}")
                for key, sections in sorted(matched.items()):
                    lines.append(f"- **`{key}`**: {len(sections)} sections")
                lines.append("")

        # Registries
        state.ensure_registries()
        if state.registries:
            lines.append("## Registries")
            lines.append("Use `lookup_registry(registry=key)` to access.\n")
            for key, reg in sorted(state.registries.items()):
                lines.append(f"- **`{key}`**: {reg.name} ({len(reg.rows)} entries)")

        return "\n".join(lines)

    # --- CC Spec Chapter Tools (Device Types, Role Types, CC Control) ---

    @mcp.tool()
    async def get_device_type(
        ctx: Context,
        name: str | None = None,
    ) -> str:
        """Get Z-Wave Device Type definition from the application layer spec, Chapter 7.

        Includes mandatory and recommended CC requirements for each device type.

        Args:
            name: Device type name (e.g., "Thermostat", "Sensor"). Omit to list all.
        """
        state = _get_state(ctx)
        if not state.config.specs_available and not state.config.app_layer_rst_available:
            return CLONE_INSTRUCTIONS

        state.ensure_app_layer_chapters()
        return search_app_layer_chapter(
            state.app_layer_chapters.get("device_types", []), state.config, "Device Types", name
        )

    @mcp.tool()
    async def get_role_type(
        ctx: Context,
        name: str | None = None,
    ) -> str:
        """Get Z-Wave Role Type definition from the application layer spec, Chapter 8.

        Role types define network behavior: CSC, SSC, PC, RPC, PEN, AOEN, etc.

        Args:
            name: Role type name or abbreviation. Omit to list all.
        """
        state = _get_state(ctx)
        if not state.config.specs_available and not state.config.app_layer_rst_available:
            return CLONE_INSTRUCTIONS

        state.ensure_app_layer_chapters()
        return search_app_layer_chapter(
            state.app_layer_chapters.get("role_types", []), state.config, "Role Types", name
        )

    @mcp.tool()
    async def get_cc_interview_steps(
        ctx: Context,
        name: str | None = None,
    ) -> str:
        """Get CC interview/control requirements from the application layer spec, Chapter 6.

        Describes how a controller should interview devices for each CC.

        Args:
            name: CC name (e.g., "Door Lock", "Notification"). Omit to list all.
        """
        state = _get_state(ctx)
        if not state.config.specs_available and not state.config.app_layer_rst_available:
            return CLONE_INSTRUCTIONS

        state.ensure_app_layer_chapters()
        return search_app_layer_chapter(
            state.app_layer_chapters.get("cc_control", []),
            state.config,
            "CC Control / Interview",
            name,
        )

    # --- Device Class & Header Constants Tools ---

    @mcp.tool()
    async def get_device_class(
        ctx: Context,
        generic: str | None = None,
        specific: str | None = None,
        generic_id: int | None = None,
    ) -> str:
        """Look up Z-Wave Device Class (Generic/Specific types).

        The legacy device classification from ZW_classcmd.h that maps device
        class IDs to names. For the newer Device Type spec (application layer Ch. 7), use
        get_device_type() instead.

        Args:
            generic: Generic device class name (e.g., "Switch Binary"). Omit to list all.
            specific: Specific device class name to search for.
            generic_id: Generic device class ID (e.g., 16 for 0x10).
        """
        state = _get_state(ctx)
        if not state.config.specs_available:
            return CLONE_INSTRUCTIONS

        state.ensure_header()

        if not state.device_classes:
            return "No device class data found."

        # Filter by generic_id
        if generic_id is not None:
            for dc in state.device_classes:
                if dc.generic_id == generic_id:
                    return format_device_class(dc)
            return f"No generic device class with ID 0x{generic_id:02X}."

        # Search by generic name
        if generic:
            gl = generic.lower()
            for dc in state.device_classes:
                if gl in dc.generic_name.lower() or gl in dc.comment.lower():
                    return format_device_class(dc)
            return f"No generic device class matching '{generic}'."

        # Search by specific name
        if specific:
            sl = specific.lower()
            lines = ["# Device Class Search Results\n"]
            for dc in state.device_classes:
                matches = [
                    (name, sid, cmt)
                    for name, sid, cmt in dc.specific_types
                    if sl in name.lower() or sl in cmt.lower()
                ]
                if matches:
                    lines.append(f"## {dc.generic_name} (0x{dc.generic_id:02X})")
                    for name, sid, cmt in matches:
                        desc = f" — {cmt}" if cmt else ""
                        lines.append(f"- **{name}** (0x{sid:02X}){desc}")
                    lines.append("")
            if len(lines) > 1:
                return "\n".join(lines)
            return f"No specific type matching '{specific}'."

        # List all
        lines = ["# Z-Wave Device Classes\n"]
        lines.append("| Generic Class | ID | Specific Types |")
        lines.append("|--------------|-----|----------------|")
        for dc in state.device_classes:
            specifics = len(dc.specific_types)
            lines.append(f"| {dc.generic_name} | 0x{dc.generic_id:02X} | {specifics} |")
        return "\n".join(lines)

    @mcp.tool()
    async def search_application_notes(
        ctx: Context,
        search: str | None = None,
    ) -> str:
        """Search Z-Wave Application Notes (APL/INS documents).

        Covers Multi-Channel basics, Battery support, Networking basics,
        Control application basics, Time/Date, Development basics, and more.

        Args:
            search: Search text (e.g., "multi channel", "battery", "SDK7").
                Omit to list all available application notes.
        """
        state = _get_state(ctx)
        if not state.config.specs_available:
            return CLONE_INSTRUCTIONS

        state.ensure_supplementary()
        return search_supplementary_group(
            state.supplementary,
            state.supplementary_paths,
            state.config,
            "appnote_",
            "Application Notes",
            None,
            search,
        )

    @mcp.tool()
    async def get_test_spec(
        ctx: Context,
        pdf: str | None = None,
        search: str | None = None,
    ) -> str:
        """Look up Z-Wave test specifications for certification compliance.

        Covers PHY, MAC, Network layer tests and Long Range variants.

        Args:
            pdf: Specific test spec key (e.g., "test_phy", "test_mac",
                "test_network", "test_lr_phy"). Omit to list available.
            search: Search text. Searches within pdf if provided, otherwise
                searches across all test specs.
        """
        state = _get_state(ctx)
        if not state.config.specs_available:
            return CLONE_INSTRUCTIONS

        state.ensure_supplementary()
        return search_supplementary_group(
            state.supplementary,
            state.supplementary_paths,
            state.config,
            "test_",
            "Test Specifications",
            pdf,
            search,
        )

    @mcp.tool()
    async def get_legacy_spec(
        ctx: Context,
        pdf: str | None = None,
        section: str | None = None,
        search: str | None = None,
    ) -> str:
        """Look up legacy Z-Wave specifications.

        Includes 500 Series Application Programmer's Guide, 500 Series
        Serial API, legacy Device Class spec, and Z-Wave Plus v1 Device Types.

        Args:
            pdf: Specific legacy spec key (e.g., "legacy_500_app_guide",
                "legacy_500_serial_api"). Omit to list available.
            section: Section title to retrieve (requires pdf).
            search: Search text. Searches within pdf if provided, otherwise
                searches across all legacy specs.
        """
        state = _get_state(ctx)
        if not state.config.specs_available:
            return CLONE_INSTRUCTIONS

        state.ensure_supplementary()
        return search_supplementary_group(
            state.supplementary,
            state.supplementary_paths,
            state.config,
            "legacy_",
            "Legacy Specifications",
            pdf,
            search,
            section,
        )

    @mcp.tool()
    async def lookup_zwave_constants(
        ctx: Context,
        search: str,
        header: str | None = None,
    ) -> str:
        """Search Z-Wave C header constants (#define values).

        Covers Serial API function IDs, security keys, transport flags,
        controller API defines, NVM layout, and more.

        Args:
            search: Search text (matches define name or comment, e.g., "FUNC_ID",
                "security", "S2", "TRANSMIT_OPTION").
            header: Specific header file (e.g., "ZW_SerialAPI.h"). Omit to search all.
        """
        state = _get_state(ctx)
        if not state.config.specs_available:
            return CLONE_INSTRUCTIONS

        state.ensure_header_constants()
        if not state.header_constants:
            return "No header constants available."

        search_lower = search.lower()
        lines = [f"# Z-Wave Constants matching '{search}'\n"]
        total = 0

        files_to_search = state.header_constants.items()
        if header:
            if header in state.header_constants:
                files_to_search = [(header, state.header_constants[header])]
            else:
                available = ", ".join(sorted(state.header_constants))
                return f"Header '{header}' not found. Available: {available}"

        for fname, constants in sorted(files_to_search):
            matches = [
                c
                for c in constants
                if search_lower in c.name.lower() or search_lower in c.comment.lower()
            ]
            if not matches:
                continue

            lines.append(f"## {fname}\n")
            lines.append("| Define | Value | Description |")
            lines.append("|--------|-------|-------------|")
            for c in matches[:50]:
                lines.append(f"| {c.name} | {c.value} | {c.comment} |")
            if len(matches) > 50:
                lines.append(f"\n*...{len(matches) - 50} more matches*")
            lines.append("")
            total += len(matches)

        if total == 0:
            available = ", ".join(sorted(state.header_constants))
            return f"No constants matching '{search}'.\nAvailable headers: {available}"

        lines.insert(1, f"*{total} matches across header files*\n")
        return "\n".join(lines)

    return mcp


# Lazy module-level instance for `fastmcp dev` and `fastmcp run`.
# Uses __getattr__ so Config.from_env() is only called when `mcp` is
# actually accessed, not at import time.
_mcp: FastMCP | None = None


def __getattr__(name: str) -> object:
    global _mcp
    if name == "mcp":
        if _mcp is None:
            _mcp = create_server(Config.from_env())
        return _mcp
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
