"""Тесты упражнения 11: ``batched`` и рецепт ``grouper``."""

from __future__ import annotations

import pytest

from pytutor.exercises.itertools import ex11_batched_grouper as ex


def test_batch() -> None:
    assert ex.batch("ABCDEFG", 3) == [("A", "B", "C"), ("D", "E", "F"), ("G",)]
    assert ex.batch("", 3) == []
    assert ex.batch("AB", 3) == [("A", "B")]


def test_batch_rejects_non_positive_size() -> None:
    with pytest.raises(ValueError, match="at least one"):
        ex.batch("AB", 0)


def test_batch_strict() -> None:
    assert ex.batch_strict("ABCDEF", 3) == [("A", "B", "C"), ("D", "E", "F")]


def test_batch_strict_rejects_incomplete_tail() -> None:
    with pytest.raises(ValueError, match="incomplete batch"):
        ex.batch_strict("ABCDEFG", 3)


def test_batch_lengths() -> None:
    assert ex.batch_lengths("ABCDEFG", 3) == [3, 3, 1]
    assert ex.batch_lengths("", 3) == []


def test_pad_batches() -> None:
    assert ex.pad_batches("ABCDEFG", 3, "-") == [
        ("A", "B", "C"),
        ("D", "E", "F"),
        ("G", "-", "-"),
    ]
    assert ex.pad_batches("", 3, "-") == []


def test_trim_batches() -> None:
    assert ex.trim_batches("ABCDEFG", 3) == [("A", "B", "C"), ("D", "E", "F")]
    assert ex.trim_batches("AB", 3) == []


def test_reshape() -> None:
    assert ex.reshape([[0, 1], [2, 3], [4, 5]], 3) == [(0, 1, 2), (3, 4, 5)]
    # Неполная последняя строка отбрасывается.
    assert ex.reshape([[0, 1], [2, 3]], 3) == [(0, 1, 2)]
    assert ex.reshape([[0], [1]], 3) == []
    assert ex.reshape([], 3) == []
