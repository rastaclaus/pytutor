"""Эталон упражнения 1: основы ``@dataclass``."""

from __future__ import annotations

from dataclasses import dataclass


def declare_point() -> type:
    @dataclass
    class Point:
        """Точка на плоскости."""

        x: int
        y: int

    return Point


def same(a: object, b: object) -> bool:
    return a == b


def as_text(obj: object) -> str:
    return repr(obj)
