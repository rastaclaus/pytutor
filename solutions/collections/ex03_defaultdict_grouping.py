"""Эталон упражнения 3: ``collections.defaultdict`` — группировка."""

from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def group_by_key(pairs: Iterable[tuple[str, int]]) -> dict[str, list[int]]:
    result: defaultdict[str, list[int]] = defaultdict(list)
    for key, value in pairs:
        result[key].append(value)
    return dict(result)


def group_unique(pairs: Iterable[tuple[str, int]]) -> dict[str, set[int]]:
    result: defaultdict[str, set[int]] = defaultdict(set)
    for key, value in pairs:
        result[key].add(value)
    return dict(result)


def index_by_field(records: Iterable[tuple[str, str]], field: int) -> dict[str, list[tuple[str, str]]]:
    result: defaultdict[str, list[tuple[str, str]]] = defaultdict(list)
    for record in records:
        result[record[field]].append(record)
    return dict(result)


def invert_mapping(mapping: dict[str, int]) -> dict[int, list[str]]:
    result: defaultdict[int, list[str]] = defaultdict(list)
    for key, value in mapping.items():
        result[value].append(key)
    return dict(result)


def group_by_first_letter(words: Iterable[str]) -> dict[str, list[str]]:
    result: defaultdict[str, list[str]] = defaultdict(list)
    for word in words:
        if word:
            result[word[0]].append(word)
    return dict(result)
