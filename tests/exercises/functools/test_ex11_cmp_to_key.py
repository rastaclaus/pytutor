"""Тесты упражнения 11: ``cmp_to_key``."""

from __future__ import annotations

from pytutor.exercises.functools import ex11_cmp_to_key as ex


def test_compare_by_absolute() -> None:
    assert ex.compare_by_absolute(3, -5) == -1
    assert ex.compare_by_absolute(-5, 3) == 1
    assert ex.compare_by_absolute(4, -4) == 0


def test_sort_by_absolute() -> None:
    assert ex.sort_by_absolute([-5, 3, -1, 2]) == [-1, 2, 3, -5]
    assert ex.sort_by_absolute([]) == []


def test_compare_natural() -> None:
    assert ex.compare_natural("a2", "a10") == -1
    assert ex.compare_natural("a10", "a2") == 1
    assert ex.compare_natural("a2", "a2") == 0


def test_natural_sort() -> None:
    assert ex.natural_sort(["file10", "file2", "file1"]) == [
        "file1",
        "file2",
        "file10",
    ]


def test_natural_sort_with_mixed_case() -> None:
    assert ex.natural_sort(["img12", "img1", "IMG2"]) == ["img1", "IMG2", "img12"]
