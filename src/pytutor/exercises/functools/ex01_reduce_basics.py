"""Упражнение 1. Основы ``functools.reduce``. Уровень 1.

``reduce(function, iterable, initializer)`` сворачивает последовательность в одно
значение, последовательно применяя ``function(accumulator, element)``.
Если передан ``initializer``, он используется как стартовое значение
аккумулятора (и как результат для пустой последовательности).

Реализуйте все функции через ``functools.reduce``.

Подсказка: модуль ``operator`` даёт готовые ``operator.add`` и ``operator.mul``.
"""

from __future__ import annotations

import functools
import operator
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def product(numbers: Iterable[int]) -> int:
    """Вернуть произведение всех чисел.

    Произведение пустой последовательности равно 1 (нейтральный элемент).
    """
    return functools.reduce(operator.mul, numbers, 1)


def concat_strings(strings: Iterable[str]) -> str:
    """Склеить строки в одну.

    Пустая последовательность даёт пустую строку.
    """
    return functools.reduce(operator.add, strings, "")


def sum_with_initial(initial: int, numbers: Iterable[int]) -> int:
    """Вернуть сумму ``numbers``, начав отсчёт с ``initial``.

    Для пустой последовательности результатом будет сам ``initial``.
    """
    return functools.reduce(operator.add, numbers, initial=initial)

def max_or_none(numbers: Iterable[int]) -> int | None:
    """Вернуть максимум последовательности или ``None``, если она пуста.

    Подсказка: используйте ``initializer=None`` и обрабатывайте его внутри
    свёртки, потому что сравнивать числа с ``None`` нельзя.
    """
    def maximum(a: int | None, b: int) -> int | None:
        if a is None:
            return b
        return max(a, b)
    return functools.reduce(maximum, numbers, None)
