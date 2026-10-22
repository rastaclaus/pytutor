"""Эталон упражнения 8: вложенные ``defaultdict`` — автосоздание уровней."""

from __future__ import annotations

from collections import Counter, defaultdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def nested_defaultdict() -> defaultdict:
    return defaultdict(lambda: defaultdict(list))


def add_path(tree: defaultdict, path: list[str], value: int) -> defaultdict:
    node = tree
    for key in path[:-1]:
        node = node[key]
    last = path[-1]
    if last not in node:
        node[last] = []
    node[last].append(value)
    return tree


def get_path(tree: defaultdict, path: list[str], default: int | None = None) -> list[int] | None:
    node = tree
    for key in path:
        if key not in node:
            return default
        node = node[key]
    return node


def build_counts(words: Iterable[str]) -> defaultdict:
    result: defaultdict = defaultdict(Counter)
    for word in words:
        for letter in word:
            result[len(word)][letter] += 1
    return result


def merge_trees(left: defaultdict, right: defaultdict) -> defaultdict:
    result = nested_defaultdict()
    for key in set(left) | set(right):
        left_value = left.get(key)
        right_value = right.get(key)
        if isinstance(left_value, dict) and isinstance(right_value, dict):
            result[key] = merge_trees(left_value, right_value)
        elif left_value is None:
            result[key] = right_value
        elif right_value is None:
            result[key] = left_value
        else:
            result[key] = list(left_value) + list(right_value)
    return result
