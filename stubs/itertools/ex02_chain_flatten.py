"""Упражнение 2. Объединение потоков: ``chain``. Уровень 2.

``chain(a, b, c)`` отдаёт элементы сначала из ``a``, потом из ``b``, потом из
``c`` — не создавая объединённого списка. ``chain.from_iterable(x)`` делает то же
для *одного* аргумента — итерируемого объекта, который сам выдаёт итерируемые
объекты. Это стандартный способ «выпрямить» вложенность на один уровень.

Важно: ``chain`` ленив. Пока результат не начали потреблять, ни один источник не
будет прочитан.
"""

from __future__ import annotations

from itertools import chain, islice
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def flatten(nested: Iterable[Iterable[int]]) -> list[int]:
    """Выпрямить вложенность ровно на один уровень.

    ``[[1, 2], [], [3]]`` даёт ``[1, 2, 3]``. Вход может быть генератором.
    """
    raise NotImplementedError


def concat(*iterables: Iterable[str]) -> list[str]:
    """Склеить несколько итерируемых объектов в один список.

    ``concat("ab", ["c"], ())`` даёт ``["a", "b", "c"]``.
    """
    raise NotImplementedError


def words_of(lines: Iterable[str]) -> list[str]:
    """Разбить строки на слова, собрав всё в один плоский список.

    ``words_of(["a b", "c"])`` даёт ``["a", "b", "c"]``. Пустые строки
    не должны давать пустых слов.
    """
    raise NotImplementedError


def take_flattened(nested: Iterable[Iterable[int]], n: int) -> list[int]:
    """Взять первые ``n`` элементов выпрямленного потока, не выпрямляя его целиком.

    Подсказка: ``islice(chain.from_iterable(nested), n)``.
    """
    raise NotImplementedError
