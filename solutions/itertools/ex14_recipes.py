"""Эталон упражнения 14: рецепты из документации."""

from __future__ import annotations

from collections import deque
from itertools import accumulate, count, islice, tee
from math import sumprod
from operator import truediv
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def sliding_window(values: Iterable[int], size: int) -> list[tuple[int, ...]]:
    if size <= 0:
        raise ValueError("size должно быть > 0")
    iterator = iter(values)
    window = deque(islice(iterator, size - 1), maxlen=size)
    result: list[tuple[int, ...]] = []
    for value in iterator:
        window.append(value)
        if len(window) == size:
            result.append(tuple(window))
    return result


def running_mean(values: Iterable[int]) -> list[float]:
    return list(map(truediv, accumulate(values), count(1)))


def sum_of_squares(values: Iterable[int]) -> int:
    return sumprod(*tee(values))


def tail(values: Iterable[int], size: int) -> list[int]:
    if size <= 0:
        return []
    return list(deque(values, maxlen=size))


def running_extremes(values: Iterable[int]) -> list[tuple[int, int]]:
    return list(zip(accumulate(values, min), accumulate(values, max), strict=True))


def average_of_top(values: Iterable[int], size: int) -> float:
    last = tail(values, size)
    if not last:
        raise ValueError("пустой вход")
    return sum(last) / len(last)


def moving_average(values: Iterable[float], size: int) -> list[float]:
    return [sum(window) / size for window in sliding_window(values, size)]
