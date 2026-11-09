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

Общее правило: ``map``/``zip`` без ``strict`` останавливаются по самому короткому
входу, поэтому обрезать ``repeat`` вручную не нужно.
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
    """Применить ``func`` к каждой паре аргументов.

    ``apply_pairs(pow, [(2, 5), (3, 2)])`` -> ``[32, 9]``;
    ``apply_pairs(lambda a, b: a - b, [(5, 3)])`` -> ``[2]``;
    ``apply_pairs(pow, [])`` -> ``[]``.

    Подсказка: ``starmap`` распаковывает кортеж в позиционные аргументы.
    """
    raise NotImplementedError


def dot_product(left: Iterable[int], right: Iterable[int]) -> int:
    """Скалярное произведение через ``starmap`` и ``operator.mul``.

    ``dot_product([1, 2, 3], [4, 5, 6])`` -> ``32``;
    ``dot_product([], [])`` -> ``0``;
    ``dot_product([1, 2], [10])`` -> ``10`` — ``zip`` останавливается по
    короткому входу, ошибки нет.

    Материализовать входы целиком нельзя: допускаются генераторы.

    Подсказка: ``sum(starmap(operator.mul, zip(left, right)))``. Именно
    ``starmap``, а не ``map``: пара из ``zip`` должна стать двумя аргументами.
    """
    raise NotImplementedError


def total_cost(rows: Iterable[tuple[int, int]]) -> int:
    """Сумма ``price * quantity`` по строкам ``(price, quantity)``.

    ``total_cost([(2, 3), (10, 2)])`` -> ``26``;
    ``total_cost([])`` -> ``0``;
    ``total_cost([(0, 5)])`` -> ``0``.

    Подсказка: ``sum(starmap(operator.mul, rows))``; каждая строка уже кортеж,
    поэтому ``zip`` не нужен.
    """
    raise NotImplementedError


def repeat_apply(func: Callable[[str], str], value: str, times: int) -> list[str]:
    """Применить ``func`` к ``value`` ровно ``times`` раз (через ``map`` + ``repeat``).

    ``repeat_apply(str.upper, "ab", 3)`` -> ``["AB", "AB", "AB"]``;
    ``repeat_apply(str.upper, "ab", 0)`` -> ``[]``;
    ``repeat_apply(str.upper, "ab", -1)`` -> ``[]`` — отрицательное число
    повторов трактуется как ноль (``repeat`` сам бросил бы ``ValueError``).

    Подсказка: ``map(func, repeat(value, max(times, 0)))``.
    """
    raise NotImplementedError


def pair_with_constant(values: Iterable[str], constant: int) -> list[tuple[str, int]]:
    """Приписать каждому значению одну и ту же константу.

    ``pair_with_constant(["a", "b"], 0)`` -> ``[("a", 0), ("b", 0)]``;
    ``pair_with_constant([], 1)`` -> ``[]``;
    ``pair_with_constant(["a"], -7)`` -> ``[("a", -7)]``.

    Подсказка: ``zip(values, repeat(constant))`` — второй поток бесконечен,
    но ``zip`` остановится по первому.
    """
    raise NotImplementedError


def apply_all(functions: Iterable[Callable[[int], int]], value: int) -> list[int]:
    """Применить каждую функцию к одному и тому же ``value``.

    ``apply_all([abs, lambda value: value + 1], -3)`` -> ``[3, -2]``;
    ``apply_all([], 5)`` -> ``[]``;
    ``apply_all([lambda value: value * 2], 4)`` -> ``[8]``.

    Подсказка: ``map`` умеет несколько итерируемых аргументов:
    ``map(operator.call, functions, repeat(value))``.
    """
    raise NotImplementedError


def make_formatter(unit: str) -> Callable[[int], str]:
    """Вернуть функцию ``value -> "value unit"`` через ``functools.partial``.

    ``make_formatter("kg")(5)`` -> ``"5 kg"``;
    ``make_formatter("m")(2)`` -> ``"2 m"``.

    Подсказка: ``unit`` у ``_format_measurement`` — именованный (keyword-only)
    аргумент, поэтому фиксировать его нужно по имени: ``unit=unit``.
    """
    raise NotImplementedError


def format_values(values: Iterable[int], unit: str) -> list[str]:
    """Отформатировать все значения с одной единицей измерения.

    ``format_values([1, 2], "s")`` -> ``["1 s", "2 s"]``;
    ``format_values([], "s")`` -> ``[]``.

    Подсказка: ``map(make_formatter(unit), values)`` — форматтер готовится
    один раз, а не внутри каждой итерации.
    """
    raise NotImplementedError
