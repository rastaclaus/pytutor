"""Тесты упражнения 13: тонкая настройка полей."""

from __future__ import annotations

from pytutor.exercises.dataclasses import ex13_custom_eq_repr as ex


def test_entry_basics() -> None:
    entry = ex.make_entry("k", "v", 3)
    assert entry.key == "k"
    assert entry.payload == "v"
    assert entry.hits == 3


def test_repr_excludes_hits() -> None:
    assert ex.repr_excludes_hits() is True


def test_repr_contains_other_fields() -> None:
    text = repr(ex.make_entry("k", "v"))
    assert "key='k'" in text
    assert "payload='v'" in text


def test_equality_ignores_hits() -> None:
    assert ex.equality_ignores_hits() is True


def test_unsafe_hash_is_generated() -> None:
    assert ex.unsafe_hash_is_generated() is True


def test_plain_mutable_dataclass_is_unhashable() -> None:
    entry = ex.make_entry("k", "v")
    try:
        hash(entry)
    except TypeError:
        pass
    else:  # pragma: no cover
        raise AssertionError("изменяемый dataclass не должен хешироваться")
