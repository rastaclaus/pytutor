"""Тесты упражнения 7: основы ``lru_cache`` / ``cache``."""

from __future__ import annotations

from pytutor.exercises.functools import ex07_lru_cache_basics as ex


def test_fib_values() -> None:
    assert [ex.fib(n) for n in range(8)] == [0, 1, 1, 2, 3, 5, 8, 13]
    assert ex.fib(30) == 832040


def test_fib_is_memoized() -> None:
    ex.fib.cache_clear()
    assert ex.fib(20) == 6765
    info = ex.fib.cache_info()
    # Рекурсия впервые вычисляет fib(0)..fib(20): 21 промах.
    assert info.misses == 21
    assert info.hits > 0


def test_cache_clear_resets_state() -> None:
    ex.fib(10)
    ex.fib.cache_clear()
    assert ex.fib.cache_info().currsize == 0


def test_catalan_values() -> None:
    assert [ex.catalan(n) for n in range(6)] == [1, 1, 2, 5, 14, 42]
    assert ex.catalan(10) == 16796


def test_catalan_is_memoized() -> None:
    ex.catalan.cache_clear()
    ex.catalan(15)
    assert ex.catalan.cache_info().hits > 0
