"""FastMCP server with Z-Wave specification tools."""

from __future__ import annotations

import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass, field
from difflib import get_close_matches

from fastmcp import Context, FastMCP

from mcp_zwave_specs.cache import CacheManager
from mcp_zwave_specs.config import DEFAULT_PATHS, Config
from mcp_zwave_specs.extractors.app_layer import (
    extract_app_layer_chapter_sections,
    group_cc_versions,
    split_app_layer_sections,
)
from mcp_zwave_specs.extractors.header import (
    DeviceClass,
    HeaderConstant,
    parse_device_classes,
    parse_header,
    parse_header_constants,
)
from mcp_zwave_specs.extractors.pdf import extract_pages
from mcp_zwave_specs.extractors.registry import parse_cc_list, parse_registries
from mcp_zwave_specs.extractors.supplementary import extract_supplementary
from mcp_zwave_specs.models import (
    CCHeaderData,
    CommandClassInfo,
    RegistryData,
    SpecSection,
)
from mcp_zwave_specs.search import SearchIndex

logger = logging.getLogger(__name__)

CLONE_INSTRUCTIONS = (
    "The zwave-js/specs repository is required but was not found.\n"
    "Clone it with:\n"
    "  git clone https://github.com/zwave-js/specs.git\n"
    "Then start the server with:\n"
    "  zwave-specs-mcp --specs-dir /path/to/specs"
)


