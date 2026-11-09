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


def make_stats_tracker(maxsize: int) -> dict[str, int]:
    """Бонус: статистика кэша после серии вызовов."""

    @lru_cache(maxsize=maxsize)
    def square(x: int) -> int:
        return x * x

    for i in range(10):
        square(i)
    for i in range(5):
        square(i)

    info = square.cache_info()
    return {"hits": info.hits, "misses": info.misses, "currsize": info.currsize}
