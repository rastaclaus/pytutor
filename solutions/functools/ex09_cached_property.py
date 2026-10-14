"""Эталон упражнения 9: ``cached_property``."""

from __future__ import annotations

from functools import cached_property


class HeavyValue:
    def __init__(self, base: int) -> None:
        self.base = base
        self.computations = 0

    @cached_property
    def value(self) -> int:
        self.computations += 1
        return self.base**2
