"""Тесты упражнения 8: ``slots=True``."""

from __future__ import annotations

from pytutor.exercises.dataclasses import ex08_slots as ex


def test_slotted_point_works() -> None:
    point_cls = ex.declare_slotted_point()
    point = point_cls(1, 2)
    assert (point.x, point.y) == (1, 2)


def test_slotted_has_no_dict() -> None:
    assert ex.has_instance_dict(ex.declare_slotted_point()(1, 2)) is False


def test_object_with_dict_is_detected() -> None:
    class Plain:
        x: int

    instance = Plain()
    instance.x = 1
    assert ex.has_instance_dict(instance) is True


def test_foreign_attribute_fails() -> None:
    assert ex.foreign_attribute_fails() is True


def test_weakref_is_supported() -> None:
    assert ex.weakref_is_supported() is True


def test_slots_define_attributes() -> None:
    point_cls = ex.declare_slotted_point()
    assert set(point_cls.__slots__) == {"x", "y"}
