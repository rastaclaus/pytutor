"""Тесты упражнения 9: ``cached_property``."""

from __future__ import annotations

from functools import cached_property

from pytutor.exercises.functools import ex09_cached_property as ex


def test_value_is_computed_once() -> None:
    obj = ex.HeavyValue(3)
    assert obj.value == 9
    assert obj.computations == 1
    # Повторное обращение берёт значение из кэша.
    assert obj.value == 9
    assert obj.computations == 1


def test_uses_cached_property() -> None:
    assert isinstance(ex.HeavyValue.__dict__["value"], cached_property)


def test_deletion_invalidates_cache() -> None:
    obj = ex.HeavyValue(2)
    assert obj.value == 4
    del obj.value
    assert obj.value == 4
    assert obj.computations == 2


def test_manual_override_wins() -> None:
    obj = ex.HeavyValue(2)
    assert obj.value == 4
    obj.value = 100
    assert obj.value == 100
    assert obj.computations == 1
