"""Тесты упражнения 1: основы ``@dataclass``."""

from __future__ import annotations

from dataclasses import dataclass, fields

from pytutor.exercises.dataclasses import ex01_basics as ex


def test_declare_point_generates_init() -> None:
    point_cls = ex.declare_point()
    point = point_cls(1, 2)
    assert point_cls.__name__ == "Point"
    assert (point.x, point.y) == (1, 2)


def test_declare_point_generates_repr() -> None:
    point_cls = ex.declare_point()
    # Класс объявлен внутри функции, поэтому в repr попадает его полное имя.
    assert repr(point_cls(1, 2)) == f"{point_cls.__qualname__}(x=1, y=2)"


def test_declare_point_generates_eq() -> None:
    point_cls = ex.declare_point()
    assert point_cls(1, 2) == point_cls(1, 2)
    assert point_cls(1, 2) != point_cls(1, 3)


def test_field_order_follows_declaration() -> None:
    point_cls = ex.declare_point()
    assert [item.name for item in fields(point_cls)] == ["x", "y"]


def test_different_classes_are_not_equal() -> None:
    point_cls = ex.declare_point()

    @dataclass
    class Other:
        x: int
        y: int

    assert not ex.same(point_cls(1, 2), Other(1, 2))
    assert ex.same(point_cls(1, 2), point_cls(1, 2))


def test_as_text_uses_repr() -> None:
    point_cls = ex.declare_point()
    assert ex.as_text(point_cls(3, 4)) == f"{point_cls.__qualname__}(x=3, y=4)"
