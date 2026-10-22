"""Эталон упражнения 15: ленивый ETL на ``itertools``."""

from __future__ import annotations

from itertools import batched
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator

Record = tuple[str, str, int]


def parse_line(raw: str) -> Record:
    level, user, amount = raw.split(",")
    return level.strip(), user.strip(), int(amount)


def valid_records(lines: Iterable[str]) -> Iterator[Record]:
    for line in lines:
        try:
            yield parse_line(line)
        except ValueError:
            continue


def totals_by_user(records: Iterable[Record]) -> Iterator[tuple[str, int]]:
    for _level, user, amount in records:
        yield user, amount


def batch_totals(records: Iterable[Record], size: int) -> list[tuple[int, ...]]:
    return [tuple(amount for _level, _user, amount in batch) for batch in batched(records, size)]


def top_users(lines: Iterable[str], limit: int) -> list[tuple[str, int]]:
    totals: dict[str, int] = {}
    for user, amount in totals_by_user(valid_records(lines)):
        totals[user] = totals.get(user, 0) + amount
    ordered = sorted(totals.items(), key=lambda item: (-item[1], item[0]))
    return ordered[: max(limit, 0)]


def summarise(lines: Iterable[str]) -> tuple[int, int, str | None]:
    count = 0
    total = 0
    levels: dict[str, int] = {}
    for level, _user, amount in valid_records(lines):
        count += 1
        total += amount
        levels[level] = levels.get(level, 0) + 1
    if not levels:
        return 0, 0, None
    most_common = max(levels.items(), key=lambda item: item[1])
    return count, total, most_common[0]


def process(lines: Iterable[str], batch_size: int) -> list[tuple[int, int]]:
    result = []
    for index, batch in enumerate(batched(valid_records(lines), batch_size)):
        result.append((index, sum(amount for _level, _user, amount in batch)))
    return result
