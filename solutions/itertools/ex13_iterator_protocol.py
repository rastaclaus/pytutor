"""Эталон упражнения 13: протокол итератора."""

from __future__ import annotations

from itertools import count
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable, Iterator


def exhaust(values: Iterable[int]) -> tuple[list[int], list[int]]:
    return list(values), list(values)


def materialise(values: Iterable[int]) -> tuple[list[int], list[int]]:
    saved = list(values)
    return list(saved), list(saved)


def is_iterator(value: object) -> bool:
    return iter(value) is value if hasattr(value, "__iter__") else False


def read_until_sentinel(read: Callable[[], int], sentinel: int) -> list[int]:
    return list(iter(read, sentinel))


def lazy_map_side_effects(values: Iterable[int], seen: list[int]) -> tuple[Iterator[int], list[int]]:
    def doubled() -> Iterator[int]:
        for value in values:
            seen.append(value)
            yield value * 2

    return doubled(), seen


def count_until_limit(limit: int, seen: list[int]) -> int:
    total = 0
    last = 0
    for value in count(1):
        total += value
        seen.append(value)
        last = value
        if total > limit:
            break
    return last
