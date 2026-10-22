"""Эталон упражнения 2: ``chain``."""

from __future__ import annotations

from itertools import chain, islice
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def flatten(nested: Iterable[Iterable[int]]) -> list[int]:
    return list(chain.from_iterable(nested))


def concat(*iterables: Iterable[str]) -> list[str]:
    return list(chain(*iterables))


def words_of(lines: Iterable[str]) -> list[str]:
    return list(chain.from_iterable(line.split() for line in lines))


def take_flattened(nested: Iterable[Iterable[int]], n: int) -> list[int]:
    return list(islice(chain.from_iterable(nested), n))
