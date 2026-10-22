"""Упражнение 3. Основы ``functools.partial``. Уровень 2.

``partial(func, *args, **kwargs)`` возвращает новую функцию, у которой часть
аргументов уже зафиксирована. Это удобно, когда нужно «приготовить» функцию с
конкретной настройкой и передать её дальше (например, в ``map``).

Функция ``format_currency`` уже реализована — она пригодится как готовая основа
для ``make_price_formatter``.
"""

from __future__ import annotations

import operator
from functools import partial
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable


def format_currency(value: float, currency: str = "₽", decimals: int = 2) -> str:
    """Отформатировать сумму: ``format_currency(3.5, "$", 1)`` -> ``"3.5 $"``."""
    return f"{value:.{decimals}f} {currency}"


def make_multiplier(factor: int) -> Callable[[int], int]:
    """Вернуть функцию ``x -> factor * x``.

    Подсказка: ``partial(operator.mul, factor)``.
    """
    raise NotImplementedError


def make_power(exp: int) -> Callable[[int], int]:
    """Вернуть функцию ``base -> base ** exp``.

    Подсказка: ``partial(pow, exp=exp)``.
    """
    raise NotImplementedError


def add_all(numbers: Iterable[int], amount: int) -> list[int]:
    """Вернуть список, где к каждому числу прибавлен ``amount``.

    Реализуйте через ``map`` и ``functools.partial``.
    """
    raise NotImplementedError


def make_price_formatter(currency: str, decimals: int = 2) -> Callable[[float], str]:
    """Вернуть функцию-форматтер цены с зафиксированными ``currency`` и ``decimals``."""
    raise NotImplementedError
