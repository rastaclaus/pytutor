"""Упражнение 10. Разветвление потока: ``tee``. Уровень 5.

``tee(iterable, n)`` возвращает ``n`` независимых итераторов над одним источником.
Сам источник читается **один раз**, а прочитанные элементы буферизуются, пока их
не заберут все копии. Отсюда две тонкости:

* если одна копия ушла далеко вперёд, а вторая не читалась, буфер растёт;
* ``tee`` — не копия данных: это «развилка» с общей памятью. Если обе копии
  читаются по очереди, источник не перечитывается.

Ещё трюк: ``tee(iterator, 1)`` делает поток «подглядываемым» — можно узнать
следующий элемент, не сдвигая исходный итератор.
"""

from __future__ import annotations

from itertools import tee
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable, Iterator


def duplicate(values: Iterable[int]) -> tuple[list[int], list[int]]:
    """Вернуть две независимые копии потока в виде списков."""
    raise NotImplementedError


def peek(values: Iterable[str]) -> tuple[str | None, list[str]]:
    """Вернуть первый элемент и поток, начинающийся с него же.

    Для пустого входа — ``(None, [])``.
    """
    raise NotImplementedError


def split_by_predicate(values: Iterable[int], predicate: Callable[[int], bool]) -> tuple[list[int], list[int]]:
    """Разделить поток на «подошло» и «не подошло» за один проход.

    Подсказка: ``tee`` + два ``filter``/``filterfalse`` по копиям.
    """
    raise NotImplementedError


def count_calls_once(values: Iterable[int]) -> tuple[int, int]:
    """Прочитать поток дважды (сумма и количество), не перечитывая источник.

    Вернуть ``(сумма, количество)``.
    """
    raise NotImplementedError


def first_and_last(values: Iterable[int]) -> tuple[int, int] | None:
    """Первый и последний элементы потока.

    Вход может быть генератором — материализовать его целиком нельзя.
    Подсказка: одна копия — на первый элемент, вторая — на «хвост».
    """
    raise NotImplementedError


def lookahead_pairs(values: Iterable[int]) -> list[tuple[int, int | None]]:
    """Пары «текущий элемент и следующий» без потери последнего.

    ``[1, 2, 3]`` даёт ``[(1, 2), (2, 3), (3, None)]``: классическая задача,
    которую ``pairwise`` не решает.
    """
    raise NotImplementedError
