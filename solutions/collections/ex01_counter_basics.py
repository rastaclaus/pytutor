"""Эталон упражнения 1: ``collections.Counter`` — простой счёт частот."""

from __future__ import annotations

from collections import Counter
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def count_characters(text: str) -> Counter[str]:
    return Counter(text)


def count_words(words: Iterable[str]) -> Counter[str]:
    return Counter(words)


def most_common_items(counter: Counter[str], n: int) -> list[tuple[str, int]]:
    if n < 0:
        raise ValueError("n должно быть >= 0")
    return counter.most_common(n)


def total_count(counter: Counter[str]) -> int:
    return counter.total()


def unique_items(counter: Counter[str]) -> list[str]:
    return [key for key, count in counter.items() if count > 0]


def expand(counter: Counter[str]) -> list[str]:
    return list(counter.elements())
