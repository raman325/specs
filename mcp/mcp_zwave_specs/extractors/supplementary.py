"""Extract supplementary (non-CC/application layer) spec PDFs by chapter headings."""

from __future__ import annotations

import logging
from pathlib import Path

from mcp_zwave_specs.config import Config
from mcp_zwave_specs.extractors.pdf import PageChunk, extract_pages
from mcp_zwave_specs.models import SpecSection

logger = logging.getLogger(__name__)


def _split_by_toc(
    pages: list[PageChunk],
    pdf_name: str,
    min_level: int = 1,
    max_level: int = 2,
) -> list[SpecSection]:
    """Split pages into sections using TOC entries at the specified levels."""
    # Collect TOC entries at the desired levels
    toc_entries: list[tuple[str, int]] = []  # (title, page_number)
    for page in pages:
        for level, title, page_num in page.toc_items:
            if min_level <= level <= max_level:
                toc_entries.append((title, page_num))

    if not toc_entries:
        # No TOC — return as a single section
        content = "\n".join(p.text for p in pages)
        return [SpecSection(title=pdf_name, content=content, pdf_name=pdf_name)]

    sections: list[SpecSection] = []
    for i, (title, start_page) in enumerate(toc_entries):
        end_page = toc_entries[i + 1][1] if i + 1 < len(toc_entries) else pages[-1].page_number + 1

        parts: list[str] = []
        for page in pages:
            if page.page_number < start_page:
                continue
            if page.page_number >= end_page:
                break
            parts.append(f"\n<!-- PAGE {page.page_number + 1} -->\n")
            parts.append(page.text)

        content = "\n".join(parts).strip()
        if not content:
            continue

        sections.append(
            SpecSection(
                title=title,
                content=content,
                pdf_name=pdf_name,
                section_number=str(i + 1),
                page_start=start_page + 1,
                page_end=end_page,
            )
        )

    return sections


def _extract_pdf_group(
    result: dict[str, list[SpecSection]],
    pdf_map: dict[str, str],
    base_dir: Path,
) -> None:
    """Extract a group of PDFs from a directory into result."""
    for key, filename in pdf_map.items():
        pdf_path = base_dir / filename
        if not pdf_path.exists():
            logger.warning("PDF not found: %s", pdf_path)
            continue
        pages = extract_pages(pdf_path)
        sections = _split_by_toc(pages, key)
        result[key] = sections
        logger.info("Split %s into %d sections", key, len(sections))


def extract_supplementary(config: Config) -> dict[str, list[SpecSection]]:
    """Extract and split all supplementary PDFs.

    Returns a dict of pdf_key → list of SpecSection.
    """
    result: dict[str, list[SpecSection]] = {}
    stack_dir = config.specs_dir / "Z-Wave Stack Specifications"

    # Stack specification PDFs
    _extract_pdf_group(result, config.supplementary_pdfs, stack_dir)

    # Test specification PDFs (some in Stack Specs, one in CC Specs)
    _extract_pdf_group(result, config.test_pdfs, stack_dir)
    # CC Control Test Spec is in a different directory
    cc_test_path = (
        config.specs_dir
        / "Z-Wave Command Classes Specifications"
        / "Z-Wave Command Class Control Test Specification.pdf"
    )
    if cc_test_path.exists():
        pages = extract_pages(cc_test_path)
        sections = _split_by_toc(pages, "test_cc_control")
        result["test_cc_control"] = sections

    # Z-Wave Plus v2 Device Type Test Spec
    zwp_test = config.specs_dir / "Z-Wave Plus v2 Specifications"
    if zwp_test.is_dir():
        _extract_pdf_group(
            result,
            {"test_device_type": "Z-Wave Plus v2 Device Type Test Specification.pdf"},
            zwp_test,
        )

    # Standalone PDFs (top-level)
    for key, filename in config.standalone_pdfs.items():
        pdf_path = config.specs_dir / filename
        if not pdf_path.exists():
            logger.warning("PDF not found: %s", pdf_path)
            continue
        pages = extract_pages(pdf_path)
        sections = _split_by_toc(pages, key)
        result[key] = sections
        logger.info("Split %s into %d sections", key, len(sections))

    # Legacy specification PDFs
    legacy_dir = config.specs_dir / "Legacy Specifications"
    if legacy_dir.is_dir():
        _extract_pdf_group(result, config.legacy_pdfs, legacy_dir)

    # SmartStart PDFs
    smartstart_dir = config.smartstart_dir
    if smartstart_dir.is_dir():
        for pdf_path in sorted(smartstart_dir.glob("*.pdf")):
            key = "smartstart_" + pdf_path.stem.lower().replace(" ", "_").replace("-", "_")
            pages = extract_pages(pdf_path)
            sections = _split_by_toc(pages, key)
            result[key] = sections
            logger.info("Split %s into %d sections", key, len(sections))

    # Application Notes (Z-Wave specific only)
    app_notes_dir = config.app_notes_dir
    if app_notes_dir.is_dir():
        for pdf_path in sorted(app_notes_dir.glob("*.pdf")):
            if not pdf_path.stem.startswith(("APL", "INS")):
                continue
            key = "appnote_" + pdf_path.stem.lower().replace(" ", "_").replace("-", "_")
            pages = extract_pages(pdf_path)
            sections = _split_by_toc(pages, key)
            result[key] = sections
            logger.info("Split %s into %d sections", key, len(sections))

    return result
