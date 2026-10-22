"""Упражнение 14. Рецепты из документации. Уровень 7.

В документации ``itertools`` есть раздел «Itertools Recipes» — готовые комбинации
инструментов для типовых задач. Здесь три из них:

* ``sliding_window`` — окно на ``deque(maxlen=n)``;
* ``running_mean`` — ``map(truediv, accumulate(values), count(1))``: бегущая
  сумма делится на бегущий счётчик;
* ``sum_of_squares`` — ``sumprod(*tee(values))``: две копии одного потока,
  скалярное произведение вектора с самим собой;
* ``tail`` — последние ``n`` элементов через ``deque(maxlen=n)``.

Общая идея рецептов: не материализовать вход и переиспользовать уже изученные
примитивы вместо ручных циклов.
"""

from __future__ import annotations

from collections import deque
from itertools import accumulate, count, islice, tee
from math import sumprod
from operator import truediv
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def sliding_window(values: Iterable[int], size: int) -> list[tuple[int, ...]]:
    """Все перекрывающиеся окна длины ``size`` (рецепт из документации)."""
    raise NotImplementedError


def running_mean(values: Iterable[int]) -> list[float]:
    """Среднее значение всех элементов, виденных к текущему моменту."""
    raise NotImplementedError


def sum_of_squares(values: Iterable[int]) -> int:
    """Сумма квадратов через ``sumprod`` и ``tee``."""
    raise NotImplementedError


def tail(values: Iterable[int], size: int) -> list[int]:
    """Последние ``size`` элементов без материализации входа."""
    raise NotImplementedError


def running_extremes(values: Iterable[int]) -> list[tuple[int, int]]:
    """Для каждого префикса — пара ``(минимум, максимум)``."""
    raise NotImplementedError


def average_of_top(values: Iterable[int], size: int) -> float:
    """Среднее последних ``size`` элементов.

    Для пустого входа — ``ValueError``.
    """
    raise NotImplementedError


def moving_average(values: Iterable[float], size: int) -> list[float]:
    """Скользящее среднее по окну ``size``."""
    raise NotImplementedError
