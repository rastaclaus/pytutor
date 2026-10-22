"""Тесты упражнения 10: ``total_ordering``."""

from __future__ import annotations

import pytest

from pytutor.exercises.functools import ex10_total_ordering as ex


def test_equality() -> None:
    assert ex.Version(1, 2) == ex.Version(1, 2)
    assert ex.Version(1, 2) != ex.Version(1, 3)


def test_lt_and_derived_operators() -> None:
    assert ex.Version(1, 2) < ex.Version(1, 10)
    assert ex.Version(2, 0) > ex.Version(1, 9)
    assert ex.Version(1, 0) <= ex.Version(1, 0)
    assert ex.Version(1, 0) >= ex.Version(1, 0)
    assert not (ex.Version(1, 0) < ex.Version(1, 0))


def test_sorted() -> None:
    versions = [
        ex.Version(2, 0),
        ex.Version(1, 10),
        ex.Version(1, 2),
        ex.Version(1, 2, 0),
    ]
    assert sorted(versions) == [
        ex.Version(1, 2),
        ex.Version(1, 2, 0),
        ex.Version(1, 10),
        ex.Version(2, 0),
    ]


def test_repr() -> None:
    assert repr(ex.Version(1, 2, 0)) == "Version(1, 2, 0)"


def test_incomparable_type_raises() -> None:
    with pytest.raises(TypeError):
        _ = ex.Version(1) < 5
