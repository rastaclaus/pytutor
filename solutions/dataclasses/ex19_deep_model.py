"""Эталон упражнения 19: неизменяемое дерево."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Self

if TYPE_CHECKING:
    from collections.abc import Iterator


def declare_node() -> type:
    @dataclass(frozen=True, slots=True, kw_only=True)
    class Node:
        """Узел неизменяемого дерева."""

        name: str
        children: tuple[Node, ...] = ()
        parent: Node | None = field(default=None, repr=False, compare=False)

        def is_leaf(self) -> bool:
            return not self.children

        def walk(self) -> Iterator[str]:
            yield self.name
            for child in self.children:
                yield from child.walk()

        def with_child(self, child: Self) -> Self:
            grown = type(self)(name=self.name, children=(*self.children, child), parent=self.parent)
            object.__setattr__(child, "parent", grown)
            return grown

        def depth(self) -> int:
            if not self.children:
                return 1
            return 1 + max(child.depth() for child in self.children)

    return Node


def _build(node_cls: type, name: str, subtree: dict[str, object]) -> object:
    children = tuple(_build(node_cls, child_name, child_subtree) for child_name, child_subtree in subtree.items())
    node = node_cls(name=name, children=children)
    for child in children:
        object.__setattr__(child, "parent", node)
    return node


def make_tree(structure: dict[str, object]) -> object:
    node_cls = declare_node()
    (root_name, root_subtree), *_ = structure.items()
    return _build(node_cls, root_name, root_subtree)  # type: ignore[arg-type]


def names_in_order(node: object) -> list[str]:
    return list(node.walk())  # type: ignore[attr-defined]


def depth(node: object) -> int:
    return node.depth()  # type: ignore[attr-defined]


def add_child(node: object, name: str) -> object:
    node_cls = type(node)
    child = node_cls(name=name)
    return node.with_child(child)  # type: ignore[attr-defined]
