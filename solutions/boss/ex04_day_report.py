"""Эталон упражнения 4 (boss): дневной отчёт ресторана."""

from __future__ import annotations

from collections import Counter, defaultdict
from typing import TYPE_CHECKING

from pytutor.exercises.boss.ex01_courier_models import declare_models

if TYPE_CHECKING:
    from collections.abc import Iterable

_EVENT_TYPES = frozenset({"pickup", "deliver", "cancel"})


def _parse_log(raw: str) -> tuple[str, str, int] | None:
    try:
        courier, event, amount = raw.split(";")
        amount_value = int(amount)
    except ValueError, TypeError:
        return None
    if event not in _EVENT_TYPES:
        return None
    return courier, event, amount_value


def parse_orders(raw_orders: Iterable[str]) -> list[object]:
    dish_cls, order_cls = declare_models()
    orders: dict[str, object] = {}
    for raw in raw_orders:
        try:
            order_id, sku, price, qty = raw.split(";")
            price_value = int(price)
            qty_value = int(qty)
        except ValueError, TypeError:
            continue
        order = orders.setdefault(order_id, order_cls(order_id))
        order.items.append(dish_cls(sku, price_value, qty_value))  # type: ignore[attr-defined]
    return list(orders.values())


def best_order(orders: list[object]) -> object | None:
    best = None
    best_total = -1
    for order in orders:
        if order.total() > best_total:  # type: ignore[attr-defined]
            best = order
            best_total = order.total()  # type: ignore[attr-defined]
    return best


def hour_buckets(orders: list[object], bucket_size: int) -> defaultdict[int, int]:
    if bucket_size < 1:
        msg = f"bucket_size must be >= 1, got {bucket_size}"
        raise ValueError(msg)
    buckets: defaultdict[int, int] = defaultdict(int)
    for index, order in enumerate(orders):
        buckets[index // bucket_size] += order.total()  # type: ignore[attr-defined]
    return buckets


def top_dishes(orders: list[object], n: int) -> list[tuple[str, int]]:
    quantities: Counter[str] = Counter()
    for order in orders:
        for dish in order.items:  # type: ignore[attr-defined]
            quantities[dish.sku] += dish.qty
    ranked = sorted(quantities.items(), key=lambda item: (-item[1], item[0]))
    return ranked[: max(n, 0)]


def day_report(lines: Iterable[str], raw_orders: Iterable[str], n: int) -> dict[str, object]:
    revenue = 0
    for raw in lines:
        record = _parse_log(raw)
        if record is not None and record[1] == "deliver":
            revenue += record[2]
    orders = parse_orders(raw_orders)
    best = best_order(orders)
    return {
        "revenue": revenue,
        "best_order": best.order_id if best is not None else None,
        "top_dishes": top_dishes(orders, n),
    }
