"""Тесты упражнения 3: замороженные экземпляры."""

from __future__ import annotations

import pytest

from pytutor.exercises.dataclasses import ex03_frozen as ex


def test_frozen_point_basics() -> None:
    point_cls = ex.declare_frozen_point()
    point = point_cls(1, 2)
    assert (point.x, point.y) == (1, 2)


def test_frozen_point_is_immutable() -> None:
    point_cls = ex.declare_frozen_point()
    point = point_cls(1, 2)
    with pytest.raises(Exception, match="cannot assign to field"):
        point.x = 10


def test_try_to_mutate_reports_error() -> None:
    assert ex.try_to_mutate() is True


def test_frozen_and_mutable_hashability() -> None:
    frozen_cls = ex.declare_frozen_point()
    mutable_cls = ex.declare_mutable_point()
    assert ex.is_hashable(frozen_cls(1, 2)) is True
    assert ex.is_hashable(mutable_cls(1, 2)) is False


def test_frozen_objects_work_in_set() -> None:
    point_cls = ex.declare_frozen_point()
    points = {point_cls(1, 2), point_cls(1, 2), point_cls(3, 4)}
    assert len(points) == 2


def test_mutable_point_allows_assignment() -> None:
    point_cls = ex.declare_mutable_point()
    point = point_cls(1, 2)
    point.x = 10
    assert point.x == 10
