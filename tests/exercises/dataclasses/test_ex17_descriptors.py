"""Тесты упражнения 17: поля-дескрипторы."""

from __future__ import annotations

import pytest

from pytutor.exercises.dataclasses import ex17_descriptors as ex


def test_default_is_used() -> None:
    item = ex.declare_item()()
    assert item.quantity == 1


def test_value_is_coerced_to_int() -> None:
    item = ex.make_item("7")
    assert item.quantity == 7
    assert isinstance(item.quantity, int)


def test_boundaries() -> None:
    assert ex.make_item(0).quantity == 0
    assert ex.make_item(100).quantity == 100


@pytest.mark.parametrize("value", [-1, 101, "abc"])
def test_out_of_range_rejected(value: object) -> None:
    with pytest.raises(ValueError):
        ex.make_item(value)


def test_assignment_is_validated_too() -> None:
    item = ex.declare_item()()
    item.quantity = "42"
    assert item.quantity == 42
    with pytest.raises(ValueError, match="диапазон"):
        item.quantity = 500
