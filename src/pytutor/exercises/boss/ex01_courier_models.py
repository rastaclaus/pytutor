"""Упражнение 1 (boss). Неизменяемые модели заказа. Уровень 6.

Сценарий: в сервисе доставки заказ проходит через несколько статусов.
Каждое изменение — новый объект; история переходов накапливается рядом.

Реализуйте:

* ``declare_models()`` — создать и вернуть два dataclass:

  - ``Dish``: ``sku: str``, ``price: int``, ``qty: int = 1``;
    вычисляемое (``field(init=False)``) поле ``total: int = 0``, которое
    ``__post_init__`` заполняет значением ``price * qty``;
  - ``Order``: ``order_id: str``, ``courier: str = ""``,
    ``items: list[Dish] = field(default_factory=list)``;
    метод ``total()`` — сумма ``dish.total`` по позициям.

  Классы возвращаются кортежем ``(Dish, Order)``.

* ``new_order(order_id: str)`` — создать заказ без позиций.

* ``add_dish(order, dish)`` — вернуть **новый** заказ со списком позиций,
  куда дописан ``dish``; исходный заказ не меняется, список исходника
  не мутируется.

* ``assign_courier(order, courier)`` — вернуть новый заказ с заполненным
  курьером; исходный не меняется.

* ``repeat_dish(order, sku)`` — вернуть новый заказ, в котором позиция
  с данным ``sku`` умножена на два: вместо одной позиции ``Dish(sku, price, qty)``
  стоит ``Dish(sku, price, qty * 2)`` на том же месте. Позиции с другим ``sku``
  — те же объекты. Если ``sku`` нет в заказе, вернуть заказ без изменений
  (новым объектом).

Тексты ошибок: ``assign_courier`` с пустой строкой курьера бросает ``ValueError``
(в сообщении есть ``courier``).
"""

from __future__ import annotations

from dataclasses import dataclass, field


def declare_models() -> tuple[type, type]:
    """Создать и вернуть ``(Dish, Order)`` — см. условие модуля."""
    raise NotImplementedError


def new_order(order_id: str) -> object:
    """Создать заказ без позиций."""
    raise NotImplementedError


def add_dish(order: object, dish: object) -> object:
    """Новый заказ с дописанной позицией; исходный не меняется."""
    raise NotImplementedError


def assign_courier(order: object, courier: str) -> object:
    """Новый заказ с курьером; пустая строка — ``ValueError`` (``courier``)."""
    raise NotImplementedError


def repeat_dish(order: object, sku: str) -> object:
    """Новый заказ, где позиция с ``sku`` удвоена; остальных не касаемся."""
    raise NotImplementedError
