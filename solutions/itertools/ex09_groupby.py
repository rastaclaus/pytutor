"""Эталон упражнения 9: ``groupby``."""

from __future__ import annotations

from itertools import groupby
from operator import itemgetter
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable


def runs(values: Iterable[str]) -> list[tuple[str, int]]:
    return [(key, sum(1 for _ in group)) for key, group in groupby(values)]


def groups_as_lists(
    values: Iterable[str], key: Callable[[str], object] | None = None
) -> list[tuple[object, list[str]]]:
    return [(group_key, list(group)) for group_key, group in groupby(values, key)]


def unique_justseen(values: Iterable[str]) -> list[str]:
    return list(map(itemgetter(0), groupby(values)))


def group_by_parity(values: Iterable[int]) -> dict[str, list[int]]:
    ordered = sorted(values, key=lambda value: value % 2)
    return {
        "чётные" if key == 0 else "нечётные": list(group)
        for key, group in groupby(ordered, key=lambda value: value % 2)
    }


def longest_run(values: Iterable[str]) -> tuple[str, int] | None:
    best: tuple[str, int] | None = None
    for key, group in groupby(values):
        length = sum(1 for _ in group)
        if best is None or length > best[1]:
            best = (key, length)
    return best


def group_words_by_length(words: Iterable[str]) -> dict[int, list[str]]:
    ordered = sorted(words, key=len)
    return {length: list(group) for length, group in groupby(ordered, key=len)}
