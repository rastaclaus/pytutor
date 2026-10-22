"""Эталон упражнения 6: ``starmap`` и ``repeat``."""

from __future__ import annotations

import operator
from functools import partial
from itertools import repeat, starmap
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable


def _format_measurement(value: int, *, unit: str) -> str:
    return f"{value} {unit}"


def apply_pairs(func: Callable[[int, int], int], pairs: Iterable[tuple[int, int]]) -> list[int]:
    return list(starmap(func, pairs))


def dot_product(left: Iterable[int], right: Iterable[int]) -> int:
    # Именно starmap: пары из zip распаковываются в аргументы mul.
    pairs = zip(left, right, strict=False)
    return sum(starmap(operator.mul, pairs))


def total_cost(rows: Iterable[tuple[int, int]]) -> int:
    return sum(starmap(operator.mul, rows))


def repeat_apply(func: Callable[[str], str], value: str, times: int) -> list[str]:
    return list(map(func, repeat(value, max(times, 0))))


def pair_with_constant(values: Iterable[str], constant: int) -> list[tuple[str, int]]:
    return list(zip(values, repeat(constant), strict=False))


def apply_all(functions: Iterable[Callable[[int], int]], value: int) -> list[int]:
    return list(map(operator.call, functions, repeat(value)))


def make_formatter(unit: str) -> Callable[[int], str]:
    return partial(_format_measurement, unit=unit)


def format_values(values: Iterable[int], unit: str) -> list[str]:
    return list(map(make_formatter(unit), values))
