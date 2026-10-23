"""Тесты упражнения 4: сравнения и ``order=True``."""

from __future__ import annotations

import pytest

from pytutor.exercises.dataclasses import ex04_order as ex


def test_order_generates_comparisons() -> None:
    version_cls = ex.declare_version()
    assert version_cls(1, 2) < version_cls(1, 3)
    assert version_cls(2, 0) > version_cls(1, 9)
    assert version_cls(1, 2) <= version_cls(1, 2)
    assert version_cls(1, 2) == version_cls(1, 2)


def test_comparison_uses_field_order() -> None:
    version_cls = ex.declare_version()
    assert version_cls(2, 0) > version_cls(1, 99)
    # первое поле важнее второго
    assert not version_cls(1, 5) > version_cls(2, 0)


def test_sorted_versions() -> None:
    version_cls = ex.declare_version()
    versions = [version_cls(2, 1), version_cls(1, 4), version_cls(1, 0)]
    assert ex.sorted_versions(versions) == [version_cls(1, 0), version_cls(1, 4), version_cls(2, 1)]


def test_max_version() -> None:
    version_cls = ex.declare_version()
    assert ex.max_version([version_cls(1, 2), version_cls(3, 0)]) == version_cls(3, 0)
    assert ex.max_version([]) is None


def test_compare_with_other_type_raises() -> None:
    version_cls = ex.declare_version()
    with pytest.raises(TypeError):
        _ = version_cls(1, 2) < 5  # type: ignore[operator]


def test_order_without_eq_is_rejected() -> None:
    assert ex.order_without_eq_is_rejected() is True
