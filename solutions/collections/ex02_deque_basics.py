"""Эталон упражнения 2: ``collections.deque`` — очередь и стек."""

from __future__ import annotations

from collections import deque
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def make_queue(initial: Iterable[int]) -> deque[int]:
    return deque(initial)


def queue_push_pop(initial: Iterable[int], values: list[int]) -> list[int]:
    dq = deque(initial)
    dq.extend(values)
    return [dq.popleft() for _ in range(len(dq))]


def stack_push_pop(initial: Iterable[int], values: list[int]) -> list[int]:
    dq = deque(initial)
    dq.extend(values)
    return [dq.pop() for _ in range(len(dq))]


def bounded_history(values: Iterable[int], maxlen: int) -> list[int]:
    if maxlen <= 0:
        raise ValueError("maxlen должно быть > 0")
    return list(deque(values, maxlen=maxlen))


def add_with_limit(history: deque[int], value: int, maxlen: int) -> deque[int]:
    history.append(value)
    while len(history) > maxlen:
        history.popleft()
    return history
