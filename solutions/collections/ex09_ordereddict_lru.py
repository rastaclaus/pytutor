"""Эталон упражнения 9: ``OrderedDict`` и LRU-кэш."""

from __future__ import annotations

from collections import OrderedDict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


class LRUCache:
    def __init__(self, capacity: int) -> None:
        if capacity < 1:
            raise ValueError("capacity должно быть >= 1")
        self.capacity = capacity
        self._data: OrderedDict[str, int] = OrderedDict()

    def get(self, key: str) -> int | None:
        if key not in self._data:
            return None
        self._data.move_to_end(key)
        return self._data[key]

    def put(self, key: str, value: int) -> None:
        if key in self._data:
            self._data.move_to_end(key)
        self._data[key] = value
        if len(self._data) > self.capacity:
            self._data.popitem(last=False)

    def __len__(self) -> int:
        return len(self._data)


def fifo_cache(items: Iterable[tuple[str, int]], capacity: int) -> list[tuple[str, int]]:
    if capacity < 1:
        raise ValueError("capacity должно быть >= 1")
    cache: OrderedDict[str, int] = OrderedDict()
    evicted: list[tuple[str, int]] = []
    for key, value in items:
        if len(cache) >= capacity and key not in cache:
            evicted.append(cache.popitem(last=False))
        cache[key] = value
    return evicted


def touch(cache: OrderedDict[str, int], key: str) -> OrderedDict[str, int]:
    if key in cache:
        cache.move_to_end(key)
    return cache


def oldest_key(cache: OrderedDict[str, int]) -> str | None:
    if not cache:
        return None
    return next(iter(cache))
