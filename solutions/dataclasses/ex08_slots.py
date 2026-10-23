"""Эталон упражнения 8: ``slots=True``."""

from __future__ import annotations

import weakref
from dataclasses import dataclass


def declare_slotted_point() -> type:
    @dataclass(slots=True)
    class SlottedPoint:
        """Точка без ``__dict__``."""

        x: int
        y: int

    return SlottedPoint


def declare_weakref_point() -> type:
    @dataclass(slots=True, weakref_slot=True)
    class WeakPoint:
        """Точка, на которую можно сделать слабую ссылку."""

        x: int
        y: int

    return WeakPoint


def has_instance_dict(obj: object) -> bool:
    return hasattr(obj, "__dict__")


def foreign_attribute_fails() -> bool:
    point = declare_slotted_point()(1, 2)
    try:
        point.z = 3  # type: ignore[attr-defined]
    except AttributeError:
        return True
    return False


def weakref_is_supported() -> bool:
    point = declare_weakref_point()(1, 2)
    return weakref.ref(point)() is point
