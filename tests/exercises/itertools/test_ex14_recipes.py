"""Тесты упражнения 14: рецепты из документации."""

from __future__ import annotations

import pytest

from pytutor.exercises.itertools import ex14_recipes as ex


def test_sliding_window() -> None:
    assert ex.sliding_window("ABCDEFG", 3) == [
        ("A", "B", "C"),
        ("B", "C", "D"),
        ("C", "D", "E"),
        ("D", "E", "F"),
        ("E", "F", "G"),
    ]
    assert ex.sliding_window([1, 2], 3) == []
    assert ex.sliding_window([1], 1) == [(1,)]


def test_sliding_window_rejects_bad_size() -> None:
    with pytest.raises(ValueError, match="size"):
        ex.sliding_window([1], 0)


def test_running_mean() -> None:
    assert ex.running_mean([2, 4, 6]) == pytest.approx([2.0, 3.0, 4.0])
    assert ex.running_mean([]) == []


def test_sum_of_squares() -> None:
    assert ex.sum_of_squares([1, 2, 3]) == 14
    assert ex.sum_of_squares([]) == 0


def test_tail() -> None:
    assert ex.tail([1, 2, 3, 4], 2) == [3, 4]
    assert ex.tail([1, 2], 5) == [1, 2]
    assert ex.tail([1], 0) == []


def test_running_extremes() -> None:
    assert ex.running_extremes([3, 1, 4]) == [(3, 3), (1, 3), (1, 4)]
    assert ex.running_extremes([]) == []


def test_average_of_top() -> None:
    assert ex.average_of_top([1, 2, 3, 4], 2) == pytest.approx(3.5)
    assert ex.average_of_top([5], 3) == pytest.approx(5.0)


def test_average_of_top_empty() -> None:
    with pytest.raises(ValueError, match="пустой"):
        ex.average_of_top([], 2)


def test_moving_average() -> None:
    assert ex.moving_average([1.0, 2.0, 3.0], 2) == pytest.approx([1.5, 2.5])
    assert ex.moving_average([1.0], 2) == []
