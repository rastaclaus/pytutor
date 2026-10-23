"""Эталон упражнения 15: ``make_dataclass``."""

from __future__ import annotations

from dataclasses import make_dataclass
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Iterable, Sequence


def build_point() -> type:
    return make_dataclass("DynPoint", [("x", int), ("y", int)])


def build_record(names: Sequence[str]) -> type:
    return make_dataclass("DynRecord", [(name, Any) for name in names])


def build_row(values: Iterable[tuple[str, type]]) -> type:
    return make_dataclass("DynRow", list(values))


def add_method(instance: object) -> object:  # noqa: ARG001
    """Создать класс с методом и вернуть его экземпляр со значением 21."""
    cls = make_dataclass(
        "DynCalc",
        [("value", int)],
        namespace={"doubled": lambda self: self.value * 2},
    )
    return cls(21)
