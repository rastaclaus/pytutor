"""Эталон упражнения 17: временные корзины: агрегация потоков событий."""

from __future__ import annotations

from collections import Counter, deque
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator


Event = tuple[int, str]  # (время, метка)


def bucket_size(events: Iterable[Event], bucket: int) -> Counter[int]:
    if bucket <= 0:
        raise ValueError("bucket должно быть > 0")
    result: Counter[int] = Counter()
    for timestamp, _ in events:
        if timestamp >= 0:
            result[timestamp // bucket] += 1
    return result


def bucket_labels(events: Iterable[Event], bucket: int) -> dict[int, list[str]]:
    if bucket <= 0:
        raise ValueError("bucket должно быть > 0")
    result: dict[int, list[str]] = {}
    for timestamp, label in events:
        if timestamp < 0:
            continue
        key = timestamp // bucket
        result.setdefault(key, []).append(label)
    return result


def top_labels_per_bucket(events: Iterable[Event], bucket: int) -> dict[int, list[tuple[str, int]]]:
    grouped = bucket_labels(events, bucket)
    return {
        key: sorted(counter.items(), key=lambda item: (-item[1], item[0]))[:3]
        for key, labels in grouped.items()
        for counter in [Counter(labels)]
    }


def stream_buckets(events: Iterable[Event], bucket: int, window: int) -> Iterator[Counter[int]]:
    if bucket <= 0 or window <= 0:
        raise ValueError("bucket и window должны быть > 0")
    active: Counter[int] = Counter()
    order: deque[int] = deque()
    for timestamp, _ in events:
        if timestamp < 0:
            continue
        key = timestamp // bucket
        active[key] += 1
        if key not in order:
            order.append(key)
        while len(order) > window:
            old = order.popleft()
            del active[old]
        yield Counter(active)
