"""Упражнение 5. Бегущие итоги: ``accumulate``. Уровень 3.

``accumulate(iterable, func=operator.add, *, initial=None)`` отдаёт
промежуточные результаты свёртки: ``p0, p0+p1, p0+p1+p2, ...``.
Это как ``functools.reduce``, но с историей каждого шага.

* ``func`` — любая бинарная функция (``operator.mul``, ``max``, ``min``);
* ``initial`` добавляет стартовое значение в начало результата, поэтому
  элементов становится на один больше, чем во входе;
* ``accumulate`` ленив, работает с бесконечными потоками.

``functools.reduce`` даёт только последний элемент — если нужен лишь итог,
используйте именно его.

Общее правило: при пустом входе ``accumulate`` без ``initial`` даёт ``[]``,
а с ``initial`` — ``[initial]``.
"""

from __future__ import annotations

import operator
from itertools import accumulate
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def running_sum(numbers: Iterable[int]) -> list[int]:
    """Бегущая сумма: ``[1, 2, 3] -> [1, 3, 6]``.

    ``running_sum([])`` -> ``[]``;
    ``running_sum([5])`` -> ``[5]`` — один элемент даёт один результат.
    """
    raise NotImplementedError


def running_sum_with_start(start: int, numbers: Iterable[int]) -> list[int]:
    """Бегущая сумма с начальным значением ``start``.

    ``running_sum_with_start(10, [1, 2])`` -> ``[10, 11, 13]``;
    ``running_sum_with_start(42, [])`` -> ``[42]`` — ``initial`` попадает в
    результат даже для пустого входа;
    ``running_sum_with_start(0, [1])`` -> ``[0, 1]`` — длина на единицу больше
    длины входа.

    Подсказка: ``accumulate(numbers, initial=start)``.
    """
    raise NotImplementedError


def running_product(numbers: Iterable[int]) -> list[int]:
    """Бегущее произведение.

    ``running_product([2, 3, 4])`` -> ``[2, 6, 24]``;
    ``running_product([])`` -> ``[]``;
    ``running_product([0, 5])`` -> ``[0, 0]`` — ноль обнуляет всё после себя.

    Подсказка: ``accumulate(numbers, operator.mul)``.
    """
    raise NotImplementedError


def running_max(numbers: Iterable[int]) -> list[int]:
    """Бегущий максимум: ``[3, 1, 4] -> [3, 3, 4]``.

    ``running_max([3, 1, 4, 2])`` -> ``[3, 3, 4, 4]``;
    ``running_max([])`` -> ``[]``;
    ``running_max([-5, -1])`` -> ``[-5, -1]``.

    Подсказка: ``accumulate(numbers, max)``.
    """
    raise NotImplementedError


def running_balance(transactions: Iterable[int]) -> list[int]:
    """Баланс после каждой транзакции (стартовый баланс — 0).

    ``running_balance([100, -30, -50])`` -> ``[0, 100, 70, 20]`` — нулевой
    баланс идёт первым элементом результата;
    ``running_balance([])`` -> ``[0]``;
    ``running_balance([-10])`` -> ``[0, -10]`` — уходить в минус можно.

    Подсказка: ``initial=0`` добавляет нулевой баланс в начало.
    """
    raise NotImplementedError


def final_sum(numbers: Iterable[int]) -> int:
    """Только итоговая сумма (без истории), через ``functools.reduce``.

    ``final_sum([1, 2, 3])`` -> ``6``;
    ``final_sum([])`` -> ``0`` — нейтральный элемент передан как
    ``initializer``.
    """
    raise NotImplementedError


def running_pairwise_ratio(numbers: Iterable[int]) -> list[float]:
    """Бегущее отношение: первый элемент как есть, далее ``acc / value``.

    ``running_pairwise_ratio([100, 2, 5])`` -> ``[100.0, 50.0, 10.0]``:
    ``100 / 2 = 50``, затем ``50 / 5 = 10``;
    ``running_pairwise_ratio([7])`` -> ``[7]`` — делить не на что;
    ``running_pairwise_ratio([])`` -> ``[]``.

    То есть ``result[0] == numbers[0]``, а ``result[i] == result[i-1] /
    numbers[i]`` для ``i >= 1``. Длина результата равна длине входа.

    Подсказка: ``accumulate`` не умеет «первый без операции», поэтому
    передайте первый элемент как ``initial`` и сверните только хвост:
    ``accumulate(values[1:], operator.truediv, initial=values[0])``.
    """
    raise NotImplementedError
