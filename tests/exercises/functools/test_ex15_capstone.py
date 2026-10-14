"""Тесты упражнения 15: капстоун-конвейер на ``functools``."""

from __future__ import annotations

import functools

import pytest

from pytutor.exercises.functools import ex15_capstone as ex


def test_parse_measurement() -> None:
    assert ex.parse_measurement("  10 ") == 10
    assert ex.parse_measurement("-3") == -3


def test_parse_measurement_is_cached() -> None:
    ex.parse_measurement.cache_clear()
    assert ex.parse_measurement("7") == 7
    assert ex.parse_measurement("7") == 7
    assert ex.parse_measurement.cache_info().hits == 1


def test_pipeline_order() -> None:
    combined = ex.pipeline(lambda x: x + 1, lambda x: x * 2)
    assert combined(3) == 8  # (3 + 1) * 2


def test_make_scaler() -> None:
    scaler = ex.make_scaler(2, 1)
    assert scaler(5) == 11
    assert ex.make_scaler(3)(4) == 12


def test_scale_value_does_not_mutate() -> None:
    row = {"cat": "a", "value": 5}
    scaled = ex.scale_value(row, ex.make_scaler(2, 1))
    assert scaled == {"cat": "a", "value": 11}
    assert row == {"cat": "a", "value": 5}


def test_aggregate_by_category() -> None:
    rows = [
        {"cat": "a", "value": 1},
        {"cat": "b", "value": 2},
        {"cat": "a", "value": 3},
    ]
    assert ex.aggregate_by_category(rows) == {"a": 4, "b": 2}
    assert ex.aggregate_by_category([]) == {}


def test_retry_recovers() -> None:
    attempts: list[int] = []

    @ex.retry(3)
    def flaky() -> str:
        attempts.append(1)
        if len(attempts) < 2:
            raise RuntimeError("ещё нет")
        return "ok"

    assert flaky() == "ok"
    assert len(attempts) == 2


def test_retry_exhausts() -> None:
    attempts: list[int] = []

    @ex.retry(2, exceptions=(ValueError,))
    def always_fails() -> None:
        attempts.append(1)
        raise ValueError("boom")

    with pytest.raises(ValueError):
        always_fails()
    assert len(attempts) == 2


def test_end_to_end_pipeline() -> None:
    rows = [
        {"cat": "a", "raw": "10"},
        {"cat": "b", "raw": "5"},
        {"cat": "a", "raw": "7"},
    ]
    parse = lambda row: {**row, "value": ex.parse_measurement(row["raw"])}
    scale = functools.partial(ex.scale_value, scaler=ex.make_scaler(2, 1))
    process = ex.pipeline(parse, scale)

    processed = [process(row) for row in rows]
    assert processed == [
        {"cat": "a", "raw": "10", "value": 21},
        {"cat": "b", "raw": "5", "value": 11},
        {"cat": "a", "raw": "7", "value": 15},
    ]
    assert ex.aggregate_by_category(processed) == {"a": 36, "b": 11}
