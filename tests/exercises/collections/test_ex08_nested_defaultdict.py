"""Тесты упражнения 8: вложенные ``defaultdict``."""

from __future__ import annotations

from collections import Counter, defaultdict

from pytutor.exercises.collections import ex08_nested_defaultdict as ex


def test_nested_defaultdict_makes_second_level() -> None:
    tree = ex.nested_defaultdict()
    assert isinstance(tree, defaultdict)
    tree["a"]["x"].append(1)
    assert tree["a"]["x"] == [1]


def test_add_path() -> None:
    tree = ex.nested_defaultdict()
    ex.add_path(tree, ["a", "x"], 1)
    ex.add_path(tree, ["a", "x"], 2)
    ex.add_path(tree, ["b"], 3)
    assert tree["a"]["x"] == [1, 2]
    assert tree["b"] == [3]


def test_get_path() -> None:
    tree = ex.nested_defaultdict()
    ex.add_path(tree, ["a", "x"], 1)
    assert ex.get_path(tree, ["a", "x"]) == [1]
    assert ex.get_path(tree, ["a", "y"]) is None
    assert ex.get_path(tree, ["z"]) is None
    assert ex.get_path(tree, ["a", "x"], []) == [1]
    # get_path не должен создавать узлы
    assert "z" not in tree


def test_build_counts() -> None:
    tree = ex.build_counts(["ab", "abc"])
    assert tree[2] == Counter(a=1, b=1)
    assert tree[3] == Counter(a=1, b=1, c=1)


def test_merge_trees() -> None:
    left = ex.nested_defaultdict()
    right = ex.nested_defaultdict()
    ex.add_path(left, ["a", "x"], 1)
    ex.add_path(right, ["a", "x"], 2)
    ex.add_path(right, ["a", "x"], 3)
    merged = ex.merge_trees(left, right)
    assert merged["a"]["x"] == [1, 2, 3]
