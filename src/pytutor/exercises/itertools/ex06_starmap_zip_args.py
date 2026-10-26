"""Упражнение 6. ``starmap`` и ``repeat``: аргументы уже упакованы. Уровень 3.

``map(func, iterable)`` передаёт в ``func`` один аргумент. Если аргументы уже
лежат кортежами, нужен ``starmap(func, iterable_of_tuples)``: он делает
``func(*args)``. Разница ровно как между ``func(a, b)`` и ``func(*pair)``.

``repeat(value, times)`` — бесконечный (или ограниченный) источник одного и того
же значения. В паре с ``map``/``zip``/``starmap`` он позволяет «размножить»
константу: ``map(pow, range(5), repeat(2))`` возводит всё в квадрат.

``functools.partial`` фиксирует часть аргументов заранее — вместе с ``map`` это
даёт компактные конвейеры без лямбд.

Функция ``_format_measurement`` уже реализована — используйте её.
"""

from __future__ import annotations

import operator
from functools import partial
from itertools import repeat, starmap
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable


def _format_measurement(value: int, *, unit: str) -> str:
    """Отформатировать значение с единицей измерения (``"5 kg"``)."""
    return f"{value} {unit}"


def apply_pairs(func: Callable[[int, int], int], pairs: Iterable[tuple[int, int]]) -> list[int]:
    """Применить ``func`` к каждой паре аргументов."""
    return list(starmap(func, pairs))


def dot_product(left: Iterable[int], right: Iterable[int]) -> int:
    """Скалярное произведение через ``starmap`` и ``operator.mul``."""
    return sum(map(operator.mul, left, right, strict=False))


def total_cost(rows: Iterable[tuple[int, int]]) -> int:
    """Сумма ``price * quantity`` по строкам ``(price, quantity)``."""
    return sum(starmap(operator.mul, rows))


def repeat_apply(func: Callable[[str], str], value: str, times: int) -> list[str]:
    """Применить ``func`` к ``value`` ровно ``times`` раз (через ``map`` + ``repeat``)."""
    return list(map(func, repeat(value, times)))


def pair_with_constant(values: Iterable[str], constant: int) -> list[tuple[str, int]]:
    """Приписать каждому значению одну и ту же константу."""
    return list(zip(values, repeat(constant), strict=False))


def apply_all(functions: Iterable[Callable[[int], int]], value: int) -> list[int]:
    """Применить каждую функцию к одному и тому же ``value``.

    Подсказка: ``map`` умеет несколько итерируемых аргументов:
    ``map(operator.call, functions, repeat(value))``.
    """
    return list(map(operator.call, functions, repeat(value)))  # ty: ignore[invalid-argument-type]


def make_formatter(unit: str) -> Callable[[int], str]:
    """Вернуть функцию ``value -> "value unit"`` через ``functools.partial``."""
    return partial(_format_measurement, unit=unit)


def format_values(values: Iterable[int], unit: str) -> list[str]:
    """Отформатировать все значения с одной единицей измерения."""
    formatter = make_formatter(unit)
    return list(map(formatter, values))

