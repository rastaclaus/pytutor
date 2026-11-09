"""Эталон упражнения 16: вложенные структуры."""

from __future__ import annotations

from dataclasses import dataclass, field, replace


def declare_order() -> tuple[type, type]:
    @dataclass
    class OrderItem:
        """Позиция заказа."""

        sku: str
        price: float
        qty: int = 1

        def total(self) -> float:
            return self.price * self.qty

    @dataclass
    class Order:
        """Заказ."""

        order_id: str
        items: list[OrderItem] = field(default_factory=list)

        def total(self) -> float:
            return sum(item.total() for item in self.items)

    return OrderItem, Order


def make_order(items: list[tuple[str, float, int]]) -> object:
    item_cls, order_cls = declare_order()
    return order_cls("A1", [item_cls(sku, price, qty) for sku, price, qty in items])


def order_total(order: object) -> float:
    return order.total()  # type: ignore[attr-defined]


def add_item(order: object, sku: str, price: float, qty: int = 1) -> object:
    item_cls, _ = declare_order()
    order.items.append(item_cls(sku, price, qty))  # type: ignore[attr-defined]
    return order


def default_items_are_independent() -> bool:
    _, order_cls = declare_order()
    first = order_cls("a")
    second = order_cls("b")
    return first.items is not second.items


def deep_replace(order: object, sku: str, **changes: float) -> object:
    """Бонус: новый заказ с изменённой позицией."""
    _item_cls, order_cls = declare_order()
    old_item = next(item for item in order.items if item.sku == sku)  # type: ignore[attr-defined]
    new_item = replace(old_item, **changes)
    new_items = [
        new_item if item.sku == sku else item
        for item in order.items  # type: ignore[attr-defined]
    ]
    return order_cls(order.order_id, new_items)  # type: ignore[attr-defined]
