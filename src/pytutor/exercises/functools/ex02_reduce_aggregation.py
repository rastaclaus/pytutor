"""Упражнение 2. ``reduce`` для агрегации. Уровень 2.

Здесь ``reduce`` используется как основа для типичных агрегаций: разворачивание
вложенных списков, подсчёт частот, поиск самого частого элемента и группировка.

Все четыре функции реализуйте через ``functools.reduce``.
"""

from __future__ import annotations

import functools
from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable

T = TypeVar("T")
K = TypeVar("K")


def flatten(nested: Iterable[Iterable[int]]) -> list[int]:
    """Развернуть последовательность последовательностей в один список.

    Порядок элементов сохраняется: ``[[1, 2], [3], []]`` -> ``[1, 2, 3]``.
    """
    def _extract(acc: list[int], numbers: Iterable[int]) -> list[int]:
        acc.extend(numbers)
        return acc

    return functools.reduce(_extract, nested, [])


def count_items(items: Iterable[str]) -> dict[str, int]:
    """Посчитать, сколько раз встречается каждый элемент."""

    def counter(acc: dict[str, int], item: str) -> dict[str, int]:
        acc[item] = acc.setdefault(item, 0) + 1
        return acc

    return functools.reduce(counter, items, {})



def most_common(items: Iterable[str]) -> str | None:
    """Вернуть самый частый элемент или ``None`` для пустой последовательности.

    При равенстве частот возвращается тот элемент, который встретился раньше.
    """
    counts = count_items(items)
    if not counts:
        return None
    return max(counts, key=counts.get)  # ty: ignore[no-matching-overload]


def group_by[K, T](items: Iterable[T], key: Callable[[T], K]) -> dict[K, list[T]]:
    """Сгруппировать элементы по значению ``key(item)``.

    Порядок групп и элементов внутри группы — как при первом появлении.
    """
    def group_by(acc: dict[K, list[T]], item: T) -> dict[K, list[T]]:
        acc.setdefault(key(item), []).append(item)
        return acc
    return functools.reduce(group_by, items, {})
