"""Application layer RST source extractor — reads pre-split RST/Sphinx source
files as an alternative to PDF extraction.

Expects the ``source/`` directory of a Sphinx project with this layout::

    source/
      application_command_classes/
        command_class_definitions.rst      # toctree listing CC RST files
        command_class_definitions/
          door_lock_command_class_version_4.rst
          ...
      management_command_classes/           # same structure
      transport_encapsulation_command_classes/
      network_protocol_command_classes/
      command_class_control/               # chapter with inline sections
      device_type_v2/                      # chapter
      role_type/                           # chapter
"""

from __future__ import annotations

import logging
import re
from pathlib import Path

from mcp_zwave_specs.models import CommandClassInfo, SpecSection

logger = logging.getLogger(__name__)

# Category directory names → category labels (same values as app_layer.py)
RST_CATEGORIES: dict[str, str] = {
    "application_command_classes": "application",
    "management_command_classes": "management",
    "transport_encapsulation_command_classes": "transport",
    "network_protocol_command_classes": "network",
}

# Section numbering prefixes (same as app_layer.py)
CHAPTER_SECTION_PREFIX: dict[str, str] = {
    "application": "2.2",
    "management": "3.2",
    "transport": "4.2",
    "network": "5.2",
}

# Chapter directories → keys used by the server
RST_CHAPTERS: dict[str, str] = {
    "command_class_control": "cc_control",
    "device_type_v2": "device_types",
    "role_type": "role_types",
}

# Toctree entry: "  Title <path.rst>"
RE_TOCTREE_ENTRY = re.compile(r"^\s+(.+?)\s+<(.+?)>\s*$")

# CC title: "Door Lock Command Class, version 4" or "version 1-2 [DEPRECATED]"
RE_CC_RST = re.compile(
    r"^(.+?)\s+Command\s+Class,\s+version\s+(\d+)(?:-(\d+))?\s*(?:\[(\w[\w\s]*)\])?\s*$",
    re.IGNORECASE,
)


def _parse_toctree(rst_path: Path) -> list[tuple[str, Path]]:
    """Parse toctree entries from an RST file, returning (title, resolved_path) pairs."""
    if not rst_path.exists():
        return []

    text = rst_path.read_text(encoding="utf-8", errors="replace")
    parent = rst_path.parent
    entries: list[tuple[str, Path]] = []

    in_toctree = False
    for line in text.splitlines():
        if ".. toctree::" in line:
            in_toctree = True
            continue
        if in_toctree:
            # Toctree options (indented lines starting with :)
            stripped = line.strip()
            if stripped.startswith(":") or stripped == "":
                continue
            # Check for toctree entry
            m = RE_TOCTREE_ENTRY.match(line)
            if m:
                title = m.group(1)
                rel_path = m.group(2)
                if not rel_path.endswith(".rst"):
                    rel_path += ".rst"
                entries.append((title, (parent / rel_path).resolve()))
            elif stripped and not stripped.startswith(".."):
                # End of toctree block (non-empty, non-directive line)
                in_toctree = False

    return entries


def split_app_layer_sections_rst(rst_dir: Path) -> list[CommandClassInfo]:
    """Extract CC sections from RST source tree.

    Walks category directories, parses toctree entries from
    ``command_class_definitions.rst``, and reads individual CC RST files.

    Returns a flat list of CommandClassInfo (one per toctree entry).
    Use ``group_cc_versions()`` from ``app_layer.py`` to merge versions.
    """
    sections: list[CommandClassInfo] = []

    for dir_name, category in RST_CATEGORIES.items():
        defs_rst = rst_dir / dir_name / "command_class_definitions.rst"
        entries = _parse_toctree(defs_rst)
        if not entries:
            logger.warning("No toctree entries found in %s", defs_rst)
            continue

        prefix = CHAPTER_SECTION_PREFIX[category]
        counter = 0

        for title, rst_path in entries:
            m = RE_CC_RST.match(title)
            if not m:
                logger.debug("Skipping non-CC toctree entry: %s", title)
                continue

            cc_name = m.group(1).strip()
            version_start = int(m.group(2))
            version_end = int(m.group(3)) if m.group(3) else version_start
            status = m.group(4).strip().upper() if m.group(4) else "Active"
            versions = list(range(version_start, version_end + 1))

            if not rst_path.exists():
                logger.warning("CC RST file not found: %s", rst_path)
                continue

            content = rst_path.read_text(encoding="utf-8", errors="replace")
            counter += 1

            sections.append(
                CommandClassInfo(
                    name=cc_name,
                    section_number=f"{prefix}.{counter}",
                    versions=versions,
                    status=status,
                    content=content,
                    category=category,
                )
            )

        logger.info(
            "Extracted %d CC entries from %s (%s)",
            counter,
            dir_name,
            category,
        )

    logger.info("Total CC sections from RST: %d", len(sections))
    return sections


def extract_app_layer_chapter_sections_rst(
    rst_dir: Path,
) -> dict[str, list[SpecSection]]:
    """Extract chapter sections (device types, role types, CC control) from RST source.

    Returns a dict of chapter_key → list of SpecSection, matching the
    structure produced by ``extract_app_layer_chapter_sections()`` for PDFs.
    """
    result: dict[str, list[SpecSection]] = {}

    for dir_name, key in RST_CHAPTERS.items():
        chapter_dir = rst_dir / dir_name
        if not chapter_dir.is_dir():
            logger.warning("Chapter directory not found: %s", chapter_dir)
            continue

        index_rst = chapter_dir / "index.rst"
        entries = _parse_toctree(index_rst)
        if not entries:
            logger.warning("No toctree entries in %s", index_rst)
            continue

        sections: list[SpecSection] = []
        for i, (title, rst_path) in enumerate(entries):
            if not rst_path.exists():
                logger.warning("Chapter RST file not found: %s", rst_path)
                continue

            content = rst_path.read_text(encoding="utf-8", errors="replace")
            # Follow nested toctrees to include sub-files
            content = _expand_toctree_content(rst_path, content)

            sections.append(
                SpecSection(
                    title=title,
                    content=content,
                    pdf_name="app_layer",
                    section_number=f"{key}.{i + 1}",
                )
            )

        if sections:
            result[key] = sections
            logger.info("Extracted %d sections for chapter '%s'", len(sections), key)

    return result


def _expand_toctree_content(rst_path: Path, content: str) -> str:
    """If an RST file has a toctree, append the content of referenced files."""
    sub_entries = _parse_toctree(rst_path)
    if not sub_entries:
        return content

    parts = [content]
    for _title, sub_path in sub_entries:
        if not sub_path.exists():
            continue
        sub_content = sub_path.read_text(encoding="utf-8", errors="replace")
        parts.append(f"\n\n{sub_content}")

    return "\n".join(parts)
