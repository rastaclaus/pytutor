"""Тесты упражнения 18: ``MutableMapping`` — свой словарь с нуля."""

from __future__ import annotations

from pytutor.exercises.collections import ex18_custom_mapping as ex


def test_logging_dict_operations() -> None:
    d = ex.LoggingDict()
    d["a"] = 1
    _ = d["a"]
    d["b"] = 2
    del d["a"]
    assert d.log == ["set:a=1", "get:a", "set:b=2", "del:a"]
    assert len(d) == 1
    assert "b" in d
    assert "a" not in d


def test_logging_dict_builtin_methods() -> None:
    d = ex.LoggingDict()
    d["x"] = 10
    assert d.get("x") == 10
    assert d.get("nope") is None
    assert dict(d.items()) == {"x": 10}
    assert d.pop("x") == 10
    assert len(d) == 0


def test_access_counting_dict() -> None:
    d = ex.AccessCountingDict({"a": 1, "b": 2})
    _ = d["a"]
    _ = d["a"]
    _ = d["b"]
    assert d.access == {"a": 2, "b": 1}
    assert d.most_accessed(1) == [("a", 2)]
    assert d.most_accessed(5) == [("a", 2), ("b", 1)]


def test_access_counting_dict_del_removes_count() -> None:
    d = ex.AccessCountingDict({"a": 1})
    _ = d["a"]
    del d["a"]
    assert "a" not in d.access
    assert len(d) == 0
