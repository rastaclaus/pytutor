"""Тесты упражнения 15: ленивый ETL."""

from __future__ import annotations

from collections.abc import Iterator

import pytest

from pytutor.exercises.itertools import ex15_capstone as ex

LOG = [
    "INFO,ann,10",
    "WARN,bob,5",
    "INFO,ann,1",
    "битая строка",
    "INFO,ann,abc",
    "DEBUG,bob,2",
]


def test_parse_line() -> None:
    assert ex.parse_line("INFO,ann,10") == ("INFO", "ann", 10)
    assert ex.parse_line(" WARN , bob , 5 ") == ("WARN", "bob", 5)


def test_parse_line_rejects_broken() -> None:
    with pytest.raises(ValueError, match="values to unpack"):
        ex.parse_line("нет запятых")
    with pytest.raises(ValueError, match="invalid literal"):
        ex.parse_line("INFO,ann,abc")


def test_valid_records_is_lazy() -> None:
    stream = ex.valid_records(LOG)
    assert isinstance(stream, Iterator)
    assert next(stream) == ("INFO", "ann", 10)


def test_valid_records_skips_broken() -> None:
    assert list(ex.valid_records(LOG)) == [
        ("INFO", "ann", 10),
        ("WARN", "bob", 5),
        ("INFO", "ann", 1),
        ("DEBUG", "bob", 2),
    ]


def test_totals_by_user_is_lazy() -> None:
    records = ex.valid_records(LOG)
    assert next(iter(ex.totals_by_user(records))) == ("ann", 10)


def test_batch_totals() -> None:
    records = list(ex.valid_records(LOG))
    assert ex.batch_totals(records, 2) == [(10, 5), (1, 2)]
    assert ex.batch_totals([], 2) == []


def test_top_users() -> None:
    assert ex.top_users(LOG, 2) == [("ann", 11), ("bob", 7)]
    assert ex.top_users(LOG, 1) == [("ann", 11)]
    assert ex.top_users(LOG, 0) == []


def test_summarise() -> None:
    assert ex.summarise(LOG) == (4, 18, "INFO")
    assert ex.summarise([]) == (0, 0, None)


def test_process() -> None:
    assert ex.process(LOG, 2) == [(0, 15), (1, 3)]
    assert ex.process(LOG, 10) == [(0, 18)]


def test_pipeline_does_not_consume_before_iteration() -> None:
    consumed: list[str] = []

    def source() -> Iterator[str]:
        for line in LOG:
            consumed.append(line)
            yield line

    stream = ex.valid_records(source())
    assert consumed == []
    assert next(stream) == ("INFO", "ann", 10)
    assert consumed == ["INFO,ann,10"]


def test_top_users_with_limit_zero() -> None:
    assert ex.top_users(count_lines(3), 0) == []


def count_lines(n: int) -> Iterator[str]:
    for index in range(n):
        yield f"INFO,user{index},{index + 1}"


def test_top_users_with_prefix_sum() -> None:
    assert ex.top_users(count_lines(3), 10) == [
        ("user2", 3),
        ("user1", 2),
        ("user0", 1),
    ]
