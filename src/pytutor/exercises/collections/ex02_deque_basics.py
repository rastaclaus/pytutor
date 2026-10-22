"""Упражнение 2. ``collections.deque`` — очередь и стек. Уровень 1.

``deque`` (double-ended queue) — двусторонняя очередь: быстро добавляет и
удаляет элементы с обоих концов. Для списка операция ``pop(0)`` — O(n), для
``deque`` — O(1).

Ключевые операции: ``append``/``appendleft``, ``pop``/``popleft``, а также
``maxlen`` — ограничение длины: при переполнении старый элемент вытесняется
автоматически.
"""

from __future__ import annotations

from collections import deque
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def make_queue(initial: Iterable[int]) -> deque[int]:
    """Создать ``deque`` из элементов ``initial``."""
    raise NotImplementedError


def queue_push_pop(initial: Iterable[int], values: list[int]) -> list[int]:
    """Повести себя как очередь (FIFO).

    Добавить ``values`` в конец очереди из ``initial``, затем извлечь все
    элементы по одному с начала. Вернуть список извлечённых элементов.
    """
    raise NotImplementedError


def stack_push_pop(initial: Iterable[int], values: list[int]) -> list[int]:
    """Повести себя как стек (LIFO).

    Добавить ``values`` в конец стека из ``initial``, затем извлечь все
    элементы по одному с конца. Вернуть список извлечённых элементов.
    """
    raise NotImplementedError


def bounded_history(values: Iterable[int], maxlen: int) -> list[int]:
    """Вернуть последние ``maxlen`` элементов.

    Для ``maxlen <= 0`` — ``ValueError``.
    """
    raise NotImplementedError


def add_with_limit(history: deque[int], value: int, maxlen: int) -> deque[int]:
    """Добавить ``value`` в ``history``, не превышая ``maxlen``.

    Если длина очереди уже равна ``maxlen``, старый элемент вытесняется.
    Вернуть ту же очередь (nullable).
    """
    raise NotImplementedError
