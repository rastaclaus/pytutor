"""Упражнение 1. Основы ``functools.reduce``. Уровень 1.

``reduce(function, iterable, initializer)`` сворачивает последовательность в одно
значение, последовательно применяя ``function(accumulator, element)``.
Если передан ``initializer``, он используется как стартовое значение
аккумулятора (и как результат для пустой последовательности).

Реализуйте все функции через ``functools.reduce``.

Подсказка: модуль ``operator`` даёт готовые ``operator.add`` и ``operator.mul``.

Главное правило набора: ``reduce`` **без** ``initializer`` на пустом входе
бросает ``TypeError``. Поэтому везде, где пустой вход должен давать результат,
нужен явный ``initializer`` — нейтральный элемент операции.
"""

from __future__ import annotations

import functools
import operator
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def product(numbers: Iterable[int]) -> int:
    """Вернуть произведение всех чисел.

    ``product([2, 3, 4])`` -> ``24``;
    ``product([5])`` -> ``5``;
    ``product([])`` -> ``1`` — нейтральный элемент умножения, он же
    ``initializer``;
    ``product([2, 0, 4])`` -> ``0``.

    Подсказка: ``reduce(operator.mul, numbers, 1)``. Без третьего аргумента
    пустой вход упал бы с ``TypeError``.
    """
    raise NotImplementedError


def concat_strings(strings: Iterable[str]) -> str:
    """Склеить строки в одну.

    ``concat_strings(["a", "b", "c"])`` -> ``"abc"``;
    ``concat_strings(["hi"])`` -> ``"hi"``;
    ``concat_strings([])`` -> ``""`` — пустая последовательность даёт пустую
    строку.

    Подсказка: ``reduce(operator.add, strings, "")``.
    """
    raise NotImplementedError


def sum_with_initial(initial: int, numbers: Iterable[int]) -> int:
    """Вернуть сумму ``numbers``, начав отсчёт с ``initial``.

    ``sum_with_initial(10, [1, 2, 3])`` -> ``16``;
    ``sum_with_initial(0, [1, 2, 3])`` -> ``6``;
    ``sum_with_initial(42, [])`` -> ``42`` — для пустой последовательности
    результатом будет сам ``initial``.

    Подсказка: здесь ``initializer`` — это параметр ``initial``, а не константа.
    """
    raise NotImplementedError


def max_or_none(numbers: Iterable[int]) -> int | None:
    """Вернуть максимум последовательности или ``None``, если она пуста.

    ``max_or_none([3, 1, 2])`` -> ``3``;
    ``max_or_none([-5, -1, -9])`` -> ``-1`` — отрицательные числа тоже
    сравниваются как обычно;
    ``max_or_none([7])`` -> ``7``;
    ``max_or_none([])`` -> ``None``.

    Подсказка: используйте ``initializer=None`` и обрабатывайте его внутри
    свёртки, потому что сравнивать числа с ``None`` нельзя: аккумулятор
    ``None`` означает «пока ничего не накопили».
    """
    raise NotImplementedError
