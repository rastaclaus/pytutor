"""Эталон упражнения 14: слияние ``ChainMap``: «плоский» словарь и отчёт."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections import ChainMap
    from collections.abc import Iterable


def flatten(cm: ChainMap[str, int]) -> dict[str, int]:
    return dict(cm)


def source_report(cm: ChainMap[str, int]) -> dict[str, int]:
    report: dict[str, int] = {}
    for i, layer in enumerate(cm.maps):
        for key in layer:
            if key not in report:
                report[key] = i
    return report


def conflict_keys(cm: ChainMap[str, int]) -> list[str]:
    seen: set[str] = set()
    conflicts: list[str] = []
    for layer in cm.maps:
        for key in layer:
            if key in seen and key not in conflicts:
                conflicts.append(key)
            seen.add(key)
    return conflicts


def update_all_layers(cm: ChainMap[str, int], key: str, value: int) -> ChainMap[str, int]:
    for layer in cm.maps:
        if key in layer:
            layer[key] = value
    return cm


def merged_from(layers: Iterable[dict[str, int]]) -> dict[str, int]:
    result: dict[str, int] = {}
    for layer in layers:
        result.update(layer)
    return result
