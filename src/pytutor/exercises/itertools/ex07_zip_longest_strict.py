"""Упражнение 7. Неравные длины: ``zip_longest`` и ``zip(strict=True)``. Уровень 4.

Встроенный ``zip`` молча останавливается по самому короткому входу — это удобно,
но иногда ошибка в данных должна быть видна. С Python 3.10 у ``zip`` есть
``strict=True``: при разной длине он бросает ``ValueError`` **после** того, как
отдал все пары до конца короткого входа.

``itertools.zip_longest`` идёт до самого длинного входа и подставляет
``fillvalue`` (по умолчанию ``None``) на место недостающих элементов. Частный
случай: один и тот же итератор, переданный несколько раз, распиливает поток на
колонки — это рецепт ``grouper`` из документации.

Важно про тексты ошибок: ``zip(strict=True)`` формирует сообщение сам (в нём есть
слово ``shorter``), а режимы ``batched`` — своё (``at least one`` / ``incomplete
batch``). Переупаковывать эти исключения не нужно.
"""

from __future__ import annotations

from itertools import zip_longest
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def merge_uneven(left: Iterable[str], right: Iterable[int]) -> list[tuple[str, int | None]]:
    """Слить неравные потоки, подставляя ``None`` вместо пропусков.

    ``merge_uneven("ABC", [1, 2])`` -> ``[("A", 1), ("B", 2), ("C", None)]``;
    ``merge_uneven("A", [1, 2, 3])`` -> ``[("A", 1), (None, 2), (None, 3)]``;
    ``merge_uneven("", [])`` -> ``[]``.

    Подсказка: у ``zip_longest`` ``fillvalue`` по умолчанию как раз ``None``.
    """
    raise NotImplementedError


def merge_with_fill(left: Iterable[str], right: Iterable[int], fill: int) -> list[tuple[str, int]]:
    """Слить неравные потоки, подставляя ``fill`` вместо пропусков.

    ``merge_with_fill("AB", [1, 2, 3], 0)`` -> ``[("A", 1), ("B", 2), (0, 3)]``;
    ``merge_with_fill("ABC", [1], -1)`` -> ``[("A", 1), ("B", -1), ("C", -1)]``;
    ``merge_with_fill("", [], 0)`` -> ``[]``.

    ``fill`` подставляется на место недостающего элемента любой из сторон:
    в первом примере им стал левый (``str``), во втором — правый (``int``).

    Подсказка: ``zip_longest(left, right, fillvalue=fill)``.
    """
    raise NotImplementedError


def zip_strict(left: Iterable[int], right: Iterable[int]) -> list[tuple[int, int]]:
    """Слить потоки, упав с ``ValueError`` при разной длине.

    ``zip_strict([1, 2], [3, 4])`` -> ``[(1, 3), (2, 4)]``;
    ``zip_strict([], [])`` -> ``[]``;
    ``zip_strict([1, 2], [3])`` -> ``ValueError`` (в сообщении есть ``shorter``).

    Ошибку не перехватывайте и не заменяйте своей: тест ищет stdlib-текст.

    Подсказка: ``zip(left, right, strict=True)``.
    """
    raise NotImplementedError


def same_length(left: Iterable[int], right: Iterable[int]) -> bool:
    """Проверить, что длины потоков совпадают, ничего не материализуя.

    ``same_length([1, 2], [3, 4])`` -> ``True``;
    ``same_length([], [])`` -> ``True``;
    ``same_length([1, 2], [3])`` -> ``ValueError`` (в сообщении есть ``shorter``).

    Обратите внимание: при несовпадении длин функция **не возвращает** ``False``,
    а пробрасывает ``ValueError`` от ``zip(strict=True)`` — так требует тест.

    Подсказка: пройдите потоком ``zip(left, right, strict=True)``, ничего не
    сохраняя (``for _ in ...: pass``), и верните ``True``; исключение уйдёт само.
    """
    raise NotImplementedError


def grouper(items: Iterable[str], size: int) -> list[tuple[str, ...]]:
    """Нарезать поток на кортежи длины ``size``, заполняя хвост ``""``.

    ``grouper("ABCDEFG", 3)`` -> ``[("A","B","C"), ("D","E","F"), ("G","","")]``;
    ``grouper("", 2)`` -> ``[]`` — пустой вход не даёт ни одной группы;
    ``grouper("AB", 2)`` -> ``[("A", "B")]`` — ровно полная группа;
    ``grouper("AB", 0)`` -> ``ValueError`` (в сообщении есть ``size``).

    Подсказка: рецепт ``zip_longest(*[iter(items)] * size, fillvalue="")``.
    Для ``size < 1`` бросьте ``ValueError`` сами: ``range``/``*`` молча дадут
    пустой результат, а задание требует ошибку.
    """
    raise NotImplementedError


def transpose(matrix: list[list[int]]) -> list[tuple[int, ...]]:
    """Транспонировать прямоугольную матрицу.

    ``transpose([[1, 2, 3], [4, 5, 6]])`` -> ``[(1, 4), (2, 5), (3, 6)]``;
    ``transpose([])`` -> ``[]`` — пустая матрица, а не ошибка;
    ``transpose([[1], [2]])`` -> ``[(1, 2)]`` — один столбец;
    ``transpose([[1, 2], [3]])`` -> ``ValueError`` (в сообщении есть ``zip``).

    Подсказка: ``zip(*matrix, strict=True)``; пустую матрицу проверьте
    отдельно, потому что ``zip()`` без аргументов дал бы пустой результат,
    но ``strict=True`` с ним бессмысленен.
    """
    raise NotImplementedError
