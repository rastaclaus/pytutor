"""Упражнение 10. Разветвление потока: ``tee``. Уровень 5.

``tee(iterable, n)`` возвращает ``n`` независимых итераторов над одним источником.
Сам источник читается **один раз**, а прочитанные элементы буферизуются, пока их
не заберут все копии. Отсюда две тонкости:

* если одна копия ушла далеко вперёд, а вторая не читалась, буфер растёт;
* ``tee`` — не копия данных: это «развилка» с общей памятью. Если обе копии
  читаются по очереди, источник не перечитывается.

Ещё трюк: ``tee(iterator, 1)`` делает поток «подглядываемым» — можно узнать
следующий элемент, не сдвигая исходный итератор.

Практическое следствие для заданий: если функция возвращает список, а не
итератор, то материал для него берётся из копии ``tee`` — источник при этом
проходится ровно один раз.
"""

from __future__ import annotations

from itertools import tee
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable, Iterator


def duplicate(values: Iterable[int]) -> tuple[list[int], list[int]]:
    """Вернуть две независимые копии потока в виде списков.

    ``duplicate([1, 2, 3])`` -> ``([1, 2, 3], [1, 2, 3])``;
    ``duplicate([])`` -> ``([], [])``;
    ``duplicate(iter([1, 2]))`` -> ``([1, 2], [1, 2])`` — одноразовый итератор
    тоже читается ровно один раз.

    Источник не должен перечитываться: на генераторе с побочным эффектом
    побочный эффект сработает по одному разу на элемент.

    Подсказка: ``left, right = tee(values, 2)``, затем два ``list(...)``.
    Не делайте ``list(values)`` дважды — второй проход по итератору будет пуст.
    """
    raise NotImplementedError


def peek(values: Iterable[str]) -> tuple[str | None, list[str]]:
    """Вернуть первый элемент и поток, начинающийся с него же.

    ``peek(["a", "b"])`` -> ``("a", ["a", "b"])`` — первый элемент **не**
    пропадает из возвращённого списка;
    ``peek([])`` -> ``(None, [])``;
    ``peek(["a"])`` -> ``("a", ["a"])``.

    Подсказка: ``first, rest = tee(values, 2)``; первый элемент возьмите через
    ``next(iter(first), None)`` (``default=None`` обязателен для пустого входа),
    а второй список стройте из ``rest`` — он ещё не сдвинут.
    """
    raise NotImplementedError


def split_by_predicate(values: Iterable[int], predicate: Callable[[int], bool]) -> tuple[list[int], list[int]]:
    """Разделить поток на «подошло» и «не подошло» за один проход.

    ``split_by_predicate([1, 2, 3, 4], lambda value: value % 2 == 0)`` ->
    ``([2, 4], [1, 3])`` — первый список подходящие, второй остальные;
    ``split_by_predicate([], bool)`` -> ``([], [])``;
    ``split_by_predicate([0, 1], bool)`` -> ``([1], [0])``.

    Порядок внутри каждого списка — исходный.

    Подсказка: ``tee`` + два ``filter``/``filterfalse`` по копиям. Не вызывайте
    предикат дважды на элемент и не превращайте вход в список ради второго
    прохода.
    """
    raise NotImplementedError


def count_calls_once(values: Iterable[int]) -> tuple[int, int]:
    """Прочитать поток дважды (сумма и количество), не перечитывая источник.

    ``count_calls_once([1, 2, 3])`` -> ``(6, 3)``;
    ``count_calls_once([])`` -> ``(0, 0)``;
    ``count_calls_once([5])`` -> ``(5, 1)``.

    Вернуть ``(сумма, количество)`` именно в этом порядке.

    Подсказка: ``first, second = tee(values, 2)``; ``sum(first)`` и
    ``sum(1 for _ in second)``.
    """
    raise NotImplementedError


def first_and_last(values: Iterable[int]) -> tuple[int, int] | None:
    """Первый и последний элементы потока.

    ``first_and_last(iter([5, 6, 7]))`` -> ``(5, 7)``;
    ``first_and_last([5])`` -> ``(5, 5)`` — единственный элемент он же первый
    и последний;
    ``first_and_last([])`` -> ``None``.

    Вход может быть генератором — материализовать его целиком нельзя.
    Подсказка: одна копия — на первый элемент, вторая — на «хвост».
    """
    raise NotImplementedError


def lookahead_pairs(values: Iterable[int]) -> list[tuple[int, int | None]]:
    """Пары «текущий элемент и следующий» без потери последнего.

    ``lookahead_pairs([1, 2, 3])`` -> ``[(1, 2), (2, 3), (3, None)]`` —
    классическая задача, которую ``pairwise`` не решает: последний элемент
    тоже попадает в результат, с ``None`` вместо следующего;
    ``lookahead_pairs([1])`` -> ``[(1, None)]``;
    ``lookahead_pairs([])`` -> ``[]``.

    Подсказка: ``current, following = tee(values, 2)``, сдвиньте ``following``
    на один (``next(following, None)``), затем стройте пары
    ``(value, next(following, None))`` в обход ``current``.
    """
    raise NotImplementedError
