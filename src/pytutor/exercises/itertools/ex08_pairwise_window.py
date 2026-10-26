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
    return list(pairwise(values))


def differences(values: Iterable[int]) -> list[int]:
    """Разности соседних элементов: ``[1, 4, 9] -> [3, 5]``."""
    return [b - a for (a, b) in pairwise(values)]


def all_increasing(values: Iterable[int]) -> bool:
    """Проверить, что последовательность строго возрастает.

    Для последовательностей длиной 0 и 1 — ``True``.
    """
    return all(b > a for a, b in pairwise(values))


def sliding_window(values: Iterable[int], size: int) -> list[tuple[int, ...]]:
    """Скользящее окно длины ``size``.

    ``sliding_window("ABCDEFG", 3)`` даёт ``ABC BCD CDE DEF EFG``. Для ``size <= 0``
    — ``ValueError``; если элементов меньше ``size`` — пустой список.
    """
    if size <= 0:
        msg = "size must be > 0"
        raise ValueError(msg)
    iterator = iter(values)
    window = deque(islice(iterator, size), maxlen=size)
    result = [tuple(window)]
    if len(window) < size:
        return []
    for value in iterator:
        window.append(value)
        result.append(tuple(window))
    return result




def tail(values: Iterable[int], size: int) -> list[int]:
    """Последние ``size`` элементов, без материализации всего входа.

    Подсказка: ``deque(values, maxlen=size)``; для ``size <= 0`` — пустой список.
    """
    if size <= 0:
        return []
    return list(deque(values, maxlen=size))



def window_sums(values: Iterable[int], size: int) -> list[int]:
    """Суммы по каждому скользящему окну длины ``size``.

    Подсказка: переиспользуйте ``sliding_window``.
    """
    return [sum(window) for window in sliding_window(values, size)]


def pairwise_iter(values: Iterable[int]) -> Iterator[tuple[int, int]]:
    """Вернуть именно итератор пар, не список."""
    return pairwise(values)


def first_window_above(values: Iterable[int], size: int, limit: int) -> tuple[int, ...] | None:
    """Первое окно длины ``size``, сумма которого больше ``limit``.

    Подсказка: ``next`` по генератору, ``default=None``.
    """
    return next((window for window in sliding_window(values, size) if sum(window) > limit), None)

