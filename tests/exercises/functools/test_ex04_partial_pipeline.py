"""Тесты упражнения 4: ``compose``/``pipeline`` и ``partialmethod``."""

from __future__ import annotations

from pytutor.exercises.functools import ex04_partial_pipeline as ex


def _inc(x: int) -> int:
    return x + 1


def _double(x: int) -> int:
    return x * 2


def _negate(x: int) -> int:
    return -x


def test_compose_right_to_left() -> None:
    combined = ex.compose(_inc, _double)
    # inc(double(3)) = inc(6) = 7
    assert combined(3) == 7


def test_pipeline_left_to_right() -> None:
    combined = ex.pipeline(_inc, _double)
    # double(inc(3)) = double(4) = 8
    assert combined(3) == 8


def test_identity_when_empty() -> None:
    assert ex.compose()(5) == 5
    assert ex.pipeline()(5) == 5


def test_single_function() -> None:
    assert ex.compose(_negate)(4) == -4
    assert ex.pipeline(_negate)(4) == -4


def test_make_validator() -> None:
    not_empty = ex.make_validator(min_len=1)
    assert not_empty("ok") is True
    assert not_empty("") is False

    bounded = ex.make_validator(min_len=2, max_len=4)
    assert bounded("ab") is True
    assert bounded("abcd") is True
    assert bounded("a") is False
    assert bounded("abcde") is False


def test_logger_levels() -> None:
    logger = ex.Logger("app")
    assert logger.log("started") == "INFO: app started"
    assert logger.warn("careful") == "WARN: app careful"  # noqa: G010 — тестируем именно метод `warn`
    assert logger.debug("details") == "DEBUG: app details"
    assert logger.messages == [
        "INFO: app started",
        "WARN: app careful",
        "DEBUG: app details",
    ]
