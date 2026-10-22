"""Тесты упражнения 1: ``count``, ``repeat``, ``cycle``."""

from __future__ import annotations

from itertools import count

from pytutor.exercises.itertools import ex01_count_repeat_cycle as ex


def test_take_from_infinite_count() -> None:
    assert ex.take(4, count()) == [0, 1, 2, 3]
    assert ex.take(3, count(10, 5)) == [10, 15, 20]


def test_take_with_non_positive_n() -> None:
    assert ex.take(0, count()) == []
    assert ex.take(-2, count()) == []


def test_take_stops_at_short_iterable() -> None:
    assert ex.take(5, [1, 2]) == [1, 2]


def test_countdown() -> None:
    assert ex.countdown(5, 3) == [5, 4, 3]
    assert ex.countdown(-1, 4) == [-1, -2, -3, -4]
    assert ex.countdown(5, 0) == []


def test_repeat_value() -> None:
    assert ex.repeat_value("x", 3) == ["x", "x", "x"]
    assert ex.repeat_value("x", 0) == []


def test_cycle_values() -> None:
    assert ex.cycle_values(["a", "b"], 5) == ["a", "b", "a", "b", "a"]
    # По пустому входу cycle сразу заканчивается, хотя и «бесконечен».
    assert ex.cycle_values([], 3) == []


def test_numbered() -> None:
    assert ex.numbered(["a", "b"]) == [(0, "a"), (1, "b")]
    assert ex.numbered([]) == []
    assert ex.numbered(iter(["z"])) == [(0, "z")]
