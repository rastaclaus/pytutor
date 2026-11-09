"""Эталон упражнения 2 (boss): агрегация потока событий."""

from __future__ import annotations

from collections import Counter, defaultdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable

EVENT_TYPES = frozenset({"pickup", "deliver", "cancel"})


def validate_event(event: tuple[str, str, int]) -> None:
    courier, event_type, amount = event
    if event_type not in EVENT_TYPES:
        msg = f"unknown event_type: {event_type!r} (courier={courier!r}, amount={amount!r})"
        raise ValueError(msg)


def courier_totals(events: Iterable[tuple[str, str, int]]) -> dict[str, int]:
    totals: defaultdict[str, int] = defaultdict(int)
    for courier, event_type, amount in events:
        if event_type == "deliver":
            totals[courier] += amount
        elif event_type == "cancel":
            totals[courier] -= amount
    return dict(totals)


def events_by_type(events: Iterable[tuple[str, str, int]]) -> Counter[str]:
    return Counter(event_type for _, event_type, _ in events)


def top_couriers(events: Iterable[tuple[str, str, int]], n: int) -> list[tuple[str, int]]:
    totals = courier_totals(events)
    ranked = sorted(totals.items(), key=lambda item: (-item[1], item[0]))
    return ranked[: max(n, 0)]


def window_counts(events: Iterable[tuple[str, str, int]], window: int) -> Counter[str]:
    if window < 1:
        msg = f"window must be >= 1, got {window}"
        raise ValueError(msg)
    tail = list(events)[-window:]
    return Counter(event_type for _, event_type, _ in tail)


def busy_courier(events: Iterable[tuple[str, str, int]]) -> str | None:
    counts: Counter[str] = Counter()
    for courier, _, _ in events:
        counts[courier] += 1
    if not counts:
        return None
    best = None
    for courier, count in counts.items():
        if best is None or count > counts[best]:
            best = courier
    return best
