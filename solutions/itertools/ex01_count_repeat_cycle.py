"""Эталон упражнения 1: ``count``, ``repeat``, ``cycle``."""

from __future__ import annotations

from itertools import count, cycle, islice, repeat
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def take(n: int, iterable: Iterable[int]) -> list[int]:
    if n <= 0:
        return []
    return list(islice(iterable, n))


def countdown(start: int, n: int) -> list[int]:
    if n <= 0:
        return []
    return list(islice(count(start, -1), n))


def repeat_value(value: str, times: int) -> list[str]:
    return list(repeat(value, max(times, 0)))


def cycle_values(values: list[str], n: int) -> list[str]:
    if n <= 0:
        return []
    return list(islice(cycle(values), n))


def numbered(items: Iterable[str]) -> list[tuple[int, str]]:
    return list(zip(count(), items, strict=False))
