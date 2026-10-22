"""Тесты упражнения 7: ``deque.rotate`` и кольцо."""

from __future__ import annotations

from collections import deque

from pytutor.exercises.collections import ex07_deque_rotate as ex


def test_rotate_right() -> None:
    assert ex.rotate_right([1, 2, 3, 4], 1) == [4, 1, 2, 3]
    assert ex.rotate_right([1, 2, 3, 4], 5) == [4, 1, 2, 3]
    assert ex.rotate_right([1, 2, 3, 4], 0) == [1, 2, 3, 4]
    assert ex.rotate_right([], 3) == []


def test_rotate_left() -> None:
    assert ex.rotate_left([1, 2, 3, 4], 1) == [2, 3, 4, 1]
    assert ex.rotate_left([1, 2, 3, 4], 5) == [2, 3, 4, 1]
    assert ex.rotate_left([], 3) == []


def test_next_after() -> None:
    assert ex.next_after(["a", "b", "c"], "b") == "c"
    assert ex.next_after(["a", "b", "c"], "c") == "a"
    assert ex.next_after(["a", "b", "c"], "x") is None


def test_remove_all() -> None:
    dq = deque([1, 2, 1, 3, 1])
    result = ex.remove_all(dq, 1)
    assert result is dq
    assert list(result) == [2, 3]


def test_rotate_until_first() -> None:
    dq = deque([3, 1, 2])
    result = ex.rotate_until_first(dq, 1)
    assert result is dq
    assert list(result) == [1, 2, 3]

    dq = deque([1, 2, 3])
    ex.rotate_until_first(dq, 99)
    assert list(dq) == [1, 2, 3]
