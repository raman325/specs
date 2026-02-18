"""MCP tool functions for querying the Z-Wave specification."""

from __future__ import annotations

import asyncio
import contextlib
import logging
from difflib import get_close_matches

from fastmcp import Context

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

_STEP_LABELS = {
    "app_layer": "Loading command class specifications",
    "header": "Loading header data",
    "registries": "Loading registries",
    "supplementary": "Loading supplementary specifications",
    "app_layer_chapters": "Loading application layer chapters",
    "header_constants": "Loading header constants",
}


def _get_state(ctx: Context) -> AppState:
    """Get the AppState from the lifespan context."""
    return ctx.request_context.lifespan_context["app_state"]


async def _load(
    ctx: Context,
    *categories: str,
    also_rst: bool = False,
) -> tuple[AppState, str | None]:
    """Get state, check specs availability, and run ensure steps with progress.

    Returns ``(state, None)`` on success or ``(state, error_message)`` if
    specs are unavailable.
    """
    state = _get_state(ctx)
    available = state.config.specs_available or (also_rst and state.config.app_layer_rst_available)
    if not available:
        return state, CLONE_INSTRUCTIONS
    total = len(categories)
    for i, cat in enumerate(categories):
        await ctx.report_progress(progress=i, total=total, message=_STEP_LABELS[cat])
        await asyncio.to_thread(getattr(state, f"ensure_{cat}"))
    await ctx.report_progress(progress=total, total=total)
    return state, None


# --- Shared helpers for tool families ---


async def _registry_lookup(
    ctx: Context,
    key: str,
    not_found: str,
    search: str | None,
    search_columns: list[str] | None = None,
) -> str:
    """Load registries and format a single registry lookup."""
    state, err = await _load(ctx, "registries")
    if err:
        return err
    reg = state.registries.get(key)
    if not reg:
        return not_found
    return format_registry_search(reg, search, search_columns)


async def _chapter_lookup(ctx: Context, key: str, display_name: str, search: str | None) -> str:
    """Load app-layer chapters and search/list a specific chapter."""
    state, err = await _load(ctx, "app_layer_chapters", also_rst=True)
    if err:
        return err
    return search_app_layer_chapter(
        state.app_layer_chapters.get(key, []), state.config, display_name, search
    )


async def _supplementary_lookup(
    ctx: Context,
    prefix: str,
    display_name: str,
    pdf: str | None = None,
    search: str | None = None,
    section: str | None = None,
) -> str:
    """Load supplementary PDFs and search/list a group by prefix."""
    state, err = await _load(ctx, "supplementary")
    if err:
        return err
    return search_supplementary_group(
        state.supplementary,
        state.supplementary_paths,
        state.config,
        prefix,
        display_name,
        pdf,
        search,
        section,
    )


# --- Command Class Tools ---


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
    state, err = await _load(ctx, "app_layer", "header", also_rst=True)
    if err:
        return err

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
    state, err = await _load(ctx, "app_layer", also_rst=True)
    if err:
        return err

    cc = await asyncio.to_thread(state.find_cc, name, cc_id)
    if cc is None:
        search_term = name or (f"0x{cc_id:02X}" if cc_id else "unknown")
        suggestions = await asyncio.to_thread(state.suggest_cc_names, search_term) if name else []
        msg = f"Command Class '{search_term}' not found."
        if suggestions:
            msg += f"\n\nDid you mean: {', '.join(suggestions)}?"
        return msg

    header = format_cc_header(cc, state.config)
    return f"{header}\n\n---\n\n{cc.content}"


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
    state, err = await _load(ctx, "app_layer", also_rst=True)
    if err:
        return err

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
    state, err = await _load(ctx, "header")
    if err:
        return err

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


async def lookup_notification(
    ctx: Context,
    search: str | None = None,
) -> str:
    """Look up Notification CC types and events.

    Args:
        search: Search by type name (e.g., "Smoke", "Access Control") or
            event text (e.g., "door", "intrusion"). Omit to list all.
    """
    return await _registry_lookup(
        ctx,
        "notification_types",
        "Notification registry not available.",
        search,
        ["Notification Type", "col_1"],
    )


async def lookup_sensor_type(
    ctx: Context,
    sensor_type: str | None = None,
) -> str:
    """Look up Multilevel Sensor types, scales, and units.

    Args:
        sensor_type: Filter by sensor type name (e.g., "Temperature", "Humidity")
    """
    return await _registry_lookup(
        ctx,
        "sensor_types",
        "Sensor type registry not available.",
        sensor_type,
    )


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
    return await _registry_lookup(
        ctx,
        "manufacturers",
        "Manufacturer registry not available.",
        name or manufacturer_id,
        ["Customer", "ID"],
    )


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
    state, err = await _load(ctx, "registries")
    if err:
        return err

    reg = state.registries.get(registry)
    if not reg:
        available = ", ".join(sorted(state.registries.keys()))
        return f"Registry '{registry}' not found. Available: {available}"

    return format_registry_search(reg, search)


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
    return await _registry_lookup(
        ctx,
        "lifeline_association_commands",
        "Lifeline association registry not available.",
        command_class,
        ["Command Class"] if command_class else None,
    )


