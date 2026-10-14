"""Эталон упражнения 13: ``singledispatchmethod``."""

from __future__ import annotations

from functools import singledispatchmethod


class Formatter:
    @singledispatchmethod
    def render(self, value: object) -> str:
        return f"?{value}"

    @render.register
    def _(self, value: int) -> str:
        return f"int:{value}"

    @render.register
    def _(self, value: str) -> str:
        return f"str:{value!r}"
