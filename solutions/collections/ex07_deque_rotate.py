"""Эталон упражнения 7: ``deque.rotate`` и превращение списка в кольцо."""

from __future__ import annotations

from collections import deque


def rotate_right(items: list[int], n: int) -> list[int]:
    if not items:
        return []
    dq = deque(items)
    dq.rotate(n % len(dq))
    return list(dq)


def rotate_left(items: list[int], n: int) -> list[int]:
    if not items:
        return []
    dq = deque(items)
    dq.rotate(-(n % len(dq)))
    return list(dq)


def next_after(items: list[str], current: str) -> str | None:
    if current not in items:
        return None
    dq = deque(items)
    dq.rotate(-(dq.index(current) + 1))
    return dq[0]


def remove_all(dq: deque[int], value: int) -> deque[int]:
    while value in dq:
        dq.remove(value)
    return dq


def rotate_until_first(dq: deque[int], value: int) -> deque[int]:
    if value not in dq:
        return dq
    dq.rotate(-dq.index(value))
    return dq
