"""Тесты упражнения 2: ``reduce`` для агрегации."""

from __future__ import annotations

from pytutor.exercises.functools import ex02_reduce_aggregation as ex


def test_flatten() -> None:
    assert ex.flatten([[1, 2], [3], [4, 5]]) == [1, 2, 3, 4, 5]
    assert ex.flatten([[1, 2], [], [3]]) == [1, 2, 3]
    assert ex.flatten([]) == []


def test_count_items() -> None:
    assert ex.count_items(["a", "b", "a", "a"]) == {"a": 3, "b": 1}
    assert ex.count_items([]) == {}


def test_most_common() -> None:
    assert ex.most_common(["a", "b", "a", "c", "a"]) == "a"
    assert ex.most_common(["x"]) == "x"
    assert ex.most_common([]) is None
    # Ничья: побеждает элемент, встретившийся раньше.
    assert ex.most_common(["b", "a", "a", "b"]) == "b"


def test_group_by() -> None:
    words = ["apple", "avocado", "banana", "cherry", "blueberry"]
    grouped = ex.group_by(words, key=lambda w: w[0])
    assert grouped == {
        "a": ["apple", "avocado"],
        "b": ["banana", "blueberry"],
        "c": ["cherry"],
    }


def test_group_by_preserves_first_seen_order() -> None:
    grouped = ex.group_by([3, 1, 3, 2, 1], key=lambda n: n % 2)
    assert list(grouped) == [1, 0]
    assert grouped[1] == [3, 1, 3, 1]
    assert grouped[0] == [2]
