"""Тесты упражнения 5: зачем нужен ``functools.wraps``."""

from __future__ import annotations

import inspect

from pytutor.exercises.functools import ex05_wraps_identity as ex


def sample(a: int, b: int = 1) -> int:
    """Складывает два числа."""
    return a + b


def test_identity_decorator_calls_through() -> None:
    wrapped = ex.identity_decorator(sample)
    assert wrapped(2, 3) == 5


def test_identity_decorator_loses_metadata() -> None:
    wrapped = ex.identity_decorator(sample)
    assert wrapped.__name__ != "sample"
    assert wrapped.__doc__ != sample.__doc__
    assert not hasattr(wrapped, "__wrapped__")


def test_preserving_decorator_calls_through() -> None:
    wrapped = ex.preserving_decorator(sample)
    assert wrapped(2, 3) == 5


def test_preserving_decorator_keeps_metadata() -> None:
    wrapped = ex.preserving_decorator(sample)
    assert wrapped.__name__ == "sample"
    assert wrapped.__doc__ == "Складывает два числа."
    assert wrapped.__wrapped__ is sample


def test_preserving_decorator_keeps_signature() -> None:
    wrapped = ex.preserving_decorator(sample)
    assert inspect.signature(wrapped) == inspect.signature(sample)
