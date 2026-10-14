"""Тесты упражнения 6: декораторы с аргументами."""

from __future__ import annotations

import pytest

from pytutor.exercises.functools import ex06_decorator_with_args as ex


def test_repeat_collects_results() -> None:
    counter = {"n": 0}

    @ex.repeat(3)
    def tick() -> int:
        counter["n"] += 1
        return counter["n"]

    assert tick() == [1, 2, 3]


def test_repeat_zero_times() -> None:
    @ex.repeat(0)
    def tick() -> int:
        return 1

    assert tick() == []


def test_repeat_preserves_metadata() -> None:
    @ex.repeat(2)
    def named() -> int:
        """Докстринг."""
        return 1

    assert named.__name__ == "named"
    assert named.__doc__ == "Докстринг."


def test_retry_succeeds_after_failures() -> None:
    attempts: list[int] = []

    @ex.retry(3)
    def flaky() -> str:
        attempts.append(1)
        if len(attempts) < 3:
            raise RuntimeError("ещё не время")
        return "ok"

    assert flaky() == "ok"
    assert len(attempts) == 3


def test_retry_exhausts_attempts() -> None:
    attempts: list[int] = []

    @ex.retry(2, exceptions=(ValueError,))
    def always_fails() -> None:
        attempts.append(1)
        raise ValueError("boom")

    with pytest.raises(ValueError):
        always_fails()
    assert len(attempts) == 2


def test_retry_does_not_catch_other_exceptions() -> None:
    attempts: list[int] = []

    @ex.retry(3, exceptions=(ValueError,))
    def wrong_error() -> None:
        attempts.append(1)
        raise KeyError("k")

    with pytest.raises(KeyError):
        wrong_error()
    # Не пойманное исключение пробрасывается сразу, без повторов.
    assert len(attempts) == 1


def test_retry_requires_positive_times() -> None:
    with pytest.raises(ValueError):
        ex.retry(0)
