"""Упражнение 8. Соседние пары и скользящее окно. Уровень 4.

``pairwise(iterable)`` отдаёт перекрывающиеся пары ``(p0, p1), (p1, p2), ...``.
На входе короче двух элементов результат пуст. Это самый частый способ считать
разности, скорости и «соседние» переходы без индексов.

Скользящего окна в ``itertools`` нет — его собирают из ``deque(maxlen=N)``:
очередь автоматически вытесняет старый элемент при переполнении. Тот же приём
даёт «хвост» из последних ``N`` элементов.

Обратите внимание: ``pairwise`` возвращает генератор, поэтому результат нужно
материализовать самим.
"""

from __future__ import annotations

from collections import deque
from itertools import islice, pairwise
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator


def adjacent_pairs(values: Iterable[str]) -> list[tuple[str, str]]:
    """Все соседние пары подряд."""
    raise NotImplementedError


def differences(values: Iterable[int]) -> list[int]:
    """Разности соседних элементов: ``[1, 4, 9] -> [3, 5]``."""
    raise NotImplementedError


def all_increasing(values: Iterable[int]) -> bool:
    """Проверить, что последовательность строго возрастает.

    Для последовательностей длиной 0 и 1 — ``True``.
    """
    raise NotImplementedError


def sliding_window(values: Iterable[int], size: int) -> list[tuple[int, ...]]:
    """Скользящее окно длины ``size``.

    ``sliding_window("ABCDEFG", 3)`` даёт ``ABC BCD CDE DEF EFG``. Для ``size <= 0``
    — ``ValueError``; если элементов меньше ``size`` — пустой список.
    """
    raise NotImplementedError


def tail(values: Iterable[int], size: int) -> list[int]:
    """Последние ``size`` элементов, без материализации всего входа.

    Подсказка: ``deque(values, maxlen=size)``; для ``size <= 0`` — пустой список.
    """
    raise NotImplementedError


def window_sums(values: Iterable[int], size: int) -> list[int]:
    """Суммы по каждому скользящему окну длины ``size``.

    Подсказка: переиспользуйте ``sliding_window``.
    """
    raise NotImplementedError


def pairwise_iter(values: Iterable[int]) -> Iterator[tuple[int, int]]:
    """Вернуть именно итератор пар, не список."""
    raise NotImplementedError


def first_window_above(values: Iterable[int], size: int, limit: int) -> tuple[int, ...] | None:
    """Первое окно длины ``size``, сумма которого больше ``limit``.

    Подсказка: ``next`` по генератору, ``default=None``.
    """
    raise NotImplementedError
