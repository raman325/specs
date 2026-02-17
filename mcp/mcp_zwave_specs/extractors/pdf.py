"""PDF to Markdown extraction using pymupdf4llm."""

from __future__ import annotations

import logging
import time
from dataclasses import dataclass, field
from pathlib import Path

import pymupdf4llm

logger = logging.getLogger(__name__)

# Log progress every N pages during extraction
_PROGRESS_INTERVAL = 100


@dataclass
class PageChunk:
    """A single page's worth of markdown content from a PDF."""

    page_number: int  # 0-indexed
    text: str
    toc_items: list[tuple[int, str, int]] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)


def extract_pages(pdf_path: Path) -> list[PageChunk]:
    """Extract all pages from a PDF as markdown chunks.

    Uses pymupdf4llm with page_chunks=True for per-page extraction.
    """
    start = time.monotonic()
    logger.info("Extracting markdown from %s", pdf_path.name)

    chunks = pymupdf4llm.to_markdown(str(pdf_path), page_chunks=True)

    total = len(chunks)
    pages: list[PageChunk] = []
    for i, chunk in enumerate(chunks):
        page_num = chunk.get("metadata", {}).get("page", len(pages))
        pages.append(
            PageChunk(
                page_number=page_num,
                text=chunk.get("text", ""),
                toc_items=chunk.get("toc_items", []),
                metadata=chunk.get("metadata", {}),
            )
        )
        if (i + 1) % _PROGRESS_INTERVAL == 0:
            elapsed = time.monotonic() - start
            logger.info("  %s: %d/%d pages (%.1fs elapsed)", pdf_path.name, i + 1, total, elapsed)

    elapsed = time.monotonic() - start
    logger.info("Extracted %d pages from %s in %.1fs", len(pages), pdf_path.name, elapsed)
    return pages


def pages_to_markdown(pages: list[PageChunk], include_page_markers: bool = True) -> str:
    """Join page chunks into a single markdown string with optional page markers."""
    parts: list[str] = []
    for page in pages:
        if include_page_markers:
            parts.append(f"\n<!-- PAGE {page.page_number + 1} -->\n")
        parts.append(page.text)
    return "\n".join(parts)
