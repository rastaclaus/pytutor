"""Эталон упражнения 3 (boss): ленивый конвейер обработки логов."""

from __future__ import annotations

from itertools import batched
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator

_EVENT_TYPES = frozenset({"pickup", "deliver", "cancel"})


def parse_line(raw: str) -> tuple[str, str, int]:
    courier, event, amount = raw.split(";")
    return courier, event, int(amount)


def _try_parse(raw: str) -> tuple[str, str, int] | None:
    try:
        record = parse_line(raw)
    except ValueError, TypeError:
        return None
    if record[1] not in _EVENT_TYPES:
        return None
    return record


def valid_lines(lines: Iterable[str]) -> Iterator[tuple[str, str, int]]:
    return (record for line in lines if (record := _try_parse(line)) is not None)


def deliveries_only(
    records: Iterable[tuple[str, str, int]],
) -> Iterator[tuple[str, str, int]]:
    return (record for record in records if record[1] == "deliver")


def amounts(records: Iterable[tuple[str, str, int]]) -> Iterator[int]:
    return (amount for _, _, amount in records)


def batch_amounts(records: Iterable[tuple[str, str, int]], size: int) -> Iterator[tuple[int, ...]]:
    if size < 1:
        msg = f"size must be >= 1, got {size}"
        raise ValueError(msg)
    return batched(amounts(records), size)


def largest_batch(lines: Iterable[str], size: int) -> int:
    return max((sum(batch) for batch in batch_amounts(valid_lines(lines), size)), default=0)


def line_stats(lines: Iterable[str]) -> dict[str, int]:
    stats = {"valid": 0, "skipped": 0, "total": 0}
    for raw in lines:
        record = _try_parse(raw)
        if record is None:
            stats["skipped"] += 1
            continue
        stats["valid"] += 1
        if record[1] == "deliver":
            stats["total"] += record[2]
    return stats
