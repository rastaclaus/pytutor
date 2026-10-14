"""Тесты упражнения 8: тонкости ``lru_cache``."""

from __future__ import annotations

from pytutor.exercises.functools import ex08_lru_cache_edge as ex


def test_add_typed_distinguishes_int_and_float() -> None:
    ex.add_typed.cache_clear()
    assert ex.add_typed(1, 2) == 3
    assert ex.add_typed(1.0, 2.0) == 3.0
    info = ex.add_typed.cache_info()
    # 1 и 1.0 (а также 2 и 2.0) — разные ключи.
    assert info.misses == 2
    assert info.hits == 0


def test_add_untyped_merges_int_and_float() -> None:
    ex.add_untyped.cache_clear()
    assert ex.add_untyped(1, 2) == 3
    assert ex.add_untyped(1.0, 2.0) == 3.0
    info = ex.add_untyped.cache_info()
    assert info.misses == 1
    assert info.hits == 1


def test_limited_cache_size() -> None:
    ex.limited.cache_clear()
    for x in (1, 2, 3):
        ex.limited(x)
    info = ex.limited.cache_info()
    assert info.maxsize == 2
    assert info.currsize == 2


def test_limited_counts_hits_within_window() -> None:
    ex.limited.cache_clear()
    ex.limited(1)
    ex.limited(2)
    ex.limited(1)  # попадание
    assert ex.limited.cache_info().hits == 1
