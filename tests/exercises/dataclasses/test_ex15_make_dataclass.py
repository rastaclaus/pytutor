"""Тесты упражнения 15: ``make_dataclass``."""

from __future__ import annotations

from dataclasses import fields

from pytutor.exercises.dataclasses import ex15_make_dataclass as ex


def test_build_point() -> None:
    point_cls = ex.build_point()
    point = point_cls(1, 2)
    assert point_cls.__name__ == "DynPoint"
    assert (point.x, point.y) == (1, 2)


def test_build_record() -> None:
    record_cls = ex.build_record(["a", "b"])
    record = record_cls(10, "x")
    assert [item.name for item in fields(record_cls)] == ["a", "b"]
    assert (record.a, record.b) == (10, "x")


def test_build_record_without_fields() -> None:
    record_cls = ex.build_record([])
    assert fields(record_cls) == ()
    assert record_cls() == record_cls()


def test_build_row() -> None:
    row_cls = ex.build_row([("age", int), ("name", str)])
    row = row_cls(30, "alice")
    assert (row.age, row.name) == (30, "alice")


def test_add_method() -> None:
    instance = ex.add_method(None)
    assert instance.value == 21
    assert instance.doubled() == 42
