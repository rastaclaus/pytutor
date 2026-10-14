"""Эталон упражнения 12: ``singledispatch``."""

from __future__ import annotations

from functools import singledispatch
from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


@singledispatch
def describe(value: object) -> str:
    return f"неизвестный тип: {type(value).__name__}"


@describe.register
def _(value: int) -> str:
    return f"целое: {value}"


@describe.register
def _(value: str) -> str:
    return f"строка длиной {len(value)}"


@describe.register
def _(value: list) -> str:
    return f"список из {len(value)} элементов"


@describe.register
def _(value: Point) -> str:
    return f"точка ({value.x}, {value.y})"
