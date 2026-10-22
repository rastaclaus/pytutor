"""Эталон упражнения 6: ``collections.ChainMap`` — слои конфигурации."""

from __future__ import annotations

from collections import ChainMap


def make_chain(defaults: dict[str, int], user: dict[str, int]) -> ChainMap[str, int]:
    return ChainMap(user, defaults)


def lookup_priority(cm: ChainMap[str, int], key: str) -> int | None:
    return cm.get(key)


def flatten_layers(cm: ChainMap[str, int]) -> dict[str, int]:
    return dict(cm)


def insert_layer(cm: ChainMap[str, int], updates: dict[str, int]) -> ChainMap[str, int]:
    return cm.new_child(updates)


def drop_first_layer(cm: ChainMap[str, int]) -> ChainMap[str, int]:
    return cm.parents


def write_through(cm: ChainMap[str, int], key: str, value: int) -> ChainMap[str, int]:
    cm[key] = value
    return cm
