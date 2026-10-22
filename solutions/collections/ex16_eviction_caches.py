"""Эталон упражнения 16: политики вытеснения: FIFO / LRU / LFU."""

from __future__ import annotations

from collections import Counter, OrderedDict


class FIFOCache:
    def __init__(self, capacity: int) -> None:
        if capacity < 1:
            raise ValueError("capacity должно быть >= 1")
        self.capacity = capacity
        self._data: OrderedDict[str, int] = OrderedDict()

    def get(self, key: str) -> int | None:
        return self._data.get(key)

    def put(self, key: str, value: int) -> None:
        if len(self._data) >= self.capacity and key not in self._data:
            self._data.popitem(last=False)
        self._data[key] = value

    def __len__(self) -> int:
        return len(self._data)


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


class LFUCache:
    def __init__(self, capacity: int) -> None:
        if capacity < 1:
            raise ValueError("capacity должно быть >= 1")
        self.capacity = capacity
        self._data: OrderedDict[str, int] = OrderedDict()
        self._freq: Counter[str] = Counter()

    def _evict(self) -> None:
        if not self._data:
            return
        victim = min(self._data, key=lambda key: (self._freq[key], list(self._data).index(key)))
        del self._data[victim]
        del self._freq[victim]

    def get(self, key: str) -> int | None:
        if key not in self._data:
            return None
        self._freq[key] += 1
        self._data.move_to_end(key)
        return self._data[key]

    def put(self, key: str, value: int) -> None:
        if key in self._data:
            self._data[key] = value
            self._freq[key] += 1
            self._data.move_to_end(key)
            return
        if len(self._data) >= self.capacity:
            self._evict()
        self._data[key] = value
        self._freq[key] = 1

    def __len__(self) -> int:
        return len(self._data)
