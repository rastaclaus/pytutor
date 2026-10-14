"""Эталон упражнения 2: ``reduce`` для агрегации."""

from __future__ import annotations

from collections.abc import Callable, Iterable
from functools import reduce
from typing import TypeVar

T = TypeVar("T")
K = TypeVar("K")


def flatten(nested: Iterable[Iterable[int]]) -> list[int]:
    def extend(acc: list[int], chunk: Iterable[int]) -> list[int]:
        acc.extend(chunk)
        return acc

    return reduce(extend, nested, [])


def count_items(items: Iterable[str]) -> dict[str, int]:
    def bump(acc: dict[str, int], item: str) -> dict[str, int]:
        acc[item] = acc.get(item, 0) + 1
        return acc

    return reduce(bump, items, {})


def most_common(items: Iterable[str]) -> str | None:
    counts = count_items(items)
    if not counts:
        return None
    # max возвращает первый максимальный элемент в порядке вставки,
    # то есть при равенстве частот побеждает тот, что встретился раньше.
    return max(counts, key=counts.get)


def group_by(items: Iterable[T], key: Callable[[T], K]) -> dict[K, list[T]]:
    def put(acc: dict[K, list[T]], item: T) -> dict[K, list[T]]:
        acc.setdefault(key(item), []).append(item)
        return acc

    return reduce(put, items, {})
