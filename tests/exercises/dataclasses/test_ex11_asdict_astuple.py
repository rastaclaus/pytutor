"""Тесты упражнения 11: ``asdict`` и ``astuple``."""

from __future__ import annotations

import pytest

from pytutor.exercises.dataclasses import ex11_asdict_astuple as ex


def test_asdict_flat() -> None:
    point_cls, _ = ex.declare_models()
    assert ex.to_dict(point_cls(1, 2)) == {"x": 1, "y": 2}


def test_asdict_nested() -> None:
    assert ex.nested_roundtrip() == {
        "start": {"x": 0, "y": 0},
        "end": {"x": 3, "y": 4},
        "weight": 2.5,
    }


def test_astuple_nested() -> None:
    point_cls, segment_cls = ex.declare_models()
    segment = segment_cls(point_cls(0, 0), point_cls(3, 4), 2.5)
    assert ex.to_tuple(segment) == ((0, 0), (3, 4), 2.5)


def test_asdict_is_deep_copy() -> None:
    assert ex.is_deep_copy() is True


def test_asdict_rejects_non_dataclass() -> None:
    with pytest.raises(TypeError):
        ex.to_dict({"x": 1})
