"""Эталон упражнения 10: ``tee``."""

from __future__ import annotations

from itertools import filterfalse, tee
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable


def duplicate(values: Iterable[int]) -> tuple[list[int], list[int]]:
    left, right = tee(values, 2)
    return list(left), list(right)


def peek(values: Iterable[str]) -> tuple[str | None, list[str]]:
    first, rest = tee(values, 2)
    head = next(iter(first), None)
    return head, list(rest)


def split_by_predicate(values: Iterable[int], predicate: Callable[[int], bool]) -> tuple[list[int], list[int]]:
    matched, unmatched = tee(values, 2)
    return (
        [value for value in matched if predicate(value)],
        list(filterfalse(predicate, unmatched)),
    )


def count_calls_once(values: Iterable[int]) -> tuple[int, int]:
    first, second = tee(values, 2)
    return sum(first), sum(1 for _ in second)


def first_and_last(values: Iterable[int]) -> tuple[int, int] | None:
    head, tail = tee(values, 2)
    first = next(iter(head), None)
    if first is None:
        return None
    last = first
    for value in tail:
        last = value
    return first, last


def lookahead_pairs(values: Iterable[int]) -> list[tuple[int, int | None]]:
    current, following = tee(values, 2)
    next(following, None)
    return [(value, next(following, None)) for value in current]
