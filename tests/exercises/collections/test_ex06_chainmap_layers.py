"""Тесты упражнения 6: ``ChainMap`` — слои конфигурации."""

from __future__ import annotations

from collections import ChainMap

from pytutor.exercises.collections import ex06_chainmap_layers as ex


def test_make_chain() -> None:
    cm = ex.make_chain({"a": 1}, {"a": 2, "b": 3})
    assert isinstance(cm, ChainMap)
    assert cm["a"] == 2


def test_lookup_priority() -> None:
    cm = ex.make_chain({"a": 1, "b": 2}, {"b": 3})
    assert ex.lookup_priority(cm, "a") == 1
    assert ex.lookup_priority(cm, "b") == 3
    assert ex.lookup_priority(cm, "c") is None


def test_flatten_layers() -> None:
    cm = ChainMap({"a": 1}, {"a": 2, "b": 3})
    assert ex.flatten_layers(cm) == {"a": 1, "b": 3}


def test_insert_layer() -> None:
    cm = ex.make_chain({"a": 1}, {"b": 2})
    new = ex.insert_layer(cm, {"a": 10})
    assert isinstance(new, ChainMap)
    assert new["a"] == 10
    assert cm["a"] == 1  # исходный не изменился


def test_drop_first_layer() -> None:
    cm = ChainMap({"a": 1}, {"a": 2, "b": 3})
    parents = ex.drop_first_layer(cm)
    assert parents["a"] == 2
    assert "b" in parents


def test_write_through() -> None:
    user = {"a": 1}
    defaults = {"a": 2, "b": 3}
    cm = ChainMap(user, defaults)
    result = ex.write_through(cm, "a", 99)
    assert result is cm
    assert cm["a"] == 99
    assert user["a"] == 99
    assert defaults["a"] == 2  # нижележащий слой не тронут
