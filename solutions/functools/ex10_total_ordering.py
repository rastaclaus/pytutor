"""Эталон упражнения 10: ``total_ordering``."""

from __future__ import annotations

from functools import total_ordering


@total_ordering
class Version:
    def __init__(self, *parts: int) -> None:
        self.parts = tuple(parts)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Version):
            return NotImplemented
        return self.parts == other.parts

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Version):
            return NotImplemented
        return self.parts < other.parts

    def __repr__(self) -> str:
        return f"Version({', '.join(map(str, self.parts))})"
