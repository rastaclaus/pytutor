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

Разница ``takewhile``/``dropwhile`` и ``filterfalse`` — главная тема набора:
первые две смотрят только на «границу», последняя проверяет каждый элемент.
"""

from __future__ import annotations

from itertools import compress, dropwhile, filterfalse, takewhile
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable


def take_until_negative(values: Iterable[int]) -> list[int]:
    """Взять значения до первого отрицательного (само отрицательное не брать).

    ``take_until_negative([1, 2, -1, 3])`` -> ``[1, 2]`` — после ``-1``
    остановка навсегда, ``3`` уже не попадёт;
    ``take_until_negative([-1, 1])`` -> ``[]``;
    ``take_until_negative([])`` -> ``[]``;
    ``take_until_negative([0, 5])`` -> ``[0, 5]`` — ноль не отрицательный.

    Подсказка: ``takewhile(lambda value: value >= 0, values)``.
    """
    raise NotImplementedError


def skip_leading_zeros(values: Iterable[int]) -> list[int]:
    """Отбросить ведущие нули и вернуть всё остальное как есть.

    ``skip_leading_zeros([0, 0, 1, 0, 2])`` -> ``[1, 0, 2]`` — ноль после
    первого ненулевого остаётся;
    ``skip_leading_zeros([0, 0])`` -> ``[]``;
    ``skip_leading_zeros([1, 0])`` -> ``[1, 0]`` — ведущих нулей нет.

    Подсказка: ``dropwhile(lambda value: value == 0, values)``.
    """
    raise NotImplementedError


def odd_numbers(values: Iterable[int]) -> list[int]:
    """Оставить нечётные числа, используя ``filterfalse``.

    ``odd_numbers([1, 2, 3, 4, 5])`` -> ``[1, 3, 5]``;
    ``odd_numbers([2, 4])`` -> ``[]``;
    ``odd_numbers([])`` -> ``[]``.

    Подсказка: ``filterfalse(lambda value: value % 2 == 0, values)`` —
    отбрасываем чётные, оставшееся и есть нечётные.
    """
    raise NotImplementedError


def falsey_only(values: Iterable[int | None]) -> list[int | None]:
    """Оставить только ложные значения (``0``, ``None``, ``""`` и т.п.).

    ``falsey_only([0, 1, None, 2, ""])`` -> ``[0, None, ""]``;
    ``falsey_only([1, 2])`` -> ``[]``;
    ``falsey_only([])`` -> ``[]``.

    Подсказка: ``filterfalse(None, values)`` — ``None`` вместо предиката берёт
    саму истинность значения, а ``filterfalse`` оставляет ложные.
    """
    raise NotImplementedError


def select_by_mask(data: Iterable[str], mask: Iterable[bool]) -> list[str]:
    """Оставить ``data[i]`` там, где ``mask[i]`` истинно.

    ``select_by_mask("abcdef", [True, False, True, False, False, True])`` ->
    ``["a", "c", "f"]``;
    ``select_by_mask("abcdef", [True, True])`` -> ``["a", "b"]`` — маска короче,
    дальше пар нет;
    ``select_by_mask("ab", [True, True, True])`` -> ``["a", "b"]`` — данные
    короче маски, лишние флаги игнорируются.

    Подсказка: ``compress(data, mask)`` останавливается по любому короткому входу.
    """
    raise NotImplementedError


def drop_while_shorter_than(limit: int, words: Iterable[str]) -> list[str]:
    """Пропустить слова короче ``limit``, а затем вернуть все остальные.

    ``drop_while_shorter_than(3, ["a", "bb", "ccc", "d"])`` -> ``["ccc", "d"]``:
    короткое ``"d"`` в конце сохраняется, потому что порог проверяется только
    до первого достаточно длинного слова;
    ``drop_while_shorter_than(3, ["a", "bb"])`` -> ``[]``;
    ``drop_while_shorter_than(0, ["a"])`` -> ``["a"]``.

    Подсказка: ``dropwhile(lambda word: len(word) < limit, words)``.
    """
    raise NotImplementedError


def count_taken(predicate: Callable[[int], bool], values: Iterable[int]) -> int:
    """Посчитать, сколько элементов взял бы ``takewhile``.

    ``count_taken(lambda value: value < 5, count())`` -> ``5`` (берутся 0..4);
    ``count_taken(lambda value: value > 10, count())`` -> ``0`` — первый же
    элемент не подошёл;
    ``count_taken(bool, [1, 1, 0, 1])`` -> ``2``.

    Вход может быть бесконечным, поэтому считать нужно лениво и без списка.

    Подсказка: ``sum(1 for _ in takewhile(predicate, values))``.
    """
    raise NotImplementedError
