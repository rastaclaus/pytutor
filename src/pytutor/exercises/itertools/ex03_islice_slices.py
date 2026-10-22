"""Упражнение 3. Срезы итераторов: ``islice``. Уровень 2.

``islice(iterable, stop)`` и ``islice(iterable, start, stop, step)`` работают как
срезы, но **по итератору**, а не по последовательности:

* отрицательных индексов нет — ``islice(it, -1)`` бросает ``ValueError``;
* ``start`` и ``stop`` могут быть ``None`` (``None`` в ``stop`` — «до конца»);
* итератор потребляется: после ``islice`` он уже сдвинут вперёд;
* для последовательностей ``islice`` тоже работает, но выгода — именно в ленивости.

Реализуйте функции так, чтобы они не превращали вход в список.
"""

from __future__ import annotations

from itertools import islice
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator


def head(n: int, iterable: Iterable[int]) -> list[int]:
    """Вернуть первые ``n`` элементов потока."""
    raise NotImplementedError


def drop_first(n: int, iterable: Iterable[int]) -> list[int]:
    """Всё, кроме первых ``n`` элементов.

    Подсказка: ``islice(iterable, n, None)``.
    """
    raise NotImplementedError


def every_nth(n: int, iterable: Iterable[int]) -> list[int]:
    """Каждый ``n``-й элемент, начиная с нулевого.

    ``every_nth(3, range(7))`` даёт ``[0, 3, 6]``. Для ``n <= 0`` —
    ``ValueError``.
    """
    raise NotImplementedError


def nth(iterable: Iterable[int], index: int, default: int | None = None) -> int | None:
    """Вернуть элемент с номером ``index``, не читая весь поток.

    Если элемента нет — ``default``. Для ``index < 0`` — ``ValueError``.
    """
    raise NotImplementedError


def first_three(iterable: Iterable[int]) -> Iterator[int]:
    """Вернуть именно итератор первых трёх элементов (не список)."""
    raise NotImplementedError
