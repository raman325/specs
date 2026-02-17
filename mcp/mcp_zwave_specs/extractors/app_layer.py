"""Application layer spec extractor — splits the Z-Wave Application Workgroup
(AWG) specification PDF into individual Command Class sections and chapter
subsections (device types, role types, CC interview/control requirements)."""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass

from mcp_zwave_specs.extractors.pdf import PageChunk
from mcp_zwave_specs.models import CommandClassInfo, SpecSection

logger = logging.getLogger(__name__)

# CC section TOC pattern: "Alarm Command Class, version 1 [DEPRECATED]"
RE_CC_TOC = re.compile(
    r"^(.+?)\s+Command\s+Class,\s+version\s+(\d+)\s*(?:\[(\w[\w\s]*)\])?\s*$",
    re.IGNORECASE,
)

# Chapter boundaries (level-1 TOC titles → category labels)
CHAPTER_CATEGORIES: dict[str, str] = {
    "Application Command Classes": "application",
    "Management Command Classes": "management",
    "Transport-Encapsulation Command Classes": "transport",
    "Network-Protocol Command Classes": "network",
    "Command Class Control": "control",
}

# Section numbering: chapter index → section prefix
CHAPTER_SECTION_PREFIX: dict[str, str] = {
    "application": "2.2",
    "management": "3.2",
    "transport": "4.2",
    "network": "5.2",
    "control": "6",
}


@dataclass
class _TOCEntry:
    """A CC-related TOC entry with its location in the page list."""

    title: str
    cc_name: str
    version: int
    status: str
    page_number: int  # 0-indexed page number in PDF
    category: str


def _collect_cc_toc_entries(pages: list[PageChunk]) -> list[_TOCEntry]:
    """Scan TOC items across all pages to find CC section entries."""
    entries: list[_TOCEntry] = []
    current_category = ""

    # First pass: identify chapter boundaries from level-1 entries
    chapter_pages: dict[str, int] = {}
    for page in pages:
        for level, title, page_num in page.toc_items:
            if level == 1 and title in CHAPTER_CATEGORIES:
                chapter_pages[CHAPTER_CATEGORIES[title]] = page_num

    # Second pass: find CC sections (level-3 entries)
    for page in pages:
        for level, title, page_num in page.toc_items:
            # Update current category based on page position
            for cat, cat_page in sorted(chapter_pages.items(), key=lambda x: x[1]):
                if page_num >= cat_page:
                    current_category = cat

            if level != 3:
                continue

            m = RE_CC_TOC.match(title)
            if not m:
                continue

            cc_name = m.group(1).strip()
            version = int(m.group(2))
            status = m.group(3).strip() if m.group(3) else "Active"

            entries.append(
                _TOCEntry(
                    title=title,
                    cc_name=cc_name,
                    version=version,
                    status=status,
                    page_number=page_num,
                    category=current_category,
                )
            )

    logger.info("Found %d CC section TOC entries", len(entries))
    return entries


def _extract_section_text(
    pages: list[PageChunk],
    start_page: int,
    end_page: int,
) -> str:
    """Extract markdown text for pages in [start_page, end_page)."""
    parts: list[str] = []
    for page in pages:
        if page.page_number < start_page:
            continue
        if page.page_number >= end_page:
            break
        parts.append(f"\n<!-- PAGE {page.page_number + 1} -->\n")
        parts.append(page.text)
    return "\n".join(parts).strip()


def split_app_layer_sections(pages: list[PageChunk]) -> list[CommandClassInfo]:
    """Split application layer PDF pages into individual CC sections.

    Returns a list of CommandClassInfo objects, one per CC version section.
    """
    entries = _collect_cc_toc_entries(pages)
    if not entries:
        logger.warning("No CC sections found in application layer TOC")
        return []

    total_pages = len(pages)
    sections: list[CommandClassInfo] = []
    section_counter: dict[str, int] = {}  # Per-category section counter

    for i, entry in enumerate(entries):
        start_page = entry.page_number
        # End at the next entry's page within the same category
        end_page = total_pages  # fallback: rest of document
        for j in range(i + 1, len(entries)):
            if entries[j].category == entry.category:
                end_page = entries[j].page_number
                break

        content = _extract_section_text(pages, start_page, end_page)

        # Generate section number
        prefix = CHAPTER_SECTION_PREFIX.get(entry.category, "?.?")
        cat_key = entry.category
        section_counter[cat_key] = section_counter.get(cat_key, 0) + 1
        section_number = f"{prefix}.{section_counter[cat_key]}"

        sections.append(
            CommandClassInfo(
                name=entry.cc_name,
                section_number=section_number,
                versions=[entry.version],
                status=entry.status,
                page_start=start_page + 1,  # 1-indexed for display
                page_end=end_page,
                content=content,
                category=entry.category,
            )
        )

    logger.info("Split application layer spec into %d CC version sections", len(sections))
    return sections


