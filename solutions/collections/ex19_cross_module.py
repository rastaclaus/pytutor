"""Эталон упражнения 19: кросс-наборная связка: collections × itertools × functools."""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from functools import partial
from itertools import batched, count, groupby
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator


def count_by_value(values: Iterable[int]) -> Counter[int]:
    return Counter(values)


def aggregate_runs(values: Iterable[str]) -> list[tuple[str, int]]:
    return [(key, len(list(group))) for key, group in groupby(values)]


def chunk_frequencies(values: Iterable[int], size: int) -> list[Counter[int]]:
    return [Counter(chunk) for chunk in batched(values, size)]


def make_incrementing_counter(start: int, step: int) -> Counter[str]:
    items = count(start, step)
    return defaultdict(partial(next, items))


def tail_stream(values: Iterable[int], size: int) -> Iterator[list[int]]:
    window: deque[int] = deque(maxlen=size)
    for value in values:
        window.append(value)
        yield list(window)
