"""Упражнение 2. ``reduce`` для агрегации. Уровень 2.

Здесь ``reduce`` используется как основа для типичных агрегаций: разворачивание
вложенных списков, подсчёт частот, поиск самого частого элемента и группировка.

Все четыре функции реализуйте через ``functools.reduce``.
"""

from __future__ import annotations

import functools
from collections import defaultdict
from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable

T = TypeVar("T")
K = TypeVar("K")


def flatten(nested: Iterable[Iterable[int]]) -> list[int]:
    """Развернуть последовательность последовательностей в один список.

    Порядок элементов сохраняется: ``[[1, 2], [3], []]`` -> ``[1, 2, 3]``.
    """
    def extender(acc: list[int], ext: Iterable[int]) -> list[int]:
        acc.extend(ext)
        return acc

    return functools.reduce(extender, nested, [])


def count_items(items: Iterable[str]) -> dict[str, int]:
    """Посчитать, сколько раз встречается каждый элемент."""
    def bump(acc: defaultdict[str, int], val: str) -> defaultdict[str, int]:
        acc[val] += 1
        return acc

    return functools.reduce(bump, items, defaultdict(int))


def most_common(items: Iterable[str]) -> str | None:
    """Вернуть самый частый элемент или ``None`` для пустой последовательности.

    При равенстве частот возвращается тот элемент, который встретился раньше.
    """
    count = count_items(items)
    if not count:
        return None
    return max(count, key=count.get)  # ty: ignore[no-matching-overload]


def group_by(items: Iterable[T], key: Callable[[T], K]) -> dict[K, list[T]]:
    """Сгруппировать элементы по значению ``key(item)``.

    Порядок групп и элементов внутри группы — как при первом появлении.
    """
    def group(res: dict[K, list[T]], item: T) -> dict[K, list[T]]:
        key_value = key(item)
        res.setdefault(key_value, []).append(item)
        return  res
    return functools.reduce(group, items, {})