def group_cc_versions(sections: list[CommandClassInfo]) -> dict[str, CommandClassInfo]:
    """Group versioned CC sections by base name within the same category.

    Returns a dict of CC name → merged CommandClassInfo with all versions combined.
    Control chapter sections are kept separate with a " (Control)" suffix.
    """
    grouped: dict[str, CommandClassInfo] = {}

    for section in sections:
        name = section.name
        if section.category == "control":
            name = f"{name} (Control)"
        if name not in grouped:
            grouped[name] = CommandClassInfo(
                name=name,
                section_number=section.section_number,
                versions=list(section.versions),
                status=section.status,
                page_start=section.page_start,
                page_end=section.page_end,
                content=section.content,
                category=section.category,
            )
        else:
            existing = grouped[name]
            existing.versions.extend(section.versions)
            existing.versions.sort()
            if section.page_end and (
                not existing.page_end or section.page_end > existing.page_end
            ):
                existing.page_end = section.page_end
            # Append content from newer versions
            existing.content += f"\n\n---\n\n{section.content}"
            # Use status from latest version (last wins, Active > DEPRECATED)
            if section.status == "Active":
                existing.status = "Active"

    logger.info("Grouped into %d unique command classes", len(grouped))
    return grouped


# --- Chapter Extraction (Device Types, Role Types, CC Control) ---

# Level-1 chapter titles → short keys
APP_LAYER_CHAPTERS: dict[str, str] = {
    "Device Type v2 Specification": "device_types",
    "Role Type Specification": "role_types",
    "Command Class Control": "cc_control",
}


def extract_app_layer_chapter_sections(
    pages: list[PageChunk],
    chapter_title: str,
) -> list[SpecSection]:
    """Extract subsections from a named application layer chapter.

    Finds the level-1 TOC entry matching `chapter_title`, then splits content
    by level-2 subsections within that chapter's page range.
    """
    # Find the chapter's page range from level-1 TOC
    level1_entries: list[tuple[str, int]] = []

    for page in pages:
        for level, title, page_num in page.toc_items:
            if level == 1:
                level1_entries.append((title, page_num))

    chapter_start = -1
    chapter_end = len(pages)
    for i, (title, page_num) in enumerate(level1_entries):
        if title == chapter_title:
            chapter_start = page_num
            if i + 1 < len(level1_entries):
                chapter_end = level1_entries[i + 1][1]
            break

    if chapter_start < 0:
        logger.warning("Application layer chapter '%s' not found in TOC", chapter_title)
        return []

    # Collect level-2 and level-3 entries within the chapter's page range
    sub_entries: list[tuple[str, int, int]] = []  # (title, page_num, level)
    for page in pages:
        for level, title, page_num in page.toc_items:
            if level in (2, 3) and chapter_start <= page_num < chapter_end:
                sub_entries.append((title, page_num, level))

    if not sub_entries:
        # No subsections — return the whole chapter as one section
        content = _extract_section_text(pages, chapter_start, chapter_end)
        return [
            SpecSection(
                title=chapter_title,
                content=content,
                pdf_name="app_layer",
                page_start=chapter_start + 1,
                page_end=chapter_end,
            )
        ]

    sections: list[SpecSection] = []
    for i, (title, start_page, level) in enumerate(sub_entries):
        # End at next entry at same or higher level
        end_page = chapter_end
        for j in range(i + 1, len(sub_entries)):
            if sub_entries[j][2] <= level:
                end_page = sub_entries[j][1]
                break

        content = _extract_section_text(pages, start_page, end_page)
        if not content:
            continue

        sections.append(
            SpecSection(
                title=title,
                content=content,
                pdf_name="app_layer",
                section_number=f"ch{chapter_title[0]}.{i + 1}",
                page_start=start_page + 1,
                page_end=end_page,
            )
        )

    logger.info(
        "Extracted %d sections from application layer chapter '%s'",
        len(sections),
        chapter_title,
    )
    return sections
