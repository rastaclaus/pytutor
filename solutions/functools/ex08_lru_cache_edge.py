"""Эталон упражнения 8: тонкости ``lru_cache``."""

from __future__ import annotations

from functools import lru_cache


@lru_cache(typed=True)
def add_typed(a: int, b: int) -> int:
    return a + b


@lru_cache(typed=False)
def add_untyped(a: int, b: int) -> int:
    return a + b


@lru_cache(maxsize=2)
def limited(x: int) -> int:
    return x * x
