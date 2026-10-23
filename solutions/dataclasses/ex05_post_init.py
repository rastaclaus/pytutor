"""Эталон упражнения 5: ``__post_init__`` и вычисляемые поля."""

from __future__ import annotations

import inspect
from dataclasses import dataclass, field


def declare_rectangle() -> type:
    @dataclass
    class Rectangle:
        """Прямоугольник с вычисляемой площадью."""

        width: float
        height: float
        area: float = field(init=False)

        def __post_init__(self) -> None:
            if self.width <= 0 or self.height <= 0:
                raise ValueError("стороны должны быть положительными")
            self.area = self.width * self.height

    return Rectangle


def make_rectangle(width: float, height: float) -> object:
    return declare_rectangle()(width, height)


def has_area_argument() -> bool:
    params = inspect.signature(declare_rectangle().__init__).parameters
    return "area" not in params
