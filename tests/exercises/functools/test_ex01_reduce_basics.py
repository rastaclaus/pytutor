"""Тесты упражнения 1: основы ``functools.reduce``."""

from __future__ import annotations

from pytutor.exercises.functools import ex01_reduce_basics as ex


def test_product() -> None:
    assert ex.product([2, 3, 4]) == 24
    assert ex.product([5]) == 5
    # Пустая последовательность — нейтральный элемент умножения.
    assert ex.product([]) == 1


def test_product_with_zero() -> None:
    assert ex.product([2, 0, 4]) == 0


def test_concat_strings() -> None:
    assert ex.concat_strings(["a", "b", "c"]) == "abc"
    assert ex.concat_strings(["hi"]) == "hi"
    assert ex.concat_strings([]) == ""


def test_sum_with_initial() -> None:
    assert ex.sum_with_initial(10, [1, 2, 3]) == 16
    assert ex.sum_with_initial(0, [1, 2, 3]) == 6
    # Пустая последовательность возвращает initial.
    assert ex.sum_with_initial(42, []) == 42


def test_max_or_none() -> None:
    assert ex.max_or_none([3, 1, 2]) == 3
    assert ex.max_or_none([-5, -1, -9]) == -1
    assert ex.max_or_none([7]) == 7
    assert ex.max_or_none([]) is None
