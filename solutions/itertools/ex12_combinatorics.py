"""Эталон упражнения 12: комбинаторика."""

from __future__ import annotations

from itertools import combinations, combinations_with_replacement, permutations, product
from math import comb, perm
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def all_pairs(values: Iterable[str]) -> list[tuple[str, str]]:
    return list(product(values, repeat=2))


def permutations_of(values: Iterable[str], r: int) -> list[tuple[str, ...]]:
    return list(permutations(values, r))


def combinations_of(values: Iterable[str], r: int) -> list[tuple[str, ...]]:
    return list(combinations(values, r))


def combinations_with_repeats(values: Iterable[str], r: int) -> list[tuple[str, ...]]:
    return list(combinations_with_replacement(values, r))


def powerset(values: Iterable[str]) -> list[tuple[str, ...]]:
    pool = list(values)
    return [combination for size in range(len(pool) + 1) for combination in combinations(pool, size)]


def count_permutations(n: int, r: int) -> int:
    return perm(n, r)


def count_combinations(n: int, r: int) -> int:
    return comb(n, r)


def dice_sums(sides: int = 6, dice: int = 2) -> dict[int, int]:
    totals: dict[int, int] = {}
    for roll in product(range(1, sides + 1), repeat=dice):
        total = sum(roll)
        totals[total] = totals.get(total, 0) + 1
    return dict(sorted(totals.items()))
