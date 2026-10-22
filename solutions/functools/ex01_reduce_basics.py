"""Эталон упражнения 1: основы ``functools.reduce``."""

from __future__ import annotations

from functools import reduce
from operator import add, mul
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def product(numbers: Iterable[int]) -> int:
    return reduce(mul, numbers, 1)


def concat_strings(strings: Iterable[str]) -> str:
    return reduce(add, strings, "")


def sum_with_initial(initial: int, numbers: Iterable[int]) -> int:
    return reduce(add, numbers, initial)


def max_or_none(numbers: Iterable[int]) -> int | None:
    def larger(acc: int | None, value: int) -> int:
        if acc is None or value > acc:
            return value
        return acc

    return reduce(larger, numbers, None)