# --- Spec Reference Tools ---


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
    state, err = await _load(ctx, "supplementary")
    if err:
        return err

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
        lines.append(f"- **{s.section_number}**: {s.title} (pages {s.page_start}-{s.page_end})")
    return "\n".join(lines)


async def list_spec_documents(ctx: Context) -> str:
    """List all available Z-Wave spec documents, registries, and their contents."""
    state, err = await _load(ctx, "app_layer_chapters", "supplementary", "registries")
    if err:
        return err

    lines = ["# Available Z-Wave Specification Documents\n"]

    # CC Specs from application layer document
    lines.append("## Command Class Specifications (Application Layer V5.0)")
    lines.append("Use `get_command_class()` or `list_command_classes()` to access.\n")

    # CC spec chapters (device types, role types, CC control)
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
            "Other": lambda _: True,  # catch-all
        }
        assigned: set[str] = set()
        for cat_name, matcher in categories.items():
            matched = {
                k: v for k, v in state.supplementary.items() if matcher(k) and k not in assigned
            }
            if not matched:
                continue
            assigned.update(matched)
            lines.append(f"## {cat_name}")
            for key, sections in sorted(matched.items()):
                lines.append(f"- **`{key}`**: {len(sections)} sections")
            lines.append("")

    # Registries
    if state.registries:
        lines.append("## Registries")
        lines.append("Use `lookup_registry(registry=key)` to access.\n")
        for key, reg in sorted(state.registries.items()):
            lines.append(f"- **`{key}`**: {reg.name} ({len(reg.rows)} entries)")

    return "\n".join(lines)


# --- CC Spec Chapter Tools (Device Types, Role Types, CC Control) ---


async def get_device_type(
    ctx: Context,
    name: str | None = None,
) -> str:
    """Get Z-Wave Device Type definition from the application layer spec, Chapter 7.

    Includes mandatory and recommended CC requirements for each device type.

    Args:
        name: Device type name (e.g., "Thermostat", "Sensor"). Omit to list all.
    """
    return await _chapter_lookup(ctx, "device_types", "Device Types", name)


async def get_role_type(
    ctx: Context,
    name: str | None = None,
) -> str:
    """Get Z-Wave Role Type definition from the application layer spec, Chapter 8.

    Role types define network behavior: CSC, SSC, PC, RPC, PEN, AOEN, etc.

    Args:
        name: Role type name or abbreviation. Omit to list all.
    """
    return await _chapter_lookup(ctx, "role_types", "Role Types", name)


async def get_cc_interview_steps(
    ctx: Context,
    name: str | None = None,
) -> str:
    """Get CC interview/control requirements from the application layer spec, Chapter 6.

    Describes how a controller should interview devices for each CC.

    Args:
        name: CC name (e.g., "Door Lock", "Notification"). Omit to list all.
    """
    return await _chapter_lookup(ctx, "cc_control", "CC Control / Interview", name)


# --- Device Class & Header Constants Tools ---


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
    state, err = await _load(ctx, "header")
    if err:
        return err

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
    return await _supplementary_lookup(ctx, "appnote_", "Application Notes", search=search)


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
    return await _supplementary_lookup(
        ctx,
        "test_",
        "Test Specifications",
        pdf=pdf,
        search=search,
    )


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
    return await _supplementary_lookup(
        ctx,
        "legacy_",
        "Legacy Specifications",
        pdf=pdf,
        search=search,
        section=section,
    )


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
    state, err = await _load(ctx, "header_constants")
    if err:
        return err

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


async def rebuild_cache(ctx: Context) -> str:
    """Clear the spec cache and rebuild it from scratch in the background.

    Cancels any in-progress cache warming, clears all cached data, and starts
    a fresh background extraction. Useful after updating the specs repository.
    """
    lifespan_context = ctx.request_context.lifespan_context

    # Cancel current warming task if still running
    task: asyncio.Task[None] = lifespan_context["cache_build_task"]
    was_running = not task.done()
    if was_running:
        task.cancel()
        with contextlib.suppress(asyncio.CancelledError, Exception):
            await task

    old_state: AppState = lifespan_context["app_state"]
    old_state.cache.clear()

    # Fresh state — old state becomes unreachable from new tool calls
    state = AppState(config=old_state.config, cache=old_state.cache)
    lifespan_context["app_state"] = state

    async def _warm() -> None:
        try:
            await asyncio.to_thread(state.build_all)
        except Exception:
            logger.exception("Background cache warming failed")

    lifespan_context["cache_build_task"] = asyncio.create_task(_warm())
    status = "Cancelled in-progress warming, cleared" if was_running else "Cleared"
    return f"{status} cache. Rebuild started in background."


ALL_TOOLS = [
    get_cc_commands,
    get_cc_interview_steps,
    get_command_class,
    get_device_class,
    get_device_type,
    get_legacy_spec,
    get_lifeline_requirements,
    get_role_type,
    get_spec_section,
    get_test_spec,
    list_command_classes,
    list_spec_documents,
    lookup_manufacturer,
    lookup_notification,
    lookup_registry,
    lookup_sensor_type,
    lookup_zwave_constants,
    rebuild_cache,
    search_application_notes,
    search_command_classes,
]
