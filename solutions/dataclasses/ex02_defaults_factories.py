"""Эталон упражнения 2: значения по умолчанию и ``default_factory``."""

from __future__ import annotations

from dataclasses import dataclass, field


def declare_inventory_item() -> type:
    @dataclass
    class InventoryItem:
        """Позиция на складе."""

        name: str
        quantity: int = 0
        tags: list[str] = field(default_factory=list)

    return InventoryItem


def add_tag(item: object, tag: str) -> object:
    tags = item.tags  # type: ignore[attr-defined]
    tags.append(tag)
    return item


def independent_defaults() -> bool:
    item_cls = declare_inventory_item()
    first = item_cls("a")
    second = item_cls("b")
    return first.tags is not second.tags


def mutable_default_is_rejected() -> bool:
    try:

        @dataclass
        class Bad:
            items: list[int] = []  # noqa: RUF008

    except ValueError:
        return True
    return False
