"""Эталон упражнения 3: ``islice``."""

from __future__ import annotations

from itertools import islice
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator


def head(n: int, iterable: Iterable[int]) -> list[int]:
    return list(islice(iterable, n))


def drop_first(n: int, iterable: Iterable[int]) -> list[int]:
    return list(islice(iterable, n, None))


def every_nth(n: int, iterable: Iterable[int]) -> list[int]:
    if n <= 0:
        raise ValueError("n должно быть > 0")
    return list(islice(iterable, 0, None, n))


def nth(iterable: Iterable[int], index: int, default: int | None = None) -> int | None:
    if index < 0:
        raise ValueError("index должен быть >= 0")
    return next(islice(iterable, index, None), default)


def first_three(iterable: Iterable[int]) -> Iterator[int]:
    return islice(iterable, 3)
