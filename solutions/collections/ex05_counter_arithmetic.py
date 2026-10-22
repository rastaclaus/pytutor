"""Эталон упражнения 5: арифметика ``Counter``."""

from __future__ import annotations

from collections import Counter


def combine(*counters: Counter[str]) -> Counter[str]:
    result: Counter[str] = Counter()
    for counter in counters:
        result += counter
    return result


def add_counts(left: Counter[str], right: Counter[str]) -> Counter[str]:
    return left + right


def difference_counts(left: Counter[str], right: Counter[str]) -> Counter[str]:
    return left - right


def overlap_counts(left: Counter[str], right: Counter[str]) -> Counter[str]:
    return left & right


def union_counts(left: Counter[str], right: Counter[str]) -> Counter[str]:
    return left | right


def subtract_inplace(left: Counter[str], right: Counter[str]) -> Counter[str]:
    left.subtract(right)
    return left


def merge_strategies(left: Counter[str], right: Counter[str], strategy: str) -> Counter[str]:
    if strategy == "add":
        return left + right
    if strategy == "max":
        return left | right
    if strategy == "min":
        return left & right
    if strategy == "sub":
        return left - right
    message = f"Неизвестная стратегия: {strategy}"
    raise ValueError(message)
