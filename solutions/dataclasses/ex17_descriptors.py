"""Эталон упражнения 17: поля-дескрипторы."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


class IntField:
    """Дескриптор целочисленного поля с проверкой диапазона."""

    def __init__(self, *, default: int = 0, max_value: int = 100) -> None:
        self.default = default
        self.max_value = max_value
        self.name = ""

    def __set_name__(self, owner: type, name: str) -> None:
        self.name = f"_{name}"

    def __get__(self, obj: Any, objtype: type | None = None) -> int:
        if obj is None:
            return self.default
        return getattr(obj, self.name, self.default)

    def __set__(self, obj: Any, value: Any) -> None:
        number = int(value)
        if not 0 <= number <= self.max_value:
            msg = f"значение вне диапазона: {number}"
            raise ValueError(msg)
        setattr(obj, self.name, number)


def declare_item() -> type:
    @dataclass
    class Item:
        """Товар с валидируемым количеством."""

        quantity: int = IntField(default=1)  # type: ignore[assignment]

    return Item


def make_item(quantity: object) -> object:
    return declare_item()(quantity=quantity)  # type: ignore[arg-type]
