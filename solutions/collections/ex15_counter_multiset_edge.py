"""Эталон упражнения 15: крайние случаи ``Counter``: мультимножество."""

from __future__ import annotations

from collections import Counter


def nonzero_items(counter: Counter[str]) -> Counter[str]:
    return Counter({key: count for key, count in counter.items() if count > 0})


def keys_with_positive_count(counter: Counter[str]) -> list[str]:
    return [key for key, count in counter.items() if count > 0]


def is_submultiset(left: Counter[str], right: Counter[str]) -> bool:
    return all(left[key] <= right[key] for key in left if left[key] > 0)


def symmetric_difference(left: Counter[str], right: Counter[str]) -> Counter[str]:
    keys = set(left) | set(right)
    result: Counter[str] = Counter()
    for key in keys:
        diff = abs(left[key] - right[key])
        if diff > 0:
            result[key] = diff
    return result


def normalize(counter: Counter[str]) -> Counter[str]:
    return Counter({key: count for key, count in sorted(counter.items()) if count > 0})
