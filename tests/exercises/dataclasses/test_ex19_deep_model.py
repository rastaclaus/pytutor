"""Тесты упражнения 19: неизменяемое дерево."""

from __future__ import annotations

import pytest

from pytutor.exercises.dataclasses import ex19_deep_model as ex


def test_leaf() -> None:
    node_cls = ex.declare_node()
    leaf = node_cls(name="leaf")
    assert leaf.is_leaf() is True
    assert leaf.depth() == 1


def test_walk_order() -> None:
    tree = ex.make_tree({"root": {"a": {}, "b": {"c": {}}}})
    assert ex.names_in_order(tree) == ["root", "a", "b", "c"]


def test_depth() -> None:
    tree = ex.make_tree({"root": {"a": {}, "b": {"c": {}}}})
    assert ex.depth(tree) == 3


def test_parent_links() -> None:
    tree = ex.make_tree({"root": {"a": {}}})
    assert tree.children[0].parent is tree


def test_node_is_frozen() -> None:
    node_cls = ex.declare_node()
    node = node_cls(name="a")
    with pytest.raises(Exception, match="cannot assign to field"):
        node.name = "b"


def test_node_has_no_dict() -> None:
    node_cls = ex.declare_node()
    assert not hasattr(node_cls(name="a"), "__dict__")


def test_add_child_returns_new_node() -> None:
    tree = ex.make_tree({"root": {}})
    grown = ex.add_child(tree, "x")
    assert grown is not tree
    assert tree.children == ()
    assert [child.name for child in grown.children] == ["x"]
    # Новый потомок связан обратной ссылкой именно с новым узлом.
    assert grown.children[0].parent is grown


def test_nodes_are_hashable() -> None:
    node_cls = ex.declare_node()
    assert len({node_cls(name="a"), node_cls(name="a")}) == 1


def test_parent_does_not_affect_equality() -> None:
    node_cls = ex.declare_node()
    assert node_cls(name="a") == node_cls(name="a", parent=node_cls(name="p"))
