"""Тесты упражнения 3 (boss): ленивый конвейер обработки логов."""

from __future__ import annotations

import pytest

from pytutor.exercises.boss import ex03_lazy_pipeline as ex

GOOD = ["anna;deliver;120", "boris;pickup;0", "anna;cancel;120", "boris;deliver;200"]


def test_parse_line_ok() -> None:
    assert ex.parse_line("anna;deliver;120") == ("anna", "deliver", 120)
    assert ex.parse_line("bob;pickup;0") == ("bob", "pickup", 0)


def test_parse_line_bad_amount() -> None:
    with pytest.raises(ValueError):
        ex.parse_line("anna;deliver;abc")


def test_valid_lines_skips_bad() -> None:
    lines = [*GOOD, "broken", "carl;deliver;x", "dana;refund;5", "carl;deliver;50"]
    records = list(ex.valid_lines(lines))
    assert records == [
        ("anna", "deliver", 120),
        ("boris", "pickup", 0),
        ("anna", "cancel", 120),
        ("boris", "deliver", 200),
        ("carl", "deliver", 50),
    ]


def test_valid_lines_is_lazy() -> None:
    calls: list[str] = []

    def source():
        for line in ("anna;deliver;1", "boris;deliver;2"):
            calls.append(line)
            yield line

    result = ex.valid_lines(source())
    assert len(calls) == 0
    next(result)
    assert calls == ["anna;deliver;1"]


def test_deliveries_only() -> None:
    records = [("anna", "deliver", 10), ("boris", "pickup", 0), ("anna", "deliver", 5)]
    assert list(ex.deliveries_only(records)) == [
        ("anna", "deliver", 10),
        ("anna", "deliver", 5),
    ]


def test_amounts() -> None:
    records = [("a", "deliver", 10), ("b", "cancel", 3)]
    assert list(ex.amounts(records)) == [10, 3]


def test_batch_amounts() -> None:
    records = [("a", "deliver", n) for n in (1, 2, 3, 4, 5)]
    assert list(ex.batch_amounts(records, 2)) == [(1, 2), (3, 4), (5,)]


def test_batch_amounts_rejects_bad_size() -> None:
    with pytest.raises(ValueError, match="size"):
        list(ex.batch_amounts([], 0))


def test_largest_batch() -> None:
    lines = [
        "a;deliver;10",
        "b;deliver;20",
        "c;deliver;1",
        "d;deliver;2",
    ]
    assert ex.largest_batch(lines, 2) == 30


def test_largest_batch_empty() -> None:
    assert ex.largest_batch([], 3) == 0


def test_line_stats_one_pass() -> None:
    lines = [*GOOD, "broken", "carl;deliver;50"]
    stats = ex.line_stats(lines)
    assert stats == {"valid": 5, "skipped": 1, "total": 370}


def test_line_stats_empty() -> None:
    assert ex.line_stats([]) == {"valid": 0, "skipped": 0, "total": 0}
