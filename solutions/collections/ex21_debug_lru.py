"""Эталон упражнения 21: найди баг — LRU-кэш (исправленная версия).

Три бага исходной версии:

1. ``get`` не «освежал» ключ: LRU требует ``move_to_end`` при каждом обращении;
2. ``__init__`` принимал ``capacity <= 0``: должен бросать ``ValueError``;
3. ``put`` вытеснял ``popitem(last=True)`` (свежайший), а нужно ``last=False``
   (самый старый).
"""

from __future__ import annotations

from collections import OrderedDict


class BuggyLRUCache:
    """Кэш ограниченного размера: вытесняет наименее недавно использованный ключ."""

    def __init__(self, capacity: int) -> None:
        """Создать кэш на ``capacity`` элементов."""
        if capacity < 1:
            raise ValueError("capacity должно быть >= 1")
        self.capacity = capacity
        self._data: OrderedDict[str, int] = OrderedDict()

    def get(self, key: str) -> int | None:
        """Вернуть значение по ключу, освежив его (или ``None``)."""
        if key in self._data:
            self._data.move_to_end(key)
            return self._data[key]
        return None

    def put(self, key: str, value: int) -> None:
        """Записать пару; при переполнении вытеснить самого старого."""
        if key in self._data:
            self._data.move_to_end(key)
        self._data[key] = value
        if len(self._data) > self.capacity:
            self._data.popitem(last=False)

    def __len__(self) -> int:
        """Число записей в кэше."""
        return len(self._data)
