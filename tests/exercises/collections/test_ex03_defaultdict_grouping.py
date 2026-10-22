"""Тесты упражнения 3: ``defaultdict`` — группировка."""

from __future__ import annotations

from pytutor.exercises.collections import ex03_defaultdict_grouping as ex


def test_group_by_key() -> None:
    assert ex.group_by_key([("a", 1), ("b", 2), ("a", 3)]) == {
        "a": [1, 3],
        "b": [2],
    }
    assert ex.group_by_key([]) == {}


def test_group_unique() -> None:
    assert ex.group_unique([("a", 1), ("a", 1), ("a", 2)]) == {"a": {1, 2}}


def test_index_by_field() -> None:
    records = [("a", "x"), ("b", "y"), ("c", "x")]
    assert ex.index_by_field(records, 1) == {
        "x": [("a", "x"), ("c", "x")],
        "y": [("b", "y")],
    }
    assert ex.index_by_field(records, 0) == {
        "a": [("a", "x")],
        "b": [("b", "y")],
        "c": [("c", "x")],
    }


def test_invert_mapping() -> None:
    assert ex.invert_mapping({"a": 1, "b": 2, "c": 1}) == {
        1: ["a", "c"],
        2: ["b"],
    }
    assert ex.invert_mapping({}) == {}


def test_group_by_first_letter() -> None:
    assert ex.group_by_first_letter(["apple", "avocado", "banana"]) == {
        "a": ["apple", "avocado"],
        "b": ["banana"],
    }
    assert ex.group_by_first_letter(["", "x"]) == {"x": ["x"]}
