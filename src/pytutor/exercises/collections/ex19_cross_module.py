"""Упражнение 19. Кросс-наборная связка: collections × itertools × functools. Уровень 7.

Модуль ``collections`` редко работает в одиночку: его типы отлично сочетаются с
``itertools`` и ``functools``. Здесь мы соединяем наборы:

* ``itertools.groupby`` + ``Counter`` — агрегация серий;
* ``itertools.batched`` + ``Counter`` — частоты по пакетам;
* ``functools.partial`` + ``defaultdict`` — фабрики с параметрами;
* ``itertools.count``/``islice`` + ``deque`` — потоковый хвост.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from functools import partial
from itertools import batched, groupby
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator


def count_by_value(values: Iterable[int]) -> Counter[int]:
    """Посчитать, сколько раз встречается каждое значение."""
    raise NotImplementedError


def aggregate_runs(values: Iterable[str]) -> list[tuple[str, int]]:
    """Сгруппировать подряд идущие одинаковые значения.

    Вернуть список ``(значение, длина_серии)`` в порядке серий.
    ``aggregate_runs("aaabbc")`` -> ``[("a", 3), ("b", 2), ("c", 1)]``.
    """
    raise NotImplementedError


def chunk_frequencies(values: Iterable[int], size: int) -> list[Counter[int]]:
    """Разбить ``values`` на пакеты по ``size`` и посчитать частоты в каждом.

    ``chunk_frequencies([1, 1, 2, 3, 3, 3], 2)`` -> ``[Counter({1: 2}),
    Counter({2: 1, 3: 1}), Counter({3: 2})]``.
    """
    raise NotImplementedError


def make_incrementing_counter(start: int, step: int) -> Counter[str]:
    """Создать ``Counter``, фабрика которого раздаёт возрастающие значения.

    Каждый **новый** ключ получает следующее значение из последовательности
    ``start, start + step, start + 2 * step, ...``. Повторные обращения к уже
    существующему ключу возвращают сохранённое значение.

    Подсказка: ``itertools.count`` + ``functools.partial`` как фабрика
    ``defaultdict``.
    """
    raise NotImplementedError


def tail_stream(values: Iterable[int], size: int) -> Iterator[list[int]]:
    """Потоково выдавать хвост из последних ``size`` элементов.

    После каждого нового элемента выдаётся текущее окно:
    ``list(tail_stream([1, 2, 3], 2))`` -> ``[[1], [1, 2], [2, 3]]``.
    """
    raise NotImplementedError
