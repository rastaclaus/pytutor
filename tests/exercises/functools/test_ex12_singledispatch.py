"""Тесты упражнения 12: ``singledispatch``."""

from __future__ import annotations

from pytutor.exercises.functools import ex12_singledispatch as ex


def test_int_handler() -> None:
    assert ex.describe(5) == "целое: 5"
    assert ex.describe(-3) == "целое: -3"


def test_str_handler() -> None:
    assert ex.describe("hello") == "строка длиной 5"
    assert ex.describe("") == "строка длиной 0"


def test_list_handler() -> None:
    assert ex.describe([1, 2, 3]) == "список из 3 элементов"
    assert ex.describe([]) == "список из 0 элементов"


def test_point_handler() -> None:
    assert ex.describe(ex.Point(1, 2)) == "точка (1, 2)"


def test_fallback_for_unknown_type() -> None:
    assert ex.describe(3.14) == "неизвестный тип: float"
    assert ex.describe({1: 2}) == "неизвестный тип: dict"


def test_bool_dispatches_to_int() -> None:
    # bool — подкласс int, отдельный обработчик не зарегистрирован.
    assert ex.describe(True) == "целое: True"
