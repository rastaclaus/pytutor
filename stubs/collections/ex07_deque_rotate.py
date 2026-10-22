"""Упражнение 7. ``deque.rotate`` и превращение списка в кольцо. Уровень 3.

Метод ``rotate(n)`` сдвигает элементы очереди: при ``n > 0`` правый край
уходит влево («вправо по кругу»), при ``n < 0`` — наоборот. Это самый простой
способ работать со структурой «кольцо»: плейлисты, планировщики, лифты,
карусели.

Также полезны ``index`` (позиция элемента) и ``remove`` (удаление первого
вхождения).
"""

from __future__ import annotations

from collections import deque


def rotate_right(items: list[int], n: int) -> list[int]:
    """Сдвинуть список вправо по кругу на ``n`` позиций.

    ``rotate_right([1, 2, 3, 4], 1)`` -> ``[4, 1, 2, 3]``. Для ``n`` больше
    длины — сдвинуть на ``n % len`` (для непустого списка).
    """
    raise NotImplementedError


def rotate_left(items: list[int], n: int) -> list[int]:
    """Сдвинуть список влево по кругу на ``n`` позиций.

    ``rotate_left([1, 2, 3, 4], 1)`` -> ``[2, 3, 4, 1]``.
    """
    raise NotImplementedError


def next_after(items: list[str], current: str) -> str | None:
    """Вернуть следующий элемент по кругу после ``current``.

    ``next_after(["a", "b", "c"], "b")`` -> ``"c"``; ``next_after(["a", "b",
    "c"], "c")`` -> ``"a"``. Если ``current`` нет в списке — ``None``.
    """
    raise NotImplementedError


def remove_all(dq: deque[int], value: int) -> deque[int]:
    """Удалить из ``dq`` все вхождения ``value``.

    Вернуть ту же очередь. ``deque.remove`` убирает только одно вхождение, так
    что может понадобиться повторять удаление.
    """
    raise NotImplementedError


def rotate_until_first(dq: deque[int], value: int) -> deque[int]:
    """Вращать ``dq`` вправо, пока ``value`` не окажется первым элементом.

    Если ``value`` нет в очереди — вернуть очередь без изменений. Вернуть ту же
    очередь.
    """
    raise NotImplementedError
