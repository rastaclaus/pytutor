"""Эталон упражнения 3: основы ``functools.partial``."""

from __future__ import annotations

from collections.abc import Callable, Iterable
from functools import partial
from operator import add, mul


def format_currency(
    value: float, currency: str = "₽", decimals: int = 2
) -> str:
    return f"{value:.{decimals}f} {currency}"


def make_multiplier(factor: int) -> Callable[[int], int]:
    return partial(mul, factor)


def make_power(exp: int) -> Callable[[int], int]:
    return partial(pow, exp=exp)


def add_all(numbers: Iterable[int], amount: int) -> list[int]:
    return list(map(partial(add, amount), numbers))


def make_price_formatter(
    currency: str, decimals: int = 2
) -> Callable[[float], str]:
    return partial(format_currency, currency=currency, decimals=decimals)
