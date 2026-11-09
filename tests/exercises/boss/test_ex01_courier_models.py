"""Тесты упражнения 1 (boss): неизменяемые модели заказа.

В базовом прогоне всё падает с ``NotImplementedError``: тесты, зависящие от
классов из ``declare_models``, помечены ``skip``, пока классы не реализованы.
Фикстуры обёрнуты так, чтобы нерешённое упражнение не давало ``ERROR`` на
этапе настройки, а честно падало или пропускалось.
"""

from __future__ import annotations

import pytest

from pytutor.exercises.boss import ex01_courier_models as ex


def _models_or_none():
    try:
        return ex.declare_models()
    except NotImplementedError:
        return None


@pytest.fixture
def classes():
    models = _models_or_none()
    if models is None:
        pytest.skip("declare_models не реализовано")
    return models


@pytest.fixture
def dish_cls(classes):
    return classes[0]


@pytest.fixture
def order_cls(classes):
    return classes[1]


def test_dish_total_computed(dish_cls) -> None:
    dish = dish_cls("a", 3, 2)
    assert dish.total == 6
    assert dish_cls("a", 3).total == 3


def test_order_total(order_cls, dish_cls) -> None:
    order = order_cls("A1", items=[dish_cls("a", 2, 3), dish_cls("b", 5)])
    assert order.total() == 11
    assert order_cls("A2").total() == 0


def test_new_order() -> None:
    order = ex.new_order("A1")
    assert order.total() == 0
    assert order.courier == ""


def test_add_dish_returns_new_object(order_cls, dish_cls) -> None:
    order = order_cls("A1")
    changed = ex.add_dish(order, dish_cls("a", 2))
    assert changed is not order
    assert len(changed.items) == 1
    assert len(order.items) == 0
    assert changed.items[0] is not None


def test_assign_courier(order_cls, dish_cls) -> None:
    order = order_cls("A1", items=[dish_cls("a", 2)])
    changed = ex.assign_courier(order, "anna")
    assert changed.courier == "anna"
    assert order.courier == ""
    assert changed.items[0] is order.items[0]


def test_assign_courier_rejects_empty(order_cls) -> None:
    with pytest.raises(ValueError, match="courier"):
        ex.assign_courier(order_cls("A1"), "")


def test_repeat_dish_doubles_qty(order_cls, dish_cls) -> None:
    order = order_cls("A1", items=[dish_cls("a", 2, 3), dish_cls("b", 5)])
    changed = ex.repeat_dish(order, "a")
    new_a = changed.items[0]
    assert new_a.qty == 6
    assert new_a.total == 12
    assert changed.items[1] is order.items[1]  # чужие позиции не копируются
    assert order.items[0].qty == 3  # исходник не тронут


def test_repeat_dish_missing_sku(order_cls, dish_cls) -> None:
    order = order_cls("A1", items=[dish_cls("a", 2)])
    changed = ex.repeat_dish(order, "zzz")
    assert changed is not order
    assert changed.items[0] is order.items[0]
