"""Simple in-memory full-text search index with phrase boosting."""

from __future__ import annotations

import math
import re
from collections import defaultdict
from dataclasses import dataclass, field


@dataclass
class SearchResult:
    key: str
    title: str
    score: float
    snippet: str = ""


@dataclass
class _Document:
    key: str
    title: str
    text: str
    word_freq: dict[str, int] = field(default_factory=dict)


def _tokenize(text: str) -> list[str]:
    """Split text into lowercase word tokens."""
    return re.findall(r"[a-z0-9]+", text.lower())


class SearchIndex:
    """Word-based inverted index with TF-IDF scoring and phrase boosting."""

    def __init__(self) -> None:
        self._docs: dict[str, _Document] = {}
        self._inverted: dict[str, set[str]] = defaultdict(set)  # word → doc keys
        self._doc_count = 0

    def add(self, key: str, title: str, text: str) -> None:
        words = _tokenize(text)
        freq: dict[str, int] = defaultdict(int)
        for w in words:
            freq[w] += 1

        doc = _Document(key=key, title=title, text=text, word_freq=dict(freq))
        self._docs[key] = doc
        self._doc_count += 1

        for word in freq:
            self._inverted[word].add(key)

    def search(self, query: str, max_results: int = 10) -> list[SearchResult]:
        query_words = _tokenize(query)
        if not query_words:
            return []

        # Score documents using TF-IDF
        scores: dict[str, float] = defaultdict(float)
        for word in query_words:
            if word not in self._inverted:
                continue
            doc_keys = self._inverted[word]
            idf = math.log(1 + self._doc_count / len(doc_keys))
            for key in doc_keys:
                doc = self._docs[key]
                tf = doc.word_freq.get(word, 0)
                scores[key] += tf * idf

        # Phrase boost: bonus for consecutive query words appearing together
        if len(query_words) > 1:
            query_phrase = " ".join(query_words)
            for key in scores:
                doc = self._docs[key]
                lower_text = doc.text.lower()
                # Full phrase match in text
                if query_phrase in lower_text:
                    scores[key] *= 3.0
                # Title match
                if query_phrase in doc.title.lower():
                    scores[key] *= 5.0

        # Title word boost
        for key in scores:
            doc = self._docs[key]
            title_words = set(_tokenize(doc.title))
            matching = sum(1 for w in query_words if w in title_words)
            if matching:
                scores[key] *= 1.0 + matching * 0.5

        # Sort by score and return top results
        ranked = sorted(scores.items(), key=lambda x: -x[1])[:max_results]

        results = []
        for key, score in ranked:
            doc = self._docs[key]
            snippet = _extract_snippet(doc.text, query_words)
            results.append(SearchResult(key=key, title=doc.title, score=score, snippet=snippet))

        return results


def _extract_snippet(text: str, query_words: list[str], context_chars: int = 200) -> str:
    """Extract a snippet around the first occurrence of any query word."""
    lower = text.lower()
    best_pos = len(text)

    for word in query_words:
        pos = lower.find(word)
        if 0 <= pos < best_pos:
            best_pos = pos

    if best_pos >= len(text):
        return text[:context_chars] + "..."

    start = max(0, best_pos - context_chars // 2)
    end = min(len(text), best_pos + context_chars)

    snippet = text[start:end].strip()
    if start > 0:
        snippet = "..." + snippet
    if end < len(text):
        snippet = snippet + "..."

    return snippet
