"""Тесты упражнения 10: ``tee``."""

from __future__ import annotations

from pytutor.exercises.itertools import ex10_tee as ex


def test_duplicate() -> None:
    assert ex.duplicate([1, 2, 3]) == ([1, 2, 3], [1, 2, 3])
    assert ex.duplicate([]) == ([], [])


def test_duplicate_reads_source_once() -> None:
    calls: list[int] = []

    def source() -> list[int]:
        for value in (1, 2, 3):
            calls.append(value)
            yield value

    left, right = ex.duplicate(source())
    assert left == [1, 2, 3]
    assert right == [1, 2, 3]
    assert calls == [1, 2, 3]


def test_peek() -> None:
    assert ex.peek(["a", "b"]) == ("a", ["a", "b"])
    assert ex.peek([]) == (None, [])


def test_split_by_predicate() -> None:
    assert ex.split_by_predicate([1, 2, 3, 4], lambda value: value % 2 == 0) == (
        [2, 4],
        [1, 3],
    )
    assert ex.split_by_predicate([], bool) == ([], [])


def test_count_calls_once() -> None:
    assert ex.count_calls_once([1, 2, 3]) == (6, 3)
    assert ex.count_calls_once([]) == (0, 0)


def test_first_and_last() -> None:
    assert ex.first_and_last(iter([5, 6, 7])) == (5, 7)
    assert ex.first_and_last([5]) == (5, 5)
    assert ex.first_and_last([]) is None


def test_lookahead_pairs() -> None:
    assert ex.lookahead_pairs([1, 2, 3]) == [(1, 2), (2, 3), (3, None)]
    assert ex.lookahead_pairs([1]) == [(1, None)]
    assert ex.lookahead_pairs([]) == []
