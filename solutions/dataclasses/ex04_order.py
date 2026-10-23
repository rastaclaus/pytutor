"""Эталон упражнения 4: сравнения и ``order=True``."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def declare_version() -> type:
    @dataclass(order=True)
    class Version:
        """Версия вида major.minor."""

        major: int
        minor: int

    return Version


def sorted_versions(versions: Iterable[object]) -> list[object]:
    return sorted(versions)


def max_version(versions: Iterable[object]) -> object | None:
    items = list(versions)
    if not items:
        return None
    return max(items)


def order_without_eq_is_rejected() -> bool:
    try:

        @dataclass(order=True, eq=False)
        class Bad:
            value: int

    except ValueError:
        return True
    return False
