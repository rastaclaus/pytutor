"""Тесты упражнения 16: вложенные структуры."""

from __future__ import annotations

from pytutor.exercises.dataclasses import ex16_nested as ex


def test_order_total() -> None:
    order = ex.make_order([("a", 2.0, 3), ("b", 5.0, 1)])
    assert ex.order_total(order) == 11.0


def test_empty_order_total() -> None:
    assert ex.order_total(ex.make_order([])) == 0


def test_add_item() -> None:
    order = ex.make_order([])
    assert ex.add_item(order, "zz", 1.5, 2) is order
    assert ex.order_total(order) == 3.0


def test_default_items_are_independent() -> None:
    assert ex.default_items_are_independent() is True


def test_nested_repr() -> None:
    item_cls, order_cls = ex.declare_order()
    order = order_cls("A1", [item_cls("a", 1.0)])
    assert "OrderItem(sku='a', price=1.0, qty=1)" in repr(order)
