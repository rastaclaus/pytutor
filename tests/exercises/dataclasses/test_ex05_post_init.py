"""Тесты упражнения 5: ``__post_init__`` и вычисляемые поля."""

from __future__ import annotations

import pytest

from pytutor.exercises.dataclasses import ex05_post_init as ex


def test_area_is_computed() -> None:
    rectangle = ex.make_rectangle(3, 4)
    assert rectangle.area == 12


def test_area_is_not_an_init_argument() -> None:
    assert ex.has_area_argument() is True


def test_area_recomputed_on_construction() -> None:
    rectangle_cls = ex.declare_rectangle()
    assert rectangle_cls(2.5, 2).area == 5.0


@pytest.mark.parametrize(("width", "height"), [(0, 1), (1, 0), (-1, 2)])
def test_non_positive_sides_rejected(width: float, height: float) -> None:
    with pytest.raises(ValueError, match="положительн"):
        ex.make_rectangle(width, height)


def test_rectangle_equality() -> None:
    rectangle_cls = ex.declare_rectangle()
    assert rectangle_cls(2, 3) == rectangle_cls(2, 3)
