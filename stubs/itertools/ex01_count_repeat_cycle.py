"""Упражнение 1. Счётчики и повторы: ``count``, ``repeat``, ``cycle``. Уровень 1.

``itertools`` даёт три источника элементов «по требованию»:

* ``count(start, step)`` — арифметическая прогрессия (бесконечная);
* ``repeat(value, times)`` — одно и то же значение; без ``times`` — бесконечно;
* ``cycle(iterable)`` — элементы по кругу, тоже бесконечно.

Бесконечный итератор нельзя превратить в список целиком — его обрезают
``islice(iterable, n)``. ``islice`` ленив: забирает ровно ``n`` элементов и не
создаёт промежуточный список.

Реализуйте функции через эти инструменты, а не через срезы списков.
"""

from __future__ import annotations

from itertools import count, cycle, islice, repeat
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def take(n: int, iterable: Iterable[int]) -> list[int]:
    """Вернуть первые ``n`` элементов ``iterable``.

    Для ``n <= 0`` вернуть пустой список. ``iterable`` может быть бесконечным.
    """
    raise NotImplementedError


def countdown(start: int, n: int) -> list[int]:
    """Вернуть ``n`` чисел: ``start, start - 1, start - 2, ...``.

    Подсказка: ``count`` умеет и отрицательный шаг.
    """
    raise NotImplementedError


def repeat_value(value: str, times: int) -> list[str]:
    """Вернуть ``value``, повторённое ровно ``times`` раз."""
    raise NotImplementedError


def cycle_values(values: list[str], n: int) -> list[str]:
    """Вернуть первые ``n`` элементов бесконечного ``cycle(values)``.

    Для пустого ``values`` результат пуст: ``cycle`` по пустому входу сразу
    заканчивается, хотя формально и считается бесконечным.
    """
    raise NotImplementedError


def numbered(items: Iterable[str]) -> list[tuple[int, str]]:
    """Пронумеровать элементы с нуля: ``[(0, "a"), (1, "b"), ...]``."""
    raise NotImplementedError
