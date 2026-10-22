"""Упражнение 16. Политики вытеснения: FIFO / LRU / LFU. Уровень 6.

Кэши ограниченного размера различаются политикой вытеснения:

* FIFO — вытесняется самый старый по времени вставки (``OrderedDict.popitem(last=False)``);
* LRU — вытесняется наименее недавно использованный (``move_to_end`` на каждом обращении);
* LFU — вытесняется наименее часто используемый (считаем обращения через ``Counter``).

Реализуйте три класса кэшей с одинаковым интерфейсом: ``get``/``put``/``__len__``.
"""

from __future__ import annotations

from collections import Counter, OrderedDict


class FIFOCache:
    """Кэш, вытесняющий самый старый по вставке ключ."""

    def __init__(self, capacity: int) -> None:
        """Создать кэш на ``capacity`` элементов (``capacity >= 1``)."""
        raise NotImplementedError

    def get(self, key: str) -> int | None:
        """Вернуть значение (без изменения порядка)."""
        raise NotImplementedError

    def put(self, key: str, value: int) -> None:
        """Записать пару; при переполнении вытеснить самый старый ключ."""
        raise NotImplementedError

    def __len__(self) -> int:
        """Число записей."""
        raise NotImplementedError


class LRUCache:
    """Кэш, вытесняющий наименее недавно использованный ключ."""

    def __init__(self, capacity: int) -> None:
        """Создать кэш на ``capacity`` элементов (``capacity >= 1``)."""
        raise NotImplementedError

    def get(self, key: str) -> int | None:
        """Вернуть значение, освежив ключ (или ``None``)."""
        raise NotImplementedError

    def put(self, key: str, value: int) -> None:
        """Записать пару; при переполнении вытеснить LRU-ключ."""
        raise NotImplementedError

    def __len__(self) -> int:
        """Число записей."""
        raise NotImplementedError


class LFUCache:
    """Кэш, вытесняющий наименее часто используемый ключ.

    Частота считается обращениями ``get``/``put``. При равенстве частот
    вытесняется более старый ключ.
    """

    def __init__(self, capacity: int) -> None:
        """Создать кэш на ``capacity`` элементов (``capacity >= 1``)."""
        raise NotImplementedError

    def get(self, key: str) -> int | None:
        """Вернуть значение, увеличив частоту обращения (или ``None``)."""
        raise NotImplementedError

    def put(self, key: str, value: int) -> None:
        """Записать пару; при переполнении вытеснить LFU-ключ."""
        raise NotImplementedError

    def __len__(self) -> int:
        """Число записей."""
        raise NotImplementedError
