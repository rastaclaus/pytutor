"""Тесты упражнения 8: ``pairwise`` и скользящее окно."""

from __future__ import annotations

from collections.abc import Iterator
from itertools import count

import pytest

from pytutor.exercises.itertools import ex08_pairwise_window as ex


def test_adjacent_pairs() -> None:
    assert ex.adjacent_pairs("ABC") == [("A", "B"), ("B", "C")]
    assert ex.adjacent_pairs("A") == []
    assert ex.adjacent_pairs("") == []


def test_differences() -> None:
    assert ex.differences([1, 4, 9]) == [3, 5]
    assert ex.differences([5]) == []


def test_all_increasing() -> None:
    assert ex.all_increasing([1, 2, 3]) is True
    assert ex.all_increasing([1, 1, 2]) is False
    assert ex.all_increasing([3, 2]) is False
    assert ex.all_increasing([]) is True
    assert ex.all_increasing([7]) is True


def test_sliding_window() -> None:
    assert ex.sliding_window("ABCDEFG", 3) == [
        ("A", "B", "C"),
        ("B", "C", "D"),
        ("C", "D", "E"),
        ("D", "E", "F"),
        ("E", "F", "G"),
    ]
    assert ex.sliding_window([1, 2], 3) == []
    assert ex.sliding_window([1, 2, 3], 1) == [(1,), (2,), (3,)]


def test_sliding_window_rejects_non_positive_size() -> None:
    with pytest.raises(ValueError, match="size"):
        ex.sliding_window([1], 0)


def test_tail() -> None:
    assert ex.tail([1, 2, 3, 4], 2) == [3, 4]
    assert ex.tail([1, 2], 5) == [1, 2]
    assert ex.tail([1, 2], 0) == []


def test_tail_does_not_require_materialisation() -> None:
    assert ex.tail(iter([1, 2, 3, 4]), 3) == [2, 3, 4]


def test_window_sums() -> None:
    assert ex.window_sums([1, 2, 3, 4], 2) == [3, 5, 7]
    assert ex.window_sums([1], 2) == []


def test_pairwise_iter_is_lazy() -> None:
    result = ex.pairwise_iter(count())
    assert isinstance(result, Iterator)
    assert [next(result) for _ in range(2)] == [(0, 1), (1, 2)]


def test_first_window_above() -> None:
    assert ex.first_window_above([1, 2, 3, 4], 2, 6) == (3, 4)
    assert ex.first_window_above([1, 2, 3], 2, 100) is None
