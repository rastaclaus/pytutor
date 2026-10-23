"""Тесты упражнения 10: ``dataclasses.replace``."""

from __future__ import annotations

from dataclasses import replace

from pytutor.exercises.dataclasses import ex10_replace as ex


def test_replace_returns_new_object() -> None:
    settings_cls = ex.declare_settings()
    original = settings_cls("localhost", 80)
    changed = ex.with_debug(original, True)
    assert changed is not original
    assert changed.debug is True
    assert original.debug is False
    assert changed.host == original.host


def test_replace_keeps_type() -> None:
    original = ex.declare_settings()("localhost", 80)
    assert type(ex.with_debug(original, True)) is type(original)


def test_changed_fields() -> None:
    assert ex.changed_fields() == ["host", "port", "debug"]


def test_replace_unknown_field_fails() -> None:
    assert ex.replace_unknown_field_fails() is True


def test_replace_keeps_other_fields() -> None:
    settings_cls = ex.declare_settings()
    assert replace(settings_cls("a", 1), port=2).port == 2
