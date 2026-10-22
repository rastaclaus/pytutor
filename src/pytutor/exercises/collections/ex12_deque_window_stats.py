"""Упражнение 12. Скользящее окно: статистика в потоке. Уровень 5.

Когда данные приходят потоком и нужно считать статистику по последним ``N``
элементам, идеальный инструмент — ``deque(maxlen=N)``: добавление нового элемента
автоматически вытесняет самый старый, и окно всегда имеет ровно ``N`` элементов
(после разогрева).

Здесь мы строим «живые» скользящие статистики: среднее, минимум и максимум, а
также отклонение от среднего. Все вычисления — в потоке, без материализации
всего входа.
"""

from __future__ import annotations

from collections import deque
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator


def moving_average(values: Iterable[float], size: int) -> Iterator[float]:
    """Генератор скользящих средних по последним ``size`` элементам.

    ``moving_average([1, 2, 3, 4], 2)`` -> ``1.5, 2.5, 3.5``. Пока элементов
    меньше ``size``, среднее не выдаётся. Для ``size <= 0`` — ``ValueError``.
    """
    raise NotImplementedError


def moving_max(values: Iterable[int], size: int) -> Iterator[int]:
    """Генератор максимумов в каждом окне из последних ``size`` элементов."""
    raise NotImplementedError


def moving_min(values: Iterable[int], size: int) -> Iterator[int]:
    """Генератор минимумов в каждом окне из последних ``size`` элементов."""
    raise NotImplementedError


def deviation_from_mean(values: Iterable[float], size: int) -> Iterator[float]:
    """Генератор отклонений текущего элемента от среднего по окну.

    Для каждого элемента, начиная с ``size``-го, вернуть
    ``элемент - среднее_окна``.
    """
    raise NotImplementedError
