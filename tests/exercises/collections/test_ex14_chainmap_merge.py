"""Тесты упражнения 14: слияние ``ChainMap``."""

from __future__ import annotations

from collections import ChainMap

from pytutor.exercises.collections import ex14_chainmap_merge as ex


def test_flatten() -> None:
    cm = ChainMap({"a": 1}, {"a": 2, "b": 3})
    assert ex.flatten(cm) == {"a": 1, "b": 3}
    assert ex.flatten(ChainMap()) == {}


def test_source_report() -> None:
    cm = ChainMap({"a": 1}, {"a": 2, "b": 3})
    assert ex.source_report(cm) == {"a": 0, "b": 1}


def test_conflict_keys() -> None:
    cm = ChainMap({"a": 1, "c": 4}, {"a": 2, "b": 3}, {"b": 5, "c": 6})
    assert sorted(ex.conflict_keys(cm)) == ["a", "b", "c"]


def test_update_all_layers() -> None:
    first = {"a": 1}
    second = {"a": 2, "b": 3}
    cm = ChainMap(first, second)
    result = ex.update_all_layers(cm, "a", 99)
    assert result is cm
    assert first["a"] == 99
    assert second["a"] == 99
    assert second["b"] == 3


def test_merged_from() -> None:
    assert ex.merged_from([{"a": 1}, {"a": 2, "b": 3}]) == {"a": 2, "b": 3}
    assert ex.merged_from([]) == {}