@dataclass
class AppState:
    """Lazily-loaded application state."""

    config: Config
    cache: CacheManager

    # Loaded on demand
    cc_sections: dict[str, CommandClassInfo] = field(default_factory=dict)
    header_data: dict[str, CCHeaderData] = field(default_factory=dict)
    registries: dict[str, RegistryData] = field(default_factory=dict)
    supplementary: dict[str, list[SpecSection]] = field(default_factory=dict)
    search_index: SearchIndex = field(default_factory=SearchIndex)

    # CC spec chapter sections (device types, role types, cc control)
    app_layer_chapters: dict[str, list[SpecSection]] = field(default_factory=dict)
    # Device classes from ZW_classcmd.h
    device_classes: list[DeviceClass] = field(default_factory=list)
    # Constants from all header files (keyed by header filename)
    header_constants: dict[str, list[HeaderConstant]] = field(default_factory=dict)

    _app_layer_loaded: bool = False
    _header_loaded: bool = False
    _registries_loaded: bool = False
    _supplementary_loaded: bool = False
    _app_layer_chapters_loaded: bool = False
    _header_constants_loaded: bool = False

    def _ensure_app_layer(self) -> None:
        """Load CC sections from cache or extract from RST source / PDF."""
        if self._app_layer_loaded:
            return
        self._app_layer_loaded = True

        if not self.config.specs_available and not self.config.app_layer_rst_available:
            return

        # Try cache first
        if self.cache.is_valid() and self.cache.has_category("app_layer"):
            cached = self.cache.read_json("app_layer_sections.json")
            if cached:
                for name, data in cached.items():
                    self.cc_sections[name] = CommandClassInfo(**data)
                    # Load section content from individual files
                    content = self.cache.read_text(
                        f"app_layer_sections/{name.replace('/', '_')}.md"
                    )
                    if content:
                        self.cc_sections[name].content = content
                self._build_search_index()
                logger.info("Loaded %d CC sections from cache", len(self.cc_sections))
                return

        # Extract from RST source or PDF
        if self.config.app_layer_rst_available:
            from mcp_zwave_specs.extractors.app_layer_rst import (
                split_app_layer_sections_rst,
            )

            logger.info("Extracting CC sections from RST source...")
            sections = split_app_layer_sections_rst(self.config.app_layer_rst_dir)
        else:
            logger.info(
                "Extracting CC sections from application layer PDF (this may take a moment)..."
            )
            pages = extract_pages(self.config.app_layer_pdf)
            sections = split_app_layer_sections(pages)
        self.cc_sections = group_cc_versions(sections)

        # Merge CC IDs from header data
        self._ensure_header()
        for name, cc in self.cc_sections.items():
            base_name = name.removesuffix(" (Control)")
            if base_name in self.header_data:
                cc.cc_id = self.header_data[base_name].cc_id

        # Cache results
        self.cache.ensure_dirs()
        index_data = {}
        for name, cc in self.cc_sections.items():
            safe_name = name.replace("/", "_")
            self.cache.write_text(f"app_layer_sections/{safe_name}.md", cc.content)
            index_data[name] = {
                "name": cc.name,
                "section_number": cc.section_number,
                "cc_id": cc.cc_id,
                "versions": cc.versions,
                "status": cc.status,
                "page_start": cc.page_start,
                "page_end": cc.page_end,
                "content": "",  # stored separately
                "category": cc.category,
            }
        self.cache.write_json("app_layer_sections.json", index_data)
        self.cache.mark_category("app_layer")
        self.cache.mark_valid()

        self._build_search_index()
        logger.info("Extracted and cached %d CC sections", len(self.cc_sections))

    def _build_search_index(self) -> None:
        """Rebuild the full-text search index from loaded CC sections."""
        self.search_index = SearchIndex()
        for name, cc in self.cc_sections.items():
            self.search_index.add(name, name, cc.content)

    def _ensure_header(self) -> None:
        """Load CC header data and device classes from cache or ZW_classcmd.h."""
        if self._header_loaded:
            return
        self._header_loaded = True

        if not self.config.specs_available:
            return

        if self.cache.is_valid() and self.cache.has_category("header"):
            cached = self.cache.read_json("header_data.json")
            if cached:
                from mcp_zwave_specs.models import CCCommand, StructDef, StructField

                for name, data in cached.items():
                    commands = [CCCommand(**c) for c in data.get("commands", [])]
                    structs = [
                        StructDef(
                            name=s["name"],
                            fields=[StructField(**f) for f in s.get("fields", [])],
                        )
                        for s in data.get("structs", [])
                    ]
                    self.header_data[name] = CCHeaderData(
                        name=name,
                        cc_id=data["cc_id"],
                        commands=commands,
                        structs=structs,
                    )
                # Load device classes
                dc_cached = self.cache.read_json("device_classes.json")
                if dc_cached:
                    self.device_classes = [
                        DeviceClass(
                            generic_name=d["generic_name"],
                            generic_id=d["generic_id"],
                            comment=d.get("comment", ""),
                            specific_types=[tuple(s) for s in d.get("specific_types", [])],
                        )
                        for d in dc_cached
                    ]
                logger.info("Loaded %d CC header entries from cache", len(self.header_data))
                return

        self.header_data = parse_header(self.config.header_file)
        self.device_classes = parse_device_classes(self.config.header_file)

        # Cache
        cache_data = {}
        for name, hd in self.header_data.items():
            cache_data[name] = {
                "cc_id": hd.cc_id,
                "commands": [
                    {"name": c.name, "opcode": c.opcode, "cc_name": c.cc_name, "cc_id": c.cc_id}
                    for c in hd.commands
                ],
                "structs": [
                    {
                        "name": s.name,
                        "fields": [
                            {"name": f.name, "type": f.type, "bits": f.bits} for f in s.fields
                        ],
                    }
                    for s in hd.structs
                ],
            }
        self.cache.write_json("header_data.json", cache_data)
        # Cache device classes
        self.cache.write_json(
            "device_classes.json",
            [
                {
                    "generic_name": dc.generic_name,
                    "generic_id": dc.generic_id,
                    "comment": dc.comment,
                    "specific_types": list(dc.specific_types),
                }
                for dc in self.device_classes
            ],
        )
        self.cache.mark_category("header")
        self.cache.mark_valid()

    def _ensure_registries(self) -> None:
        """Load registry data from cache or parse Excel files."""
        if self._registries_loaded:
            return
        self._registries_loaded = True

        if not self.config.specs_available:
            return

        if self.cache.is_valid() and self.cache.has_category("registries"):
            cached_keys = self.cache.read_json("registries/index.json")
            if cached_keys:
                for key in cached_keys:
                    data = self.cache.read_json(f"registries/{key}.json")
                    if data:
                        self.registries[key] = RegistryData(**data)
                logger.info("Loaded %d registries from cache", len(self.registries))
                return

        self.registries = parse_registries(self.config.registries_dir)
        cc_data = parse_cc_list(self.config.cc_list_xlsx)
        self.registries.update(cc_data)

        # Cache
        keys = list(self.registries.keys())
        self.cache.write_json("registries/index.json", keys)
        for key, reg in self.registries.items():
            self.cache.write_json(
                f"registries/{key}.json",
                {
                    "name": reg.name,
                    "filename": reg.filename,
                    "rows": reg.rows,
                    "columns": reg.columns,
                },
            )
        self.cache.mark_category("registries")
        self.cache.mark_valid()

    def _ensure_supplementary(self) -> None:
        """Load supplementary PDF sections from cache or extract from PDFs."""
        if self._supplementary_loaded:
            return
        self._supplementary_loaded = True

        if not self.config.specs_available:
            return

        if self.cache.is_valid() and self.cache.has_category("supplementary"):
            cached_keys = self.cache.read_json("supplementary/index.json")
            if cached_keys:
                for key in cached_keys:
                    sections_data = self.cache.read_json(f"supplementary/{key}.json")
                    if sections_data:
                        self.supplementary[key] = [SpecSection(**s) for s in sections_data]
                logger.info(
                    "Loaded %d supplementary PDFs from cache",
                    len(self.supplementary),
                )
                return

        self.supplementary = extract_supplementary(self.config)

        # Cache
        keys = list(self.supplementary.keys())
        self.cache.write_json("supplementary/index.json", keys)
        for key, sections in self.supplementary.items():
            self.cache.write_json(
                f"supplementary/{key}.json",
                [
                    {
                        "title": s.title,
                        "content": s.content,
                        "pdf_name": s.pdf_name,
                        "section_number": s.section_number,
                        "page_start": s.page_start,
                        "page_end": s.page_end,
                    }
                    for s in sections
                ],
            )
        self.cache.mark_category("supplementary")
        self.cache.mark_valid()

    def _ensure_app_layer_chapters(self) -> None:
        """Load application layer chapter sections from cache, RST source, or PDF."""
        if self._app_layer_chapters_loaded:
            return
        self._app_layer_chapters_loaded = True

        if not self.config.specs_available and not self.config.app_layer_rst_available:
            return

        if self.cache.is_valid() and self.cache.has_category("app_layer_chapters"):
            cached_keys = self.cache.read_json("app_layer_chapters/index.json")
            if cached_keys:
                for key in cached_keys:
                    data = self.cache.read_json(f"app_layer_chapters/{key}.json")
                    if data:
                        self.app_layer_chapters[key] = [SpecSection(**s) for s in data]
                logger.info(
                    "Loaded %d CC spec chapter groups from cache", len(self.app_layer_chapters)
                )
                return

        # Extract from RST source or PDF
        if self.config.app_layer_rst_available:
            from mcp_zwave_specs.extractors.app_layer_rst import (
                extract_app_layer_chapter_sections_rst,
            )

            logger.info("Extracting chapter sections from RST source...")
            self.app_layer_chapters = extract_app_layer_chapter_sections_rst(
                self.config.app_layer_rst_dir
            )
        else:
            from mcp_zwave_specs.extractors.app_layer import APP_LAYER_CHAPTERS

            logger.info("Extracting application layer chapter sections...")
            pages = extract_pages(self.config.app_layer_pdf)
            for chapter_title, key in APP_LAYER_CHAPTERS.items():
                sections = extract_app_layer_chapter_sections(pages, chapter_title)
                if sections:
                    self.app_layer_chapters[key] = sections

        # Cache
        keys = list(self.app_layer_chapters.keys())
        self.cache.write_json("app_layer_chapters/index.json", keys)
        for key, sections in self.app_layer_chapters.items():
            self.cache.write_json(
                f"app_layer_chapters/{key}.json",
                [
                    {
                        "title": s.title,
                        "content": s.content,
                        "pdf_name": s.pdf_name,
                        "section_number": s.section_number,
                        "page_start": s.page_start,
                        "page_end": s.page_end,
                    }
                    for s in sections
                ],
            )
        self.cache.mark_category("app_layer_chapters")
        self.cache.mark_valid()
        logger.info("Extracted %d CC spec chapter groups", len(self.app_layer_chapters))

    def _ensure_header_constants(self) -> None:
        """Load header constants from cache or parse .h files."""
        if self._header_constants_loaded:
            return
        self._header_constants_loaded = True

        if not self.config.specs_available:
            return

        if self.cache.is_valid() and self.cache.has_category("header_constants"):
            cached = self.cache.read_json("header_constants.json")
            if cached:
                for fname, items in cached.items():
                    self.header_constants[fname] = [HeaderConstant(**c) for c in items]
                logger.info(
                    "Loaded constants from %d header files from cache",
                    len(self.header_constants),
                )
                return

        # Parse all .h files in API_includes (except ZW_classcmd.h which is huge)
        api_dir = self.config.api_includes_dir
        if not api_dir.is_dir():
            return
        for h_file in sorted(api_dir.glob("*.h")):
            if h_file.name == "ZW_classcmd.h":
                continue  # handled separately by _ensure_header
            constants = parse_header_constants(h_file)
            if constants:
                self.header_constants[h_file.name] = constants

        # Cache
        cache_data = {
            fname: [{"name": c.name, "value": c.value, "comment": c.comment} for c in consts]
            for fname, consts in self.header_constants.items()
        }
        self.cache.write_json("header_constants.json", cache_data)
        self.cache.mark_category("header_constants")
        self.cache.mark_valid()

    def find_cc(self, name: str | None, cc_id: int | None) -> CommandClassInfo | None:
        """Find a CC by name or ID, with fuzzy matching."""
        self._ensure_app_layer()

        if cc_id is not None:
            for cc in self.cc_sections.values():
                if cc.cc_id == cc_id:
                    return cc
            return None

        if name is None:
            return None

        # Exact match
        if name in self.cc_sections:
            return self.cc_sections[name]

        # Case-insensitive match
        lower_map = {k.lower(): k for k in self.cc_sections}
        if name.lower() in lower_map:
            return self.cc_sections[lower_map[name.lower()]]

        # Fuzzy match
        matches = get_close_matches(name.lower(), lower_map.keys(), n=1, cutoff=0.6)
        if matches:
            return self.cc_sections[lower_map[matches[0]]]

        return None

    def suggest_cc_names(self, name: str) -> list[str]:
        """Return close CC name matches for error messages."""
        self._ensure_app_layer()
        lower_map = {k.lower(): k for k in self.cc_sections}
        matches = get_close_matches(name.lower(), lower_map.keys(), n=5, cutoff=0.4)
        return [lower_map[m] for m in matches]


