"""Тесты упражнения 7: ``zip_longest`` и ``zip(strict=True)``."""

from __future__ import annotations

import pytest

from pytutor.exercises.itertools import ex07_zip_longest_strict as ex


def test_merge_uneven() -> None:
    assert ex.merge_uneven("ABC", [1, 2]) == [("A", 1), ("B", 2), ("C", None)]
    assert ex.merge_uneven("", []) == []


def test_merge_with_fill() -> None:
    assert ex.merge_with_fill("AB", [1, 2, 3], 0) == [("A", 1), ("B", 2), (0, 3)]
    assert ex.merge_with_fill("ABC", [1], -1) == [("A", 1), ("B", -1), ("C", -1)]


def test_zip_strict_equal_lengths() -> None:
    assert ex.zip_strict([1, 2], [3, 4]) == [(1, 3), (2, 4)]
    assert ex.zip_strict([], []) == []


def test_zip_strict_raises_on_mismatch() -> None:
    with pytest.raises(ValueError, match="shorter"):
        ex.zip_strict([1, 2], [3])


def test_same_length() -> None:
    assert ex.same_length([1, 2], [3, 4]) is True
    with pytest.raises(ValueError, match="shorter"):
        ex.same_length([1, 2], [3])


def test_grouper() -> None:
    assert ex.grouper("ABCDEFG", 3) == [
        ("A", "B", "C"),
        ("D", "E", "F"),
        ("G", "", ""),
    ]
    assert ex.grouper("", 2) == []
    assert ex.grouper("AB", 2) == [("A", "B")]


def test_grouper_rejects_zero_size() -> None:
    with pytest.raises(ValueError, match="size"):
        ex.grouper("AB", 0)


def test_transpose() -> None:
    assert ex.transpose([[1, 2, 3], [4, 5, 6]]) == [(1, 4), (2, 5), (3, 6)]
    assert ex.transpose([]) == []


def test_transpose_rejects_ragged_matrix() -> None:
    with pytest.raises(ValueError, match="zip"):
        ex.transpose([[1, 2], [3]])
