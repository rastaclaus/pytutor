"""Эталон упражнения 7: ``zip_longest`` и ``zip(strict=True)``."""

from __future__ import annotations

from itertools import zip_longest
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def merge_uneven(left: Iterable[str], right: Iterable[int]) -> list[tuple[str, int | None]]:
    return list(zip_longest(left, right))


def merge_with_fill(left: Iterable[str], right: Iterable[int], fill: int) -> list[tuple[str, int]]:
    return list(zip_longest(left, right, fillvalue=fill))


def zip_strict(left: Iterable[int], right: Iterable[int]) -> list[tuple[int, int]]:
    return list(zip(left, right, strict=True))


def same_length(left: Iterable[int], right: Iterable[int]) -> bool:
    for _ in zip(left, right, strict=True):
        pass
    return True


def grouper(items: Iterable[str], size: int) -> list[tuple[str, ...]]:
    if size < 1:
        raise ValueError("size должно быть >= 1")
    iterators = [iter(items)] * size
    return list(zip_longest(*iterators, fillvalue=""))


def transpose(matrix: list[list[int]]) -> list[tuple[int, ...]]:
    if not matrix:
        return []
    return list(zip(*matrix, strict=True))
