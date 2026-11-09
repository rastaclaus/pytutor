"""Тесты упражнения 16 (functools): найди баг — компаратор и ``cmp_to_key``.

Тесты описывают правильное поведение. В заготовке ``ex16_debug_cmp_to_key``
три бага; после исправлений все тесты должны стать зелёными.
"""

from __future__ import annotations

from pytutor.exercises.functools import ex16_debug_cmp_to_key as ex


def test_compare_natural_uses_numbers() -> None:
    assert ex.compare_natural("file2", "file10") == -1
    assert ex.compare_natural("file10", "file2") == 1
    assert ex.compare_natural("file2", "file2") == 0


def test_compare_natural_mixed_text() -> None:
    assert ex.compare_natural("a1", "a2") == -1
    assert ex.compare_natural("img12", "img9") == 1


def test_natural_sort_files() -> None:
    files = ["file10", "file2", "file1"]
    assert ex.natural_sort(files) == ["file1", "file2", "file10"]


def test_natural_sort_empty() -> None:
    assert ex.natural_sort([]) == []


def test_sort_files_basic() -> None:
    files = ["report10.csv", "report2.csv", "report1.csv"]
    assert ex.sort_files(files) == ["report1.csv", "report2.csv", "report10.csv"]


def test_sort_files_preserves_equal_order() -> None:
    # Стабильность: одинаковые ключи сохраняют исходный порядок.
    files = ["a1.txt", "a1.txt.bak", "a1(1).txt"]
    result = ex.sort_files(files)
    assert len(result) == 3
    assert result[0] == "a1(1).txt" or result[0] == "a1.txt"


def test_natural_sort_long_numbers() -> None:
    files = ["v2", "v100000000000000000000", "v3"]
    assert ex.natural_sort(files) == ["v2", "v3", "v100000000000000000000"]
