"""Упражнение 11. ``functools.cmp_to_key``. Уровень 6.

Иногда сортировку нельзя выразить ключом, зато легко записать компаратор
(функцию от двух элементов, возвращающую `-1`, `0` или `1`). Тогда его оборачивают
в ``cmp_to_key`` и передают в ``key=``.

Реализуйте:

* ``compare_by_absolute`` — сравнение чисел по модулю;
* ``sort_by_absolute`` — сортировка списка по модулю;
* ``compare_natural`` — «естественное» сравнение строк, где ``"file2"`` меньше
  ``"file10"`` (числовые куски сравниваются как числа, а не как текст);
* ``natural_sort`` — естественная сортировка списка строк.
"""

from __future__ import annotations

from functools import cmp_to_key


def compare_by_absolute(a: int, b: int) -> int:
    """Вернуть ``-1``/``0``/``1`` в зависимости от ``abs(a)`` и ``abs(b)``."""
    raise NotImplementedError


def sort_by_absolute(values: list[int]) -> list[int]:
    """Отсортировать ``values`` по возрастанию модуля (через ``cmp_to_key``)."""
    raise NotImplementedError


def compare_natural(a: str, b: str) -> int:
    """Естественное сравнение строк с числами внутри."""
    raise NotImplementedError


def natural_sort(strings: list[str]) -> list[str]:
    """Отсортировать строки в естественном порядке (через ``cmp_to_key``)."""
    raise NotImplementedError
