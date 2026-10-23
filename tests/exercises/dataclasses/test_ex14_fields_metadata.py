"""Тесты упражнения 14: интроспекция полей."""

from __future__ import annotations

from pytutor.exercises.dataclasses import ex14_fields_metadata as ex


def test_field_names() -> None:
    assert ex.field_names() == ["name", "kind", "size"]


def test_primary_key_names() -> None:
    assert ex.primary_key_names() == ["name"]


def test_fields_without_default() -> None:
    assert ex.fields_without_default() == ["name"]


def test_metadata_is_read_only() -> None:
    assert ex.metadata_is_read_only() is True


def test_column_construction() -> None:
    column_cls = ex.declare_column()
    column = column_cls("id")
    assert column.name == "id"
    assert column.kind == "text"
    assert column.size == 0
