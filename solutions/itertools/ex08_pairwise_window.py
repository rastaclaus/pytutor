"""Эталон упражнения 8: ``pairwise`` и скользящее окно."""

from __future__ import annotations

from collections import deque
from itertools import islice, pairwise
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator


def adjacent_pairs(values: Iterable[str]) -> list[tuple[str, str]]:
    return list(pairwise(values))


def differences(values: Iterable[int]) -> list[int]:
    return [right - left for left, right in pairwise(values)]


def all_increasing(values: Iterable[int]) -> bool:
    return all(left < right for left, right in pairwise(values))


def sliding_window(values: Iterable[int], size: int) -> list[tuple[int, ...]]:
    if size <= 0:
        raise ValueError("size должно быть > 0")
    iterator = iter(values)
    window = deque(islice(iterator, size), maxlen=size)
    if len(window) < size:
        return []
    result = [tuple(window)]
    for value in iterator:
        window.append(value)
        result.append(tuple(window))
    return result


def tail(values: Iterable[int], size: int) -> list[int]:
    if size <= 0:
        return []
    return list(deque(values, maxlen=size))


def window_sums(values: Iterable[int], size: int) -> list[int]:
    return [sum(window) for window in sliding_window(values, size)]


def pairwise_iter(values: Iterable[int]) -> Iterator[tuple[int, int]]:
    return pairwise(values)


def first_window_above(values: Iterable[int], size: int, limit: int) -> tuple[int, ...] | None:
    return next(
        (window for window in sliding_window(values, size) if sum(window) > limit),
        None,
    )
