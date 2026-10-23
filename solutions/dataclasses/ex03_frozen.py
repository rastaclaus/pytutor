"""Эталон упражнения 3: замороженные экземпляры."""

from __future__ import annotations

from dataclasses import FrozenInstanceError, dataclass


def declare_frozen_point() -> type:
    @dataclass(frozen=True)
    class FrozenPoint:
        """Неизменяемая точка."""

        x: int
        y: int

    return FrozenPoint


def declare_mutable_point() -> type:
    @dataclass
    class MutPoint:
        """Изменяемая точка."""

        x: int
        y: int

    return MutPoint


def try_to_mutate() -> bool:
    point = declare_frozen_point()(1, 2)
    try:
        point.x = 10  # type: ignore[misc]
    except FrozenInstanceError:
        return True
    return False


def is_hashable(obj: object) -> bool:
    try:
        hash(obj)
    except TypeError:
        return False
    return True
