"""Бонусные тесты упражнения 16 (dataclasses): глубокая замена позиции.

Необязательное задание повышенной сложности. В базовый прогон не входит:

    uv run pytest -m bonus
"""

from __future__ import annotations

import pytest

from pytutor.exercises.dataclasses import ex16_nested as ex


@pytest.fixture
def order():
    try:
        return ex.make_order([("a", 2.0, 3), ("b", 5.0, 1)])
    except NotImplementedError:
        pytest.skip("make_order не реализовано")


@pytest.mark.bonus
def test_deep_replace_changes_target_item(order) -> None:
    updated = ex.deep_replace(order, "a", price=3.0)
    target = next(item for item in updated.items if item.sku == "a")
    assert target.price == 3.0
    assert target.qty == 3


@pytest.mark.bonus
def test_deep_replace_keeps_original(order) -> None:
    original_price = next(item.price for item in order.items if item.sku == "a")
    ex.deep_replace(order, "a", price=3.0)
    assert next(item.price for item in order.items if item.sku == "a") == original_price


@pytest.mark.bonus
def test_deep_replace_new_order_object(order) -> None:
    updated = ex.deep_replace(order, "a", qty=10)
    assert updated is not order
    assert updated.order_id == order.order_id


@pytest.mark.bonus
def test_deep_replace_reuses_untouched_items(order) -> None:
    updated = ex.deep_replace(order, "a", price=3.0)
    old_b = next(item for item in order.items if item.sku == "b")
    new_b = next(item for item in updated.items if item.sku == "b")
    assert new_b is old_b
