"""Эталон упражнения 1 (boss): неизменяемые модели заказа."""

from __future__ import annotations

from dataclasses import dataclass, field, replace


def declare_models() -> tuple[type, type]:
    @dataclass
    class Dish:
        """Позиция заказа."""

        sku: str
        price: int
        qty: int = 1
        total: int = field(init=False, default=0)

        def __post_init__(self) -> None:
            self.total = self.price * self.qty

    @dataclass
    class Order:
        """Заказ: идентификатор, курьер и позиции."""

        order_id: str
        courier: str = ""
        items: list[Dish] = field(default_factory=list)

        def total(self) -> int:
            return sum(dish.total for dish in self.items)

    return Dish, Order


def new_order(order_id: str) -> object:
    _, order_cls = declare_models()
    return order_cls(order_id)


def add_dish(order: object, dish: object) -> object:
    _, order_cls = declare_models()
    return order_cls(order.order_id, order.courier, [*order.items, dish])  # type: ignore[attr-defined]


def assign_courier(order: object, courier: str) -> object:
    if not courier:
        msg = "courier must be a non-empty string"
        raise ValueError(msg)
    return replace(order, courier=courier)  # type: ignore[misc]


def repeat_dish(order: object, sku: str) -> object:
    dish_cls, order_cls = declare_models()
    items: list[object] = []
    changed = False
    for dish in order.items:  # type: ignore[attr-defined]
        if dish.sku == sku:
            items.append(dish_cls(dish.sku, dish.price, dish.qty * 2))
            changed = True
        else:
            items.append(dish)
    if not changed:
        return order_cls(order.order_id, order.courier, list(order.items))  # type: ignore[attr-defined]
    return order_cls(order.order_id, order.courier, items)  # type: ignore[attr-defined]
