"""Эталон упражнения 5: ``accumulate``."""

from __future__ import annotations

import operator
from functools import reduce
from itertools import accumulate
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def running_sum(numbers: Iterable[int]) -> list[int]:
    return list(accumulate(numbers))


def running_sum_with_start(start: int, numbers: Iterable[int]) -> list[int]:
    return list(accumulate(numbers, initial=start))


def running_product(numbers: Iterable[int]) -> list[int]:
    return list(accumulate(numbers, operator.mul))


def running_max(numbers: Iterable[int]) -> list[int]:
    return list(accumulate(numbers, max))


def running_balance(transactions: Iterable[int]) -> list[int]:
    return list(accumulate(transactions, initial=0))


def final_sum(numbers: Iterable[int]) -> int:
    return reduce(operator.add, numbers, 0)


def running_pairwise_ratio(numbers: Iterable[int]) -> list[float]:
    values = list(numbers)
    if not values:
        return []
    return list(accumulate(values[1:], operator.truediv, initial=values[0]))
