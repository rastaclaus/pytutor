"""Эталон упражнения 4: ``takewhile``/``dropwhile``/``filterfalse``/``compress``."""

from __future__ import annotations

from itertools import compress, dropwhile, filterfalse, takewhile
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable


def take_until_negative(values: Iterable[int]) -> list[int]:
    return list(takewhile(lambda value: value >= 0, values))


def skip_leading_zeros(values: Iterable[int]) -> list[int]:
    return list(dropwhile(lambda value: value == 0, values))


def odd_numbers(values: Iterable[int]) -> list[int]:
    return list(filterfalse(lambda value: value % 2 == 0, values))


def falsey_only(values: Iterable[int | None]) -> list[int | None]:
    return list(filterfalse(None, values))


def select_by_mask(data: Iterable[str], mask: Iterable[bool]) -> list[str]:
    return list(compress(data, mask))


def drop_while_shorter_than(limit: int, words: Iterable[str]) -> list[str]:
    return list(dropwhile(lambda word: len(word) < limit, words))


def count_taken(predicate: Callable[[int], bool], values: Iterable[int]) -> int:
    return sum(1 for _ in takewhile(predicate, values))
