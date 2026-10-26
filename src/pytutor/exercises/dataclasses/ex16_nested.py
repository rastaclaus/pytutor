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

Порядок возврата: ``declare_order()`` возвращает ``(OrderItem, Order)`` —
сначала позицию, потом заказ, хотя в тексте задания заказ упомянут первым.
"""

from __future__ import annotations

from dataclasses import dataclass, field


def declare_order() -> tuple[type, type]:
    """Создать два dataclass и вернуть ``(OrderItem, Order)``.

    * ``OrderItem``: ``sku: str``, ``price: float``, ``qty: int = 1``;
      метод ``total()`` возвращает ``price * qty``.
    * ``Order``: ``order_id: str``, ``items: list[OrderItem] = field(default_factory=list)``;
      метод ``total()`` — сумма ``item.total()`` по всем позициям.

    Поведение:

    * ``OrderItem("a", 2.0, 3).total() == 6.0``;
    * ``Order("A1").total() == 0`` — пустой заказ;
    * ``repr(Order("A1", [OrderItem("a", 1.0)]))`` содержит
      ``OrderItem(sku='a', price=1.0, qty=1)``;
    * у двух заказов списки ``items`` — разные объекты.

    Подсказка: ``items: list[OrderItem] = field(default_factory=list)``;
    ``sum(...)`` по пустому списку даёт ``0`` без дополнительных проверок.
    """
    raise NotImplementedError


def make_order(items: list[tuple[str, float, int]]) -> object:
    """Создать ``Order`` с ``order_id="A1"`` из троек ``(sku, price, qty)``.

    ``make_order([("a", 2.0, 3), ("b", 5.0, 1)])`` даёт заказ из двух позиций;
    ``make_order([])`` даёт заказ без позиций с ``total() == 0``.

    Подсказка: ``[item_cls(sku, price, qty) for sku, price, qty in items]`.
    """
    raise NotImplementedError


def order_total(order: object) -> float:
    """Вернуть сумму по всем позициям заказа.

    ``order_total(make_order([("a", 2.0, 3), ("b", 5.0, 1)]))`` -> ``11.0``;
    ``order_total(make_order([]))`` -> ``0`` (целый ноль, сравнение с ``0``
    пройдёт).

    Подсказка: делегируйте в ``order.total()`` — логика суммы живёт в классе.
    """
    raise NotImplementedError


def add_item(order: object, sku: str, price: float, qty: int = 1) -> object:
    """Добавить позицию в ``order.items`` и вернуть тот же заказ.

    ``add_item(order, "zz", 1.5, 2) is order`` -> ``True``;
    после вызова ``order_total(order)`` вырос на ``1.5 * 2 = 3.0``;
    ``qty`` по умолчанию равен 1.

    Подсказка: создайте ``OrderItem`` и сделайте ``append``; возвращать нужно
    исходный объект, а не новый.
    """
    raise NotImplementedError


def default_items_are_independent() -> bool:
    """Вернуть ``True``, если у двух заказов свои списки позиций.

    Ожидаемое значение — ``True``.

    Подсказка: ``first.items is not second.items`` — сравнивайте объекты, а не
    значения: два пустых списка равны.
    """
    raise NotImplementedError
