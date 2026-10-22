"""Упражнение 9. ``OrderedDict`` и LRU-кэш. Уровень 4.

``OrderedDict`` — словарь, который помнит порядок вставки ключей. Метод
``move_to_end(key, last=True)`` перемещает ключ в конец; ``popitem(last=False)``
удаляет самый старый ключ (первый). Этого достаточно, чтобы собрать классический
LRU-кэш (Least Recently Used): при каждом обращении ключ «освежается» в конце,
а при переполнении вытесняется ключ из начала.

Обратите внимание: с Python 3.7 обычный ``dict`` тоже сохраняет порядок вставки,
но ``OrderedDict`` даёт ``move_to_end`` и ``popitem(last=)``.
"""

from __future__ import annotations

from collections import OrderedDict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


class LRUCache:
    """Кэш ограниченного размера: вытесняет наименее недавно использованный ключ.

    Реализуйте через ``OrderedDict`` и ``move_to_end``.
    """

    def __init__(self, capacity: int) -> None:
        """Создать кэш на ``capacity`` элементов (``capacity >= 1``)."""
        raise NotImplementedError

    def get(self, key: str) -> int | None:
        """Вернуть значение по ключу, освежив его (или ``None``)."""
        raise NotImplementedError

    def put(self, key: str, value: int) -> None:
        """Записать пару; при переполнении вытеснить самого старого."""
        raise NotImplementedError

    def __len__(self) -> int:
        """Число записей в кэше."""
        raise NotImplementedError


def fifo_cache(items: Iterable[tuple[str, int]], capacity: int) -> list[tuple[str, int]]:
    """Пропустить ``items`` через FIFO-кэш и вернуть вытесненные пары.

    Вытеснение идёт в порядке вставки (первый пришёл — первый ушёл). Вернуть
    список вытесненных пар по мере их вытеснения.
    """
    raise NotImplementedError


def touch(cache: OrderedDict[str, int], key: str) -> OrderedDict[str, int]:
    """Переместить ``key`` в конец ``cache`` (освежить).

    Если ключа нет — ничего не менять. Вернуть ту же ``cache``.
    """
    raise NotImplementedError


def oldest_key(cache: OrderedDict[str, int]) -> str | None:
    """Вернуть ключ, вставленный раньше всех (или ``None`` для пустого)."""
    raise NotImplementedError
