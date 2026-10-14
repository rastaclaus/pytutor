"""Эталон упражнения 7: основы ``lru_cache`` / ``cache``."""

from __future__ import annotations

from functools import cache


@cache
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


@cache
def catalan(n: int) -> int:
    if n == 0:
        return 1
    return sum(catalan(i) * catalan(n - 1 - i) for i in range(n))
