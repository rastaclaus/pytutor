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

Тексты ошибок принадлежат stdlib, и переупаковывать их не нужно:
``batched(..., 0)`` даёт сообщение со словами ``at least one``, а
``strict=True`` — ``incomplete batch``.
"""

from __future__ import annotations

from itertools import batched, chain, zip_longest
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def batch(items: Iterable[str], size: int) -> list[tuple[str, ...]]:
    """Нарезать поток на батчи, оставив короткий хвост.

    ``batch("ABCDEFG", 3)`` -> ``[("A","B","C"), ("D","E","F"), ("G",)]``;
    ``batch("", 3)`` -> ``[]``;
    ``batch("AB", 3)`` -> ``[("A", "B")]`` — неполный единственный батч
    остаётся как есть;
    ``batch("AB", 0)`` -> ``ValueError`` (в сообщении есть ``at least one``).

    Для ``size < 1`` ничего не проверяйте вручную — ошибку даёт сам ``batched``.

    Подсказка: ``list(batched(items, size))``.
    """
    raise NotImplementedError


def batch_strict(items: Iterable[str], size: int) -> list[tuple[str, ...]]:
    """Нарезать поток, упав с ``ValueError``, если хвост неполный.

    ``batch_strict("ABCDEF", 3)`` -> ``[("A","B","C"), ("D","E","F")]``;
    ``batch_strict("ABCDEFG", 3)`` -> ``ValueError`` (в сообщении есть
    ``incomplete batch``);
    ``batch_strict("", 3)`` -> ``[]`` — пустой вход не даёт хвоста.

    Подсказка: ``batched(items, size, strict=True)``.
    """
    raise NotImplementedError


def batch_lengths(items: Iterable[str], size: int) -> list[int]:
    """Длины получившихся батчей.

    ``batch_lengths("ABCDEFG", 3)`` -> ``[3, 3, 1]``;
    ``batch_lengths("", 3)`` -> ``[]``;
    ``batch_lengths("AB", 3)`` -> ``[2]``.

    Подсказка: переиспользуйте ``batch`` и возьмите ``len`` от каждого батча.
    """
    raise NotImplementedError


def pad_batches(items: Iterable[str], size: int, fill: str) -> list[tuple[str, ...]]:
    """Нарезать поток, дополнив хвост значением ``fill`` (рецепт ``grouper``).

    ``pad_batches("ABCDEFG", 3, "-")`` -> ``[("A","B","C"), ("D","E","F"),
    ("G","-","-")]``;
    ``pad_batches("", 3, "-")`` -> ``[]``;
    ``pad_batches("AB", 3, "-")`` -> ``[("A", "B", "-")]``;
    ``pad_batches("AB", 0, "-")`` -> ``ValueError`` (в сообщении есть ``size``).

    Подсказка: ``zip_longest(*[iter(items)] * size, fillvalue=fill)``. Для
    ``size < 1`` бросьте ``ValueError`` сами: иначе ``*[]`` даст пустой ``zip``
    и молчаливый ``[]``.
    """
    raise NotImplementedError


def trim_batches(items: Iterable[str], size: int) -> list[tuple[str, ...]]:
    """Нарезать поток, отбросив неполный хвост.

    ``trim_batches("ABCDEFG", 3)`` -> ``[("A","B","C"), ("D","E","F")]``;
    ``trim_batches("AB", 3)`` -> ``[]`` — полных батчей нет;
    ``trim_batches("", 3)`` -> ``[]``;
    ``trim_batches("AB", 0)`` -> ``ValueError`` (в сообщении есть ``size``).

    Подсказка: ``zip(*[iter(items)] * size)`` — короткий ``zip`` сам отбросит
    хвост; добавьте проверку ``size < 1``, иначе результат молча пустой.
    """
    raise NotImplementedError


def reshape(rows: Iterable[Iterable[int]], columns: int) -> list[tuple[int, ...]]:
    """Переформовать поток значений в строки по ``columns`` элементов.

    ``reshape([[0, 1], [2, 3], [4, 5]], 3)`` -> ``[(0, 1, 2), (3, 4, 5)]`` —
    границы строк не важны, важен общий плоский поток;
    ``reshape([[0, 1], [2, 3]], 3)`` -> ``[(0, 1, 2)]`` — хвост отброшен;
    ``reshape([[0], [1]], 3)`` -> ``[]``;
    ``reshape([], 3)`` -> ``[]``;
    ``reshape([[0]], 0)`` -> ``ValueError`` (в сообщении есть ``columns``).

    Подсказка: ``zip(*[iter(chain.from_iterable(rows))] * columns)`` — тот же
    приём, что и в ``trim_batches``, но вход сначала выпрямляется на уровень.
    """
    raise NotImplementedError
