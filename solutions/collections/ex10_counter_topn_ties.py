"""Эталон упражнения 10: Top-N с развязкой ничьих."""

from __future__ import annotations

from collections import Counter


def top_n(counter: Counter[str], n: int) -> list[tuple[str, int]]:
    return sorted(counter.items(), key=lambda item: (-item[1], item[0]))[:n]


def bottom_n(counter: Counter[str], n: int) -> list[tuple[str, int]]:
    return sorted(counter.items(), key=lambda item: (item[1], item[0]))[:n]


def top_n_by_key(counter: Counter[str], n: int) -> list[tuple[str, int]]:
    return sorted(counter.items(), key=lambda item: item[0])[:n]


def rank_words(text: str, n: int) -> list[tuple[str, int]]:
    words = text.lower().split()
    return top_n(Counter(words), n)
