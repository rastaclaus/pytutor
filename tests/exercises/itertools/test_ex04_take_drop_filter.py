"""Тесты упражнения 4: ``takewhile``/``dropwhile``/``filterfalse``/``compress``."""

from __future__ import annotations

from itertools import count

from pytutor.exercises.itertools import ex04_take_drop_filter as ex


def test_take_until_negative() -> None:
    assert ex.take_until_negative([1, 2, -1, 3]) == [1, 2]
    assert ex.take_until_negative([-1, 1]) == []
    assert ex.take_until_negative([]) == []


def test_skip_leading_zeros() -> None:
    assert ex.skip_leading_zeros([0, 0, 1, 0, 2]) == [1, 0, 2]
    assert ex.skip_leading_zeros([0, 0]) == []
    assert ex.skip_leading_zeros([1, 0]) == [1, 0]


def test_odd_numbers() -> None:
    assert ex.odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert ex.odd_numbers([]) == []


def test_falsey_only() -> None:
    assert ex.falsey_only([0, 1, None, 2, ""]) == [0, None, ""]


def test_select_by_mask() -> None:
    assert ex.select_by_mask("abcdef", [True, False, True, False, False, True]) == [
        "a",
        "c",
        "f",
    ]


def test_select_by_mask_stops_at_shorter_input() -> None:
    assert ex.select_by_mask("abcdef", [True, True]) == ["a", "b"]
    assert ex.select_by_mask("ab", [True, True, True]) == ["a", "b"]


def test_drop_while_shorter_than() -> None:
    words = ["a", "bb", "ccc", "d"]
    assert ex.drop_while_shorter_than(3, words) == ["ccc", "d"]
    assert ex.drop_while_shorter_than(3, ["a", "bb"]) == []


def test_count_taken_on_infinite_input() -> None:
    assert ex.count_taken(lambda value: value < 5, count()) == 5
    assert ex.count_taken(lambda value: value > 10, count()) == 0
