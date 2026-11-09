"""Тесты упражнения 16 (itertools): найди баг — аналитика серий.

Тесты описывают правильное поведение. В заготовке ``ex16_debug_groupby``
три бага; после исправлений все тесты должны стать зелёными.
"""

from __future__ import annotations

from pytutor.exercises.itertools import ex16_debug_groupby as ex


def test_runs_basic() -> None:
    assert ex.runs(["A", "A", "B", "C"]) == [("A", 2), ("B", 1), ("C", 1)]
    assert ex.runs(list("AAABBC")) == [("A", 3), ("B", 2), ("C", 1)]


def test_runs_empty() -> None:
    assert ex.runs([]) == []


def test_group_sizes() -> None:
    assert ex.group_sizes(list("AABBC")) == [2, 2, 1]
    assert ex.group_sizes([]) == []


def test_group_sizes_are_not_all_zero() -> None:
    # Классическая ловушка groupby: под-итераторы пусты после перехода
    # к следующей группе. Если длины считаются вовремя, здесь не будет
    # списка из одних нулей.
    assert ex.group_sizes(list("XXYYX")) == [2, 2, 1]
    assert sum(ex.group_sizes(list("XXYYX"))) == 5


def test_unique_justseen() -> None:
    assert ex.unique_justseen(list("AABBA")) == ["A", "B", "A"]
    assert ex.unique_justseen([]) == []
    assert ex.unique_justseen(list("AAA")) == ["A"]


def test_top_run_basic() -> None:
    assert ex.top_run(list("AABBB")) == ("B", 3)
    assert ex.top_run([]) is None


def test_top_run_tie_goes_to_first() -> None:
    # Обе серии длины 2; правильный ответ — первая по порядку.
    assert ex.top_run(list("AABB")) == ("A", 2)
    assert ex.top_run(list("BBAA")) == ("B", 2)
