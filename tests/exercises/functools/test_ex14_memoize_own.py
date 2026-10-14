"""Тесты упражнения 14: свой ``memoize``."""

from __future__ import annotations

from pytutor.exercises.functools import ex14_memoize_own as ex


def test_caches_by_arguments() -> None:
    calls: list[tuple[int, int]] = []

    @ex.memoize
    def add(a: int, b: int = 0) -> int:
        calls.append((a, b))
        return a + b

    assert add(1, 2) == 3
    assert add(1, 2) == 3
    assert len(calls) == 1


def test_normalizes_positional_and_keyword_arguments() -> None:
    calls: list[int] = []

    @ex.memoize
    def add(a: int, b: int = 0) -> int:
        calls.append(1)
        return a + b

    add(1, 2)
    add(1, b=2)
    add(b=2, a=1)
    add(a=1, b=2)
    # Все четыре вызова — это одна и та же подпись (a=1, b=2).
    assert len(calls) == 1


def test_defaults_unify_missing_and_explicit() -> None:
    calls: list[int] = []

    @ex.memoize
    def add(a: int, b: int = 0) -> int:
        calls.append(1)
        return a + b

    add(5)
    add(5, 0)
    assert len(calls) == 1


def test_distinguishes_different_arguments() -> None:
    calls: list[int] = []

    @ex.memoize
    def add(a: int, b: int = 0) -> int:
        calls.append(1)
        return a + b

    add(1, 2)
    add(2, 1)
    assert len(calls) == 2


def test_preserves_metadata() -> None:
    @ex.memoize
    def named(x: int) -> int:
        """Докстринг."""
        return x

    assert named.__name__ == "named"
    assert named.__doc__ == "Докстринг."


def test_exposes_cache_and_clear() -> None:
    @ex.memoize
    def identity(x: int) -> int:
        return x

    identity(1)
    identity(2)
    identity(2)
    assert len(identity.cache) == 2
    identity.cache_clear()
    assert len(identity.cache) == 0


def test_speeds_up_recursion() -> None:
    @ex.memoize
    def fib(n: int) -> int:
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    assert fib(60) == 1548008755920