def _format_cc_header(cc: CommandClassInfo, config: Config) -> str:
    """Format the header block for a CC response."""
    lines = [f"# {cc.name} Command Class, {cc.version_str}"]
    lines.append(f"- **CC ID**: {cc.id_hex}")
    lines.append(f"- **Versions**: {', '.join(str(v) for v in cc.versions)}")
    if cc.page_start is not None and cc.page_end is not None:
        lines.append(f"- **Section**: {cc.section_number} (pages {cc.page_start}-{cc.page_end})")
    else:
        lines.append(f"- **Section**: {cc.section_number}")
    if config.app_layer_rst_available:
        lines.append("- **Source**: RST source")
    else:
        source_path = config.path_overrides.get("app_layer_pdf", DEFAULT_PATHS["app_layer_pdf"])
        lines.append(f"- **Source**: {config.github_url(source_path)}")
    lines.append(f"- **Status**: {cc.status}")
    return "\n".join(lines)


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
        if not state.config.specs_available:
            return CLONE_INSTRUCTIONS

        state._ensure_app_layer()
        state._ensure_header()

        lines = ["# Z-Wave Command Classes\n"]
        lines.append("| CC Name | CC ID | Versions | Status | Category |")
        lines.append("|---------|-------|----------|--------|----------|")

        for name in sorted(state.cc_sections):
            cc = state.cc_sections[name]
            if category and cc.category != category:
                continue
            if not include_deprecated and cc.status in ("DEPRECATED", "OBSOLETED"):
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
        if not state.config.specs_available:
            return CLONE_INSTRUCTIONS

        cc = state.find_cc(name, cc_id)
        if cc is None:
            search_term = name or (f"0x{cc_id:02X}" if cc_id else "unknown")
            suggestions = state.suggest_cc_names(search_term) if name else []
            msg = f"Command Class '{search_term}' not found."
            if suggestions:
                msg += f"\n\nDid you mean: {', '.join(suggestions)}?"
            return msg

        header = _format_cc_header(cc, state.config)
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
        if not state.config.specs_available:
            return CLONE_INSTRUCTIONS

        state._ensure_app_layer()

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

        state._ensure_header()

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

        state._ensure_registries()
        reg = state.registries.get("notification_types")
        if not reg:
            return "Notification registry not available."

        return _format_registry_search(reg, search, ["Notification Type", "col_1"])

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

        state._ensure_registries()
        reg = state.registries.get("sensor_types")
        if not reg:
            return "Sensor type registry not available."

        return _format_registry_search(reg, sensor_type)

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

        state._ensure_registries()
        reg = state.registries.get("manufacturers")
        if not reg:
            return "Manufacturer registry not available."

        search = name or manufacturer_id
        return _format_registry_search(reg, search, ["Customer", "ID"])

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

        state._ensure_registries()
        reg = state.registries.get(registry)
        if not reg:
            available = ", ".join(sorted(state.registries.keys()))
            return f"Registry '{registry}' not found. Available: {available}"

        return _format_registry_search(reg, search)

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

        state._ensure_registries()
        reg = state.registries.get("lifeline_association_commands")
        if not reg:
            return "Lifeline association registry not available."

        if command_class:
            return _format_registry_search(reg, command_class, ["Command Class"])
        return _format_registry_search(reg, None)

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

        state._ensure_supplementary()
        sections = state.supplementary.get(pdf)
        if not sections:
            available = ", ".join(sorted(state.supplementary.keys()))
            return f"PDF '{pdf}' not found. Available: {available}"

        if section:
            for s in sections:
                if section.lower() in s.title.lower() or s.section_number == section:
                    return (
                        f"# {s.title}\n"
                        f"- Source: {pdf}\n"
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
                    f"- Source: {pdf}\n"
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
        state._ensure_app_layer_chapters()
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
        state._ensure_supplementary()
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
        state._ensure_registries()
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
        if not state.config.specs_available:
            return CLONE_INSTRUCTIONS

        state._ensure_app_layer_chapters()
        return _search_app_layer_chapter(state, "device_types", "Device Types", name)

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
        if not state.config.specs_available:
            return CLONE_INSTRUCTIONS

        state._ensure_app_layer_chapters()
        return _search_app_layer_chapter(state, "role_types", "Role Types", name)

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
        if not state.config.specs_available:
            return CLONE_INSTRUCTIONS

        state._ensure_app_layer_chapters()
        return _search_app_layer_chapter(state, "cc_control", "CC Control / Interview", name)

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

        state._ensure_header()

        if not state.device_classes:
            return "No device class data found."

        # Filter by generic_id
        if generic_id is not None:
            for dc in state.device_classes:
                if dc.generic_id == generic_id:
                    return _format_device_class(dc)
            return f"No generic device class with ID 0x{generic_id:02X}."

        # Search by generic name
        if generic:
            gl = generic.lower()
            for dc in state.device_classes:
                if gl in dc.generic_name.lower() or gl in dc.comment.lower():
                    return _format_device_class(dc)
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

        state._ensure_supplementary()

        # Filter to app note keys
        app_notes = {k: v for k, v in state.supplementary.items() if k.startswith("appnote_")}
        if not app_notes:
            return "No application notes found."

        if search is None:
            lines = ["# Z-Wave Application Notes\n"]
            for key, sections in sorted(app_notes.items()):
                display = key.removeprefix("appnote_").replace("_", " ").title()
                lines.append(f"- **`{key}`**: {display} ({len(sections)} sections)")
            lines.append("\nUse `get_spec_section(pdf=key)` to read a specific note.")
            return "\n".join(lines)

        # Search across all app notes
        search_lower = search.lower()
        results: list[tuple[str, SpecSection, int]] = []
        for key, sections in app_notes.items():
            for s in sections:
                count = s.content.lower().count(search_lower)
                title_match = search_lower in s.title.lower()
                if count > 0 or title_match:
                    results.append((key, s, count + (100 if title_match else 0)))

        results.sort(key=lambda x: x[2], reverse=True)
        if not results:
            return f"No results for '{search}' in application notes."

        lines = [f"# Application Note Results for '{search}'\n"]
        for key, s, _score in results[:10]:
            lines.append(f"## {s.title}")
            lines.append(f"- Source: `{key}` (pages {s.page_start}-{s.page_end})")
            preview = s.content[:200].replace("\n", " ")
            lines.append(f"- {preview}...\n")

        if len(results) > 10:
            lines.append(f"*...{len(results) - 10} more results*")
        return "\n".join(lines)

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

        state._ensure_supplementary()
        return _search_supplementary_group(state, "test_", "Test Specifications", pdf, search)

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

        state._ensure_supplementary()
        return _search_supplementary_group(
            state, "legacy_", "Legacy Specifications", pdf, search, section
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

        state._ensure_header_constants()
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


def _search_app_layer_chapter(
    state: AppState,
    chapter_key: str,
    display_name: str,
    search: str | None,
) -> str:
    """Search or list sections within a CC spec chapter."""
    sections = state.app_layer_chapters.get(chapter_key, [])
    if not sections:
        return f"No {display_name} sections found."

    if search is None:
        # Return TOC
        lines = [f"# {display_name}\n"]
        for s in sections:
            lines.append(f"- **{s.title}** (pages {s.page_start}-{s.page_end})")
        return "\n".join(lines)

    # Search by title (case-insensitive, partial match)
    search_lower = search.lower()
    matches = [s for s in sections if search_lower in s.title.lower()]

    if not matches:
        # Fall back to content search
        matches = [s for s in sections if search_lower in s.content.lower()]

    if not matches:
        titles = [f"  - {s.title}" for s in sections]
        return f"No match for '{search}' in {display_name}.\nAvailable sections:\n" + "\n".join(
            titles
        )

    if len(matches) == 1:
        s = matches[0]
        return (
            f"# {s.title}\n"
            f"- Source: Application Layer V5.0, {display_name}\n"
            f"- Pages: {s.page_start}-{s.page_end}\n\n"
            f"---\n\n{s.content}"
        )

    # Multiple matches — return summaries
    lines = [f"# {display_name} — matches for '{search}'\n"]
    for s in matches:
        lines.append(f"## {s.title} (pages {s.page_start}-{s.page_end})")
        # Show first 200 chars as preview
        preview = s.content[:200].replace("\n", " ")
        lines.append(f"{preview}...\n")
    return "\n".join(lines)


def _search_supplementary_group(
    state: AppState,
    prefix: str,
    display_name: str,
    pdf: str | None,
    search: str | None,
    section: str | None = None,
) -> str:
    """Search or list supplementary PDFs matching a key prefix."""
    group = {k: v for k, v in state.supplementary.items() if k.startswith(prefix)}
    if not group:
        return f"No {display_name} found."

    if pdf is None and search is None:
        # List available specs in this group
        lines = [f"# {display_name}\n"]
        for key, sections in sorted(group.items()):
            lines.append(f"- **`{key}`**: {len(sections)} sections")
        return "\n".join(lines)

    if pdf:
        # Look up specific PDF
        sections = group.get(pdf)
        if not sections:
            # Try with prefix
            full_key = pdf if pdf.startswith(prefix) else f"{prefix}{pdf}"
            sections = group.get(full_key)
        if not sections:
            available = ", ".join(sorted(group))
            return f"Spec '{pdf}' not found. Available: {available}"

        if section:
            for s in sections:
                if section.lower() in s.title.lower():
                    return (
                        f"# {s.title}\n"
                        f"- Source: `{pdf}`\n"
                        f"- Pages: {s.page_start}-{s.page_end}\n\n"
                        f"---\n\n{s.content}"
                    )
            titles = [f"  - {s.title}" for s in sections]
            return f"Section '{section}' not found.\nAvailable:\n" + "\n".join(titles)

        if search:
            sl = search.lower()
            best = max(sections, key=lambda s: s.content.lower().count(sl))
            count = best.content.lower().count(sl)
            if count > 0:
                return (
                    f"# {best.title}\n"
                    f"- Source: `{pdf}`\n"
                    f"- Pages: {best.page_start}-{best.page_end}\n"
                    f"- Matches: {count}\n\n"
                    f"---\n\n{best.content}"
                )
            return f"No results for '{search}' in {pdf}."

        # No filter — show TOC
        lines = [f"# {pdf} — Sections\n"]
        for s in sections:
            lines.append(f"- **{s.title}** (pages {s.page_start}-{s.page_end})")
        return "\n".join(lines)

    # Search across all specs in group (search without pdf)
    if search:
        sl = search.lower()
        results: list[tuple[str, SpecSection, int]] = []
        for key, sections in group.items():
            for s in sections:
                count = s.content.lower().count(sl)
                title_match = sl in s.title.lower()
                if count > 0 or title_match:
                    results.append((key, s, count + (100 if title_match else 0)))
        results.sort(key=lambda x: x[2], reverse=True)
        if not results:
            return f"No results for '{search}' in {display_name}."
        lines = [f"# {display_name} — results for '{search}'\n"]
        for key, s, _score in results[:10]:
            lines.append(f"## {s.title}")
            lines.append(f"- Source: `{key}` (pages {s.page_start}-{s.page_end})")
            preview = s.content[:200].replace("\n", " ")
            lines.append(f"- {preview}...\n")
        return "\n".join(lines)

    return f"Provide 'pdf' or 'search' to query {display_name}."


def _format_device_class(dc: DeviceClass) -> str:
    """Format a single device class with its specific types."""
    lines = [f"# {dc.generic_name} (0x{dc.generic_id:02X})"]
    if dc.comment:
        lines.append(f"- **Description**: {dc.comment}")
    lines.append("- **Source**: ZW_classcmd.h\n")

    if dc.specific_types:
        lines.append("## Specific Types\n")
        lines.append("| Specific Type | ID | Description |")
        lines.append("|--------------|-----|-------------|")
        for name, sid, comment in dc.specific_types:
            lines.append(f"| {name} | 0x{sid:02X} | {comment} |")
    else:
        lines.append("*No specific types defined.*")

    return "\n".join(lines)


def _format_registry_search(
    reg: RegistryData,
    search: str | None = None,
    search_columns: list[str] | None = None,
) -> str:
    """Format registry data as markdown, optionally filtered by search."""
    rows = reg.rows
    if search:
        search_lower = search.lower()
        cols = search_columns or reg.columns
        rows = [
            row
            for row in reg.rows
            if any(search_lower in str(row.get(col, "")).lower() for col in cols)
        ]
        if not rows:
            # Fall back to searching all columns
            rows = [
                row
                for row in reg.rows
                if any(search_lower in str(v).lower() for v in row.values())
            ]

    if not rows:
        return f"No results found in {reg.name}."

    # Limit output size
    truncated = len(rows) > 50
    display_rows = rows[:50]

    lines = [f"# {reg.name}\n"]
    if search:
        lines.append(f"*Filtered by: '{search}' — {len(rows)} results*\n")

    # Build markdown table
    cols = reg.columns or (list(display_rows[0].keys()) if display_rows else [])
    lines.append("| " + " | ".join(cols) + " |")
    lines.append("| " + " | ".join("---" for _ in cols) + " |")

    for row in display_rows:
        values = [str(row.get(c, "")).replace("\n", " ")[:80] for c in cols]
        lines.append("| " + " | ".join(values) + " |")

    if truncated:
        lines.append(f"\n*...{len(rows) - 50} more rows not shown*")

    return "\n".join(lines)


# Module-level instance for `fastmcp dev` and `fastmcp run`
mcp = create_server(Config.from_env())
