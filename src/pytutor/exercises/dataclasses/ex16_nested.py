"""Упражнение 16. Вложенные структуры и фабрики. Уровень 6.

Вложенные dataclass — обычное дело: заказ содержит позиции, документ — блоки,
конфиг — секции. Ключевые моменты:

* контейнеры объявляются с ``field(default_factory=list)``/``dict``;
* ``asdict`` рекурсивно разворачивает вложенность, но не знает про
  самоссылки (цикл вызовет ``RecursionError``);
* ``replace`` меняет только верхний уровень: вложенный объект остаётся тем же
  (поверхностная копия);
* чтобы изменить глубину, нужна своя функция, возвращающая новое дерево.

Именно из-за «разделяемых» вложенных объектов концептуально неизменяемые модели
делают ``frozen=True`` на всех уровнях.
"""

from __future__ import annotations

from dataclasses import dataclass, field


def declare_order() -> tuple[type, type]:
    """Создать два dataclass и вернуть ``(OrderItem, Order)``.

    * ``OrderItem``: ``sku: str``, ``price: float``, ``qty: int = 1``;
      метод ``total()`` возвращает ``price * qty``.
    * ``Order``: ``order_id: str``, ``items: list[OrderItem] = field(default_factory=list)``;
      метод ``total()`` — сумма ``item.total()`` по всем позициям.
    """
    raise NotImplementedError


def make_order(items: list[tuple[str, float, int]]) -> object:
    """Создать ``Order`` с ``order_id="A1"`` из троек ``(sku, price, qty)``."""
    raise NotImplementedError


def order_total(order: object) -> float:
    """Вернуть сумму по всем позициям заказа."""
    raise NotImplementedError


def add_item(order: object, sku: str, price: float, qty: int = 1) -> object:
    """Добавить позицию в ``order.items`` и вернуть тот же заказ."""
    raise NotImplementedError


def default_items_are_independent() -> bool:
    """Вернуть ``True``, если у двух заказов свои списки позиций."""
    raise NotImplementedError
