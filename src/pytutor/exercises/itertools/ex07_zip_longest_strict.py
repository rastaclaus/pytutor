"""Упражнение 7. Неравные длины: ``zip_longest`` и ``zip(strict=True)``. Уровень 4.

Встроенный ``zip`` молча останавливается по самому короткому входу — это удобно,
но иногда ошибка в данных должна быть видна. С Python 3.10 у ``zip`` есть
``strict=True``: при разной длине он бросает ``ValueError`` **после** того, как
отдал все пары до конца короткого входа.

``itertools.zip_longest`` идёт до самого длинного входа и подставляет
``fillvalue`` (по умолчанию ``None``) на место недостающих элементов. Частный
случай: один и тот же итератор, переданный несколько раз, распиливает поток на
колонки — это рецепт ``grouper`` из документации.
"""

from __future__ import annotations

from itertools import zip_longest
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def merge_uneven(left: Iterable[str], right: Iterable[int]) -> list[tuple[str, int | None]]:
    """Слить неравные потоки, подставляя ``None`` вместо пропусков."""
    return list(zip_longest(left, right))


def merge_with_fill(left: Iterable[str], right: Iterable[int], fill: int) -> list[tuple[str | int, int]]:
    """Слить неравные потоки, подставляя ``fill`` вместо пропусков."""
    return list(zip_longest(left, right, fillvalue=fill))


def zip_strict(left: Iterable[int], right: Iterable[int]) -> list[tuple[int, int]]:
    """Слить потоки, упав с ``ValueError`` при разной длине."""
    return list(zip(left, right, strict=True))


def same_length(left: Iterable[int], right: Iterable[int]) -> bool:
    """Проверить, что длины потоков совпадают, ничего не материализуя.

    Подсказка: ``zip_strict`` + ``try/except``; результат ``zip`` не нужен.
    """
    _ = zip_strict(left, right)
    return True



def grouper(items: Iterable[str], size: int) -> list[tuple[str, ...]]:
    """Нарезать поток на кортежи длины ``size``, заполняя хвост ``""``.

    ``grouper("ABCDEFG", 3)`` даёт ``("A","B","C"), ("D","E","F"), ("G","","")``.
    """
    if size < 1:
        msg = "size must be > 1"
        raise ValueError(msg)

    iterators = [iter(items)] * size
    return list(zip_longest(*iterators, fillvalue=""))




def transpose(matrix: list[list[int]]) -> list[tuple[int, ...]]:
    """Транспонировать прямоугольную матрицу.

    Подсказка: ``zip(*matrix, strict=True)``; для пустой матрицы — ``[]``.
    """
    return list(zip(*matrix, strict=True))
