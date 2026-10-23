"""Тесты упражнения 2: значения по умолчанию и ``default_factory``."""

from __future__ import annotations

from pytutor.exercises.dataclasses import ex02_defaults_factories as ex


def test_defaults_apply() -> None:
    item_cls = ex.declare_inventory_item()
    item = item_cls("widget")
    assert item.name == "widget"
    assert item.quantity == 0
    assert item.tags == []


def test_explicit_values_apply() -> None:
    item_cls = ex.declare_inventory_item()
    item = item_cls("widget", quantity=3, tags=["new"])
    assert item.quantity == 3
    assert item.tags == ["new"]


def test_add_tag_mutates_and_returns_same_object() -> None:
    item_cls = ex.declare_inventory_item()
    item = item_cls("widget")
    assert ex.add_tag(item, "sale") is item
    assert item.tags == ["sale"]


def test_defaults_are_independent() -> None:
    assert ex.independent_defaults() is True


def test_mutable_default_is_rejected() -> None:
    assert ex.mutable_default_is_rejected() is True
