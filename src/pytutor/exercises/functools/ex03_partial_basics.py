"""Упражнение 3. Основы ``functools.partial``. Уровень 2.

``partial(func, *args, **kwargs)`` возвращает новую функцию, у которой часть
аргументов уже зафиксирована. Это удобно, когда нужно «приготовить» функцию с
конкретной настройкой и передать её дальше (например, в ``map``).

Функция ``format_currency`` уже реализована — она пригодится как готовая основа
для ``make_price_formatter``.

Важно: результат ``partial`` — объект типа ``functools.partial``, и тест это
проверяет. Поэтому ``lambda`` в ``make_multiplier`` не подойдёт, а аргументы,
которые нужно зафиксировать по имени, фиксируйте по имени (``decimals=decimals``).
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

    ``make_multiplier(3)(5)`` -> ``15``;
    ``make_multiplier(3)(0)`` -> ``0``;
    ``type(make_multiplier(2))`` — ``functools.partial``.

    Подсказка: ``partial(operator.mul, factor)`` — тогда свободным остаётся
    второй аргумент, то есть множимое.
    """
    raise NotImplementedError


def make_power(exp: int) -> Callable[[int], int]:
    """Вернуть функцию ``base -> base ** exp``.

    ``make_power(2)(5)`` -> ``25``;
    ``make_power(3)(2)`` -> ``8``;
    ``make_power(2)(0)`` -> ``0``.

    Подсказка: у ``pow`` параметры называются ``base`` и ``exp``, поэтому
    фиксируйте степень по имени: ``partial(pow, exp=exp)``. Позиционная форма
    ``partial(pow, exp)`` зафиксировала бы основание, и результат был бы
    ``exp ** x``.
    """
    raise NotImplementedError


def add_all(numbers: Iterable[int], amount: int) -> list[int]:
    """Вернуть список, где к каждому числу прибавлен ``amount``.

    ``add_all([1, 2, 3], 10)`` -> ``[11, 12, 13]``;
    ``add_all([], 5)`` -> ``[]``;
    ``add_all([-1], 1)`` -> ``[0]``.

    Реализуйте через ``map`` и ``functools.partial`` (без лямбд).

    Подсказка: ``map(partial(operator.add, amount), numbers)``. Результат
    ``map`` нужно материализовать в список.
    """
    raise NotImplementedError


def make_price_formatter(currency: str, decimals: int = 2) -> Callable[[float], str]:
    """Вернуть функцию-форматтер цены с зафиксированными ``currency`` и ``decimals``.

    ``make_price_formatter("$", 1)(3.5)`` -> ``"3.5 $"``;
    ``make_price_formatter("₽")(2)`` -> ``"2.00 ₽"`` — ``decimals`` по умолчанию
    равен 2;
    ``make_price_formatter("€", 0)(2.4)`` -> ``"2 €"``.

    Подсказка: ``partial(format_currency, currency=currency, decimals=decimals)``;
    свободным остаётся первый параметр ``value``.
    """
    raise NotImplementedError
