"""Тесты упражнения 4 (boss): дневной отчёт ресторана."""

from __future__ import annotations

from collections import defaultdict

import pytest

from pytutor.exercises.boss import ex04_day_report as ex

LOG = [
    "anna;deliver;120",
    "boris;pickup;0",
    "anna;cancel;120",
    "boris;deliver;200",
    "broken",
    "carl;deliver;30",
]

ORDERS = [
    "A1;roll;120;2",
    "A1;tea;50;1",
    "A2;pizza;400;1",
    "broken;line",
    "A3;roll;120;1",
]


def test_parse_orders_groups_by_id() -> None:
    orders = ex.parse_orders(ORDERS)
    assert len(orders) == 3
    first = orders[0]
    assert first.order_id == "A1"
    assert len(first.items) == 2
    assert first.total() == 290


def test_parse_orders_skips_broken() -> None:
    orders = ex.parse_orders(["A1;roll;120;2", "nope", "A2;x;y;1"])
    assert len(orders) == 1


def test_best_order() -> None:
    orders = ex.parse_orders(ORDERS)
    assert ex.best_order(orders).order_id == "A2"


def test_best_order_empty() -> None:
    assert ex.best_order([]) is None


def test_hour_buckets() -> None:
    orders = ex.parse_orders(ORDERS)
    buckets = ex.hour_buckets(orders, 2)
    assert isinstance(buckets, defaultdict)
    assert buckets == {0: 290 + 400, 1: 120}


def test_hour_buckets_rejects_bad_size() -> None:
    with pytest.raises(ValueError, match="bucket_size"):
        ex.hour_buckets([], 0)


def test_top_dishes() -> None:
    orders = ex.parse_orders(ORDERS)
    assert ex.top_dishes(orders, 2) == [("roll", 3), ("pizza", 1)]


def test_top_dishes_tie_alphabetical() -> None:
    orders = ex.parse_orders(["A1;tea;50;1", "A2;cake;60;1"])
    assert ex.top_dishes(orders, 5) == [("cake", 1), ("tea", 1)]


def test_day_report() -> None:
    report = ex.day_report(LOG, ORDERS, 2)
    assert report["revenue"] == 350  # 120 + 200 + 30, без cancel и pickup
    assert report["best_order"] == "A2"
    assert report["top_dishes"] == [("roll", 3), ("pizza", 1)]
