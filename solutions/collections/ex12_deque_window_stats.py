"""Эталон упражнения 12: скользящее окно: статистика в потоке."""

from __future__ import annotations

from collections import deque
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator


def moving_average(values: Iterable[float], size: int) -> Iterator[float]:
    if size <= 0:
        raise ValueError("size должно быть > 0")
    window: deque[float] = deque(maxlen=size)
    for value in values:
        window.append(value)
        if len(window) == size:
            yield sum(window) / size


def moving_max(values: Iterable[int], size: int) -> Iterator[int]:
    if size <= 0:
        raise ValueError("size должно быть > 0")
    window: deque[int] = deque(maxlen=size)
    for value in values:
        window.append(value)
        if len(window) == size:
            yield max(window)


def moving_min(values: Iterable[int], size: int) -> Iterator[int]:
    if size <= 0:
        raise ValueError("size должно быть > 0")
    window: deque[int] = deque(maxlen=size)
    for value in values:
        window.append(value)
        if len(window) == size:
            yield min(window)


def deviation_from_mean(values: Iterable[float], size: int) -> Iterator[float]:
    if size <= 0:
        raise ValueError("size должно быть > 0")
    window: deque[float] = deque(maxlen=size)
    for value in values:
        window.append(value)
        if len(window) == size:
            yield value - sum(window) / size
