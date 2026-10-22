"""Тесты упражнения 2: ``deque`` — очередь и стек."""

from __future__ import annotations

from collections import deque

import pytest

from pytutor.exercises.collections import ex02_deque_basics as ex


def test_make_queue() -> None:
    dq = ex.make_queue([1, 2, 3])
    assert isinstance(dq, deque)
    assert list(dq) == [1, 2, 3]


def test_queue_push_pop() -> None:
    assert ex.queue_push_pop([1, 2], [3, 4]) == [1, 2, 3, 4]
    assert ex.queue_push_pop([], [5]) == [5]


def test_stack_push_pop() -> None:
    assert ex.stack_push_pop([1, 2], [3, 4]) == [4, 3, 2, 1]
    assert ex.stack_push_pop([], [5]) == [5]


def test_bounded_history() -> None:
    assert ex.bounded_history([1, 2, 3, 4], 2) == [3, 4]
    assert ex.bounded_history([1, 2], 5) == [1, 2]


def test_bounded_history_rejects_non_positive_maxlen() -> None:
    with pytest.raises(ValueError, match="maxlen"):
        ex.bounded_history([1], 0)


def test_add_with_limit() -> None:
    history = deque([1, 2], maxlen=2)
    result = ex.add_with_limit(history, 3, 2)
    assert result is history
    assert list(result) == [2, 3]

    history = deque(maxlen=2)
    ex.add_with_limit(history, 1, 2)
    ex.add_with_limit(history, 2, 2)
    ex.add_with_limit(history, 3, 2)
    assert list(history) == [2, 3]
