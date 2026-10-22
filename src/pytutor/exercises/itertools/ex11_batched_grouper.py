"""Упражнение 11. Батчи: ``batched`` и рецепт ``grouper``. Уровень 5.

``batched(iterable, n)`` (3.12+) режет поток на кортежи длины ``n``; последний
батч может быть короче. Он ленивый: забирает из источника ровно столько, сколько
нужно для очередного батча. Начиная с 3.13 есть ``strict=True`` —
неполный последний батч превращается в ``ValueError``.

Три классических поведения для хвоста:

* ``batched`` — оставить короткий хвост как есть;
* ``batched(..., strict=True)`` — упасть;
* рецепт ``grouper`` на ``zip_longest(*[iter(it)] * n, fillvalue=...)`` —
  дополнить хвост;
* ``zip(*[iter(it)] * n)`` — отбросить неполный хвост.

Тот же приём с ``chain.from_iterable`` позволяет «переформовать» плоский поток
в строки матрицы: ``reshape``.
"""

from __future__ import annotations

from itertools import batched, chain, zip_longest
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def batch(items: Iterable[str], size: int) -> list[tuple[str, ...]]:
    """Нарезать поток на батчи, оставив короткий хвост.

    Для ``size < 1`` — ``ValueError``.
    """
    raise NotImplementedError


def batch_strict(items: Iterable[str], size: int) -> list[tuple[str, ...]]:
    """Нарезать поток, упав с ``ValueError``, если хвост неполный."""
    raise NotImplementedError


def batch_lengths(items: Iterable[str], size: int) -> list[int]:
    """Длины получившихся батчей.

    ``batch_lengths("ABCDEFG", 3)`` даёт ``[3, 3, 1]``.
    """
    raise NotImplementedError


def pad_batches(items: Iterable[str], size: int, fill: str) -> list[tuple[str, ...]]:
    """Нарезать поток, дополнив хвост значением ``fill`` (рецепт ``grouper``)."""
    raise NotImplementedError


def trim_batches(items: Iterable[str], size: int) -> list[tuple[str, ...]]:
    """Нарезать поток, отбросив неполный хвост."""
    raise NotImplementedError


def reshape(rows: Iterable[Iterable[int]], columns: int) -> list[tuple[int, ...]]:
    """Переформовать поток значений в строки по ``columns`` элементов.

    ``reshape([[0, 1], [2, 3], [4, 5]], 3)`` даёт ``[(0, 1, 2), (3, 4, 5)]``.
    Хвост, не заполнивший строку, отбрасывается.
    """
    raise NotImplementedError
