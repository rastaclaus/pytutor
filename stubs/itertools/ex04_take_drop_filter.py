"""Упражнение 4. Условные префиксы и фильтры. Уровень 3.

Четыре инструмента с разными правилами остановки:

* ``takewhile(pred, it)`` — берёт, пока ``pred`` истинно, и **останавливается
  навсегда** на первом провале (этот элемент уже потреблён и потерян);
* ``dropwhile(pred, it)`` — пропускает, пока ``pred`` истинно, затем отдаёт всё
  остальное без проверок, включая элементы, для которых ``pred`` снова истинно;
* ``filterfalse(pred, it)`` — оставляет элементы, для которых ``pred`` ложно
  (``pred=None`` оставляет ложные значения);
* ``compress(data, selectors)`` — оставляет ``data[i]``, если ``selectors[i]``
  истинно; заканчивается, когда кончится любой из потоков.

Ни одна из функций не должна материализовать вход целиком.
"""

from __future__ import annotations

from itertools import compress, dropwhile, filterfalse, takewhile
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable


def take_until_negative(values: Iterable[int]) -> list[int]:
    """Взять значения до первого отрицательного (само отрицательное не брать)."""
    raise NotImplementedError


def skip_leading_zeros(values: Iterable[int]) -> list[int]:
    """Отбросить ведущие нули и вернуть всё остальное как есть.

    ``[0, 0, 1, 0, 2]`` даёт ``[1, 0, 2]``. Для ``[0, 0]`` — пустой список.
    """
    raise NotImplementedError


def odd_numbers(values: Iterable[int]) -> list[int]:
    """Оставить нечётные числа, используя ``filterfalse``."""
    raise NotImplementedError


def falsey_only(values: Iterable[int | None]) -> list[int | None]:
    """Оставить только ложные значения (``0``, ``None``, ``""`` и т.п.)."""
    raise NotImplementedError


def select_by_mask(data: Iterable[str], mask: Iterable[bool]) -> list[str]:
    """Оставить ``data[i]`` там, где ``mask[i]`` истинно."""
    raise NotImplementedError


def drop_while_shorter_than(limit: int, words: Iterable[str]) -> list[str]:
    """Пропустить слова короче ``limit``, а затем вернуть все остальные.

    Порог проверяется только в начале: после первого достаточно длинного слова
    короткие тоже попадают в результат.
    """
    raise NotImplementedError


def count_taken(predicate: Callable[[int], bool], values: Iterable[int]) -> int:
    """Посчитать, сколько элементов взял бы ``takewhile``.

    Подсказка: ``sum(1 for _ in takewhile(...))``; вход может быть бесконечным.
    """
    raise NotImplementedError
