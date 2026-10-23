"""Эталон упражнения 12: наследование."""

from __future__ import annotations

from dataclasses import dataclass, fields


def declare_hierarchy() -> tuple[type, type]:
    @dataclass
    class Base:
        """Базовый класс."""

        name: str

        def __post_init__(self) -> None:
            self.name = self.name.lower()

    @dataclass
    class Child(Base):
        """Наследник."""

        age: int = 0

        def __post_init__(self) -> None:
            super().__post_init__()
            self.age += 1

    return Base, Child


def make_child(name: str, age: int) -> object:
    _, child_cls = declare_hierarchy()
    return child_cls(name, age)


def inherited_field_order() -> list[str]:
    _, child_cls = declare_hierarchy()
    return [item.name for item in fields(child_cls)]


def default_before_non_default_is_rejected() -> bool:
    try:

        @dataclass
        class Base:
            value: int = 0

        @dataclass
        class Child(Base):
            extra: int

    except TypeError:
        return True
    return False
