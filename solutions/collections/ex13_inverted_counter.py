"""Эталон упражнения 13: инвертированный индекс: словарь + Counter."""

from __future__ import annotations

from collections import Counter, defaultdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def _words(text: str) -> list[str]:
    return [word for word in text.lower().split() if word]


def inverted_index(documents: Iterable[str]) -> dict[str, list[int]]:
    index: defaultdict[str, set[int]] = defaultdict(set)
    for doc_id, document in enumerate(documents):
        for word in set(_words(document)):
            index[word].add(doc_id)
    return {word: sorted(doc_ids) for word, doc_ids in index.items()}


def positions_of(word: str, text: str) -> list[int]:
    return [i for i, token in enumerate(_words(text)) if token == word.lower()]


def doc_frequency(index: dict[str, list[int]]) -> Counter[str]:
    return Counter({word: len(doc_ids) for word, doc_ids in index.items()})


def search(index: dict[str, list[int]], term: str) -> list[int]:
    return sorted(index.get(term.lower(), []))


def top_terms(index: dict[str, list[int]], n: int) -> list[tuple[str, int]]:
    return sorted(
        ((word, len(doc_ids)) for word, doc_ids in index.items()),
        key=lambda item: (-item[1], item[0]),
    )[:n]
