"""Тесты упражнения 17: временные корзины."""

from __future__ import annotations

from collections import Counter

import pytest

from pytutor.exercises.collections import ex17_event_buckets as ex


def test_bucket_size() -> None:
    events = [(0, "a"), (1, "b"), (10, "c"), (11, "d"), (20, "e")]
    assert ex.bucket_size(events, 10) == Counter({0: 2, 1: 2, 2: 1})
    assert ex.bucket_size([(-5, "x")], 10) == Counter()


def test_bucket_size_rejects_bad_bucket() -> None:
    with pytest.raises(ValueError, match="bucket"):
        ex.bucket_size([], 0)


def test_bucket_labels() -> None:
    events = [(0, "a"), (10, "b")]
    assert ex.bucket_labels(events, 10) == {0: ["a"], 1: ["b"]}


def test_top_labels_per_bucket() -> None:
    events = [
        (0, "x"),
        (0, "y"),
        (0, "x"),
        (10, "z"),
        (10, "z"),
    ]
    assert ex.top_labels_per_bucket(events, 10) == {
        0: [("x", 2), ("y", 1)],
        1: [("z", 2)],
    }


def test_stream_buckets() -> None:
    events = [(0, "a"), (5, "b"), (10, "c")]
    result = list(ex.stream_buckets(events, 10, 2))
    assert result == [
        Counter({0: 1}),
        Counter({0: 2}),
        Counter({0: 2, 1: 1}),
    ]


def test_stream_buckets_evicts_old() -> None:
    events = [(0, "a"), (10, "b"), (20, "c"), (30, "d")]
    result = list(ex.stream_buckets(events, 10, 2))
    assert result[-1] == Counter({2: 1, 3: 1})
    assert 0 not in result[-1]
