"""Тесты упражнения 19: кросс-наборная связка."""

from __future__ import annotations

from collections import Counter

from pytutor.exercises.collections import ex19_cross_module as ex


def test_count_by_value() -> None:
    assert ex.count_by_value([1, 2, 1, 3, 1]) == Counter({1: 3, 2: 1, 3: 1})


def test_aggregate_runs() -> None:
    assert ex.aggregate_runs("aaabbc") == [("a", 3), ("b", 2), ("c", 1)]
    assert ex.aggregate_runs("") == []


def test_chunk_frequencies() -> None:
    assert ex.chunk_frequencies([1, 1, 2, 3, 3, 3], 2) == [
        Counter({1: 2}),
        Counter({2: 1, 3: 1}),
        Counter({3: 2}),
    ]


def test_make_incrementing_counter() -> None:
    counter = ex.make_incrementing_counter(10, 5)
    assert counter["x"] == 10
    assert counter["y"] == 15
    assert counter["x"] == 10
    assert counter["z"] == 20


def test_tail_stream() -> None:
    assert list(ex.tail_stream([1, 2, 3], 2)) == [[1], [1, 2], [2, 3]]
    assert list(ex.tail_stream([1], 5)) == [[1]]
