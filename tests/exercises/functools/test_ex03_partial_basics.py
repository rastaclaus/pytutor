"""Тесты упражнения 3: основы ``functools.partial``."""

from __future__ import annotations

import functools

from pytutor.exercises.functools import ex03_partial_basics as ex


def test_make_multiplier() -> None:
    triple = ex.make_multiplier(3)
    assert triple(5) == 15
    assert triple(0) == 0
    # Функция должна возвращаться как functools.partial.
    assert isinstance(triple, functools.partial)


def test_make_power() -> None:
    square = ex.make_power(2)
    cube = ex.make_power(3)
    assert square(5) == 25
    assert cube(2) == 8
    assert square(0) == 0


def test_add_all() -> None:
    assert ex.add_all([1, 2, 3], 10) == [11, 12, 13]
    assert ex.add_all([], 5) == []


def test_make_price_formatter() -> None:
    usd = ex.make_price_formatter("$", 1)
    assert usd(3.5) == "3.5 $"
    assert usd(10.0) == "10.0 $"

    default = ex.make_price_formatter("₽")
    assert default(2) == "2.00 ₽"
