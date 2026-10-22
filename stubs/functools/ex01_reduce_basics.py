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
    raise NotImplementedError


def concat_strings(strings: Iterable[str]) -> str:
    """Склеить строки в одну.

    Пустая последовательность даёт пустую строку.
    """
    raise NotImplementedError


def sum_with_initial(initial: int, numbers: Iterable[int]) -> int:
    """Вернуть сумму ``numbers``, начав отсчёт с ``initial``.

    Для пустой последовательности результатом будет сам ``initial``.
    """
    raise NotImplementedError


def max_or_none(numbers: Iterable[int]) -> int | None:
    """Вернуть максимум последовательности или ``None``, если она пуста.

    Подсказка: используйте ``initializer=None`` и обрабатывайте его внутри
    свёртки, потому что сравнивать числа с ``None`` нельзя.
    """
    raise NotImplementedError
