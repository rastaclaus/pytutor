"""Тесты упражнения 2 (boss): агрегация потока событий."""

from __future__ import annotations

from collections import Counter

import pytest

from pytutor.exercises.boss import ex02_event_stream as ex


@pytest.fixture
def events():
    return [
        ("anna", "pickup", 0),
        ("anna", "deliver", 120),
        ("boris", "pickup", 0),
        ("anna", "cancel", 120),
        ("boris", "deliver", 200),
        ("anna", "deliver", 80),
    ]


def test_validate_event_ok() -> None:
    ex.validate_event(("anna", "deliver", 5))
    ex.validate_event(("bob", "pickup", 0))


def test_validate_event_unknown_type() -> None:
    with pytest.raises(ValueError, match="event_type"):
        ex.validate_event(("anna", "refunded", 5))


def test_courier_totals(events) -> None:
    totals = ex.courier_totals(events)
    assert totals == {"anna": 80, "boris": 200}
    assert list(totals) == ["anna", "boris"]  # порядок первого появления


def test_courier_totals_pickup_ignored() -> None:
    # Курьер только с ``pickup`` не попадает в результат вообще.
    assert ex.courier_totals([("anna", "pickup", 999)]) == {}


def test_events_by_type(events) -> None:
    counts = ex.events_by_type(events)
    assert counts == Counter({"deliver": 3, "pickup": 2, "cancel": 1})


def test_top_couriers(events) -> None:
    assert ex.top_couriers(events, 1) == [("boris", 200)]
    assert ex.top_couriers(events, 5) == [("boris", 200), ("anna", 80)]


def test_top_couriers_tie_alphabetical() -> None:
    tie = [("zoe", "deliver", 100), ("adam", "deliver", 100)]
    assert ex.top_couriers(tie, 2) == [("adam", 100), ("zoe", 100)]


def test_top_couriers_zero_limit(events) -> None:
    assert ex.top_couriers(events, 0) == []


def test_window_counts(events) -> None:
    # Последние 3 события: cancel, deliver, deliver
    counts = ex.window_counts(events, 3)
    assert counts == Counter({"deliver": 2, "cancel": 1})
    assert ex.window_counts(events, 2) == Counter({"deliver": 2})
    assert ex.window_counts(events, 100) == Counter({"deliver": 3, "pickup": 2, "cancel": 1})


def test_window_counts_rejects_bad_window(events) -> None:
    with pytest.raises(ValueError, match="window"):
        ex.window_counts(events, 0)


def test_busy_courier(events) -> None:
    assert ex.busy_courier(events) == "anna"  # 4 события против 2


def test_busy_courier_empty() -> None:
    assert ex.busy_courier([]) is None
