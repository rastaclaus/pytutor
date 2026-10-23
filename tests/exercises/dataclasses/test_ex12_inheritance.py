"""Тесты упражнения 12: наследование."""

from __future__ import annotations

from pytutor.exercises.dataclasses import ex12_inheritance as ex


def test_child_inherits_and_runs_post_init() -> None:
    child = ex.make_child("Alice", 30)
    assert child.name == "alice"
    assert child.age == 31


def test_inherited_field_order() -> None:
    assert ex.inherited_field_order() == ["name", "age"]


def test_child_is_instance_of_base() -> None:
    base_cls, child_cls = ex.declare_hierarchy()
    assert isinstance(child_cls("bob"), base_cls)


def test_default_before_non_default_is_rejected() -> None:
    assert ex.default_before_non_default_is_rejected() is True
