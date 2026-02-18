"""Markdown formatting helpers for MCP tool responses."""

from __future__ import annotations

from pathlib import Path

from mcp_zwave_specs.config import DEFAULT_PATHS, Config
from mcp_zwave_specs.extractors.header import DeviceClass
from mcp_zwave_specs.models import CommandClassInfo, RegistryData, SpecSection


def format_cc_header(cc: CommandClassInfo, config: Config) -> str:
    """Format the header block for a CC response."""
    lines = [f"# {cc.name} Command Class, {cc.version_str}"]
    lines.append(f"- **CC ID**: {cc.id_hex}")
    lines.append(f"- **Versions**: {', '.join(str(v) for v in cc.versions)}")
    if cc.page_start is not None and cc.page_end is not None:
        lines.append(f"- **Section**: {cc.section_number} (pages {cc.page_start}-{cc.page_end})")
    else:
        lines.append(f"- **Section**: {cc.section_number}")
    if config.app_layer_rst_available:
        lines.append("- **Source**: RST")
        lines.append(f"- **File**: {config.app_layer_rst_dir}")
    else:
        source_path = config.path_overrides.get("app_layer_pdf", DEFAULT_PATHS["app_layer_pdf"])
        pdf = config.specs_dir / source_path
        lines.append("- **Source**: PDF")
        lines.append(f"- **File**: {pdf}")
        lines.append(f"- **GitHub**: {config.github_url(source_path)}")
    lines.append(f"- **Status**: {cc.status}")
    return "\n".join(lines)


def format_pdf_source(pdf_key: str, pdf_path: Path | None, config: Config) -> str:
    """Format source lines for a supplementary PDF, showing path and GitHub link."""
    if pdf_path is None:
        return f"`{pdf_key}`"
    rel = (
        pdf_path.relative_to(config.specs_dir)
        if pdf_path.is_relative_to(config.specs_dir)
        else pdf_path
    )
    github = config.github_url(str(rel))
    return f"`{pdf_key}`\n- **File**: {pdf_path}\n- **GitHub**: {github}"


def format_app_layer_source(config: Config, display_name: str) -> str:
    """Format the source lines for application layer chapter responses."""
    if config.app_layer_rst_available:
        return f"RST, {display_name}\n- **File**: {config.app_layer_rst_dir}"
    source_path = config.path_overrides.get("app_layer_pdf", DEFAULT_PATHS["app_layer_pdf"])
    pdf = config.specs_dir / source_path
    return (
        f"PDF, {display_name}\n- **File**: {pdf}\n- **GitHub**: {config.github_url(source_path)}"
    )


def search_app_layer_chapter(
    sections: list[SpecSection],
    config: Config,
    display_name: str,
    search: str | None,
) -> str:
    """Search or list sections within a CC spec chapter."""
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

    source = format_app_layer_source(config, display_name)
    if len(matches) == 1:
        s = matches[0]
        return (
            f"# {s.title}\n"
            f"- Source: {source}\n"
            f"- Pages: {s.page_start}-{s.page_end}\n\n"
            f"---\n\n{s.content}"
        )

    # Multiple matches — return summaries
    lines = [f"# {display_name} — matches for '{search}'\n"]
    for s in matches:
        lines.append(f"## {s.title} (pages {s.page_start}-{s.page_end})")
        preview = s.content[:200].replace("\n", " ")
        lines.append(f"{preview}...\n")
    return "\n".join(lines)


def search_supplementary_group(
    supplementary: dict[str, list[SpecSection]],
    supplementary_paths: dict[str, Path],
    config: Config,
    prefix: str,
    display_name: str,
    pdf: str | None,
    search: str | None,
    section: str | None = None,
) -> str:
    """Search or list supplementary PDFs matching a key prefix."""
    group = {k: v for k, v in supplementary.items() if k.startswith(prefix)}
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
            full_key = pdf if pdf.startswith(prefix) else f"{prefix}{pdf}"
            sections = group.get(full_key)
        if not sections:
            available = ", ".join(sorted(group))
            return f"Spec '{pdf}' not found. Available: {available}"

        source = format_pdf_source(pdf, supplementary_paths.get(pdf), config)
        if section:
            for s in sections:
                if section.lower() in s.title.lower():
                    return (
                        f"# {s.title}\n"
                        f"- Source: {source}\n"
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
                    f"- Source: {source}\n"
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


def format_device_class(dc: DeviceClass) -> str:
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


def format_registry_search(
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
