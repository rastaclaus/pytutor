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
"""

from __future__ import annotations

import operator
from functools import reduce
from itertools import accumulate
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def running_sum(numbers: Iterable[int]) -> list[int]:
    """Бегущая сумма: ``[1, 2, 3] -> [1, 3, 6]``."""
    return list(accumulate(numbers, operator.add))


def running_sum_with_start(start: int, numbers: Iterable[int]) -> list[int]:
    """Бегущая сумма с начальным значением ``start``.

    Для пустого входа результат — ``[start]``.
    """
    return list(accumulate(numbers, operator.add, initial=start))


def running_product(numbers: Iterable[int]) -> list[int]:
    """Бегущее произведение."""
    return list(accumulate(numbers, operator.mul))


def running_max(numbers: Iterable[int]) -> list[int]:
    """Бегущий максимум: ``[3, 1, 4] -> [3, 3, 4]``."""
    return list(accumulate(numbers, max))


def running_balance(transactions: Iterable[int]) -> list[int]:
    """Баланс после каждой транзакции (стартовый баланс — 0).

    Подсказка: ``initial=0`` добавляет нулевой баланс в начало.
    """
    return list(accumulate(transactions, operator.add, initial=0))


def final_sum(numbers: Iterable[int]) -> int:
    """Только итоговая сумма (без истории), через ``functools.reduce``."""
    return reduce(operator.add, numbers, 0)


def running_pairwise_ratio(numbers: Iterable[int]) -> list[float]:
    """Бегущее отношение ``acc / value`` для ненулевых значений.

    Подсказка: подойдёт ``operator.truediv``, но первое значение
    должно остаться как есть — проверьте, что даёт ``accumulate``
    с такой функцией и ``initial``.
    """
    return list(accumulate(numbers, operator.truediv))
