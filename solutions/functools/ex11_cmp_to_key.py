"""Эталон упражнения 11: ``cmp_to_key``."""

from __future__ import annotations

import re
from functools import cmp_to_key


def compare_by_absolute(a: int, b: int) -> int:
    x, y = abs(a), abs(b)
    return (x > y) - (x < y)


def sort_by_absolute(values: list[int]) -> list[int]:
    return sorted(values, key=cmp_to_key(compare_by_absolute))


def _natural_parts(text: str) -> list[object]:
    # Разбиваем на чередующиеся текстовые и числовые куски;
    # числовые куски сравниваем как числа.
    return [int(chunk) if chunk.isdigit() else chunk.lower() for chunk in re.split(r"(\d+)", text)]


def compare_natural(a: str, b: str) -> int:
    pa, pb = _natural_parts(a), _natural_parts(b)
    return (pa > pb) - (pa < pb)


def natural_sort(strings: list[str]) -> list[str]:
    return sorted(strings, key=cmp_to_key(compare_natural))
