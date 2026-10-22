"""Эталон упражнения 11: ``batched`` и рецепт ``grouper``."""

from __future__ import annotations

from itertools import batched, chain, zip_longest
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def batch(items: Iterable[str], size: int) -> list[tuple[str, ...]]:
    return list(batched(items, size))


def batch_strict(items: Iterable[str], size: int) -> list[tuple[str, ...]]:
    return list(batched(items, size, strict=True))


def batch_lengths(items: Iterable[str], size: int) -> list[int]:
    return [len(one) for one in batched(items, size)]


def pad_batches(items: Iterable[str], size: int, fill: str) -> list[tuple[str, ...]]:
    if size < 1:
        raise ValueError("size должно быть >= 1")
    return list(zip_longest(*[iter(items)] * size, fillvalue=fill))


def trim_batches(items: Iterable[str], size: int) -> list[tuple[str, ...]]:
    if size < 1:
        raise ValueError("size должно быть >= 1")
    return list(zip(*[iter(items)] * size))


def reshape(rows: Iterable[Iterable[int]], columns: int) -> list[tuple[int, ...]]:
    if columns < 1:
        raise ValueError("columns должно быть >= 1")
    flat = chain.from_iterable(rows)
    return list(zip(*[iter(flat)] * columns))
