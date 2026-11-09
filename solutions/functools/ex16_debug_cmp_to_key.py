"""Эталон упражнения 16 (functools): найди баг — cmp_to_key (исправленная версия).

Три бага исходной версии:

1. ``compare_natural`` сравнивал строки лексикографически, игнорируя
   подготовленный ``_natural_key``: ``"file10" < "file2"`` как текст;
2. ``natural_sort`` использовала лексикографический компаратор вместо ключа
   на базе ``_natural_key``;
3. ``sort_files`` сортировала с ``reverse=True`` — порядок оказывался обратным
   заданному (стабильность при reverse тоже меняет смысл развязок).
"""

from __future__ import annotations

import re
from functools import cmp_to_key

_CHUNK = re.compile(r"(\d+)")


def _natural_key(text: str) -> list[tuple[int, int | str]]:
    """Разбить строку на куски: числа — как числа, остальное — как текст."""
    parts: list[tuple[int, int | str]] = []
    for index, chunk in enumerate(_CHUNK.split(text)):
        if index % 2 == 1:
            parts.append((1, int(chunk)))
        elif chunk:
            parts.append((0, chunk))
    return parts


def _compare_keys(a: list[tuple[int, int | str]], b: list[tuple[int, int | str]]) -> int:
    for left, right in zip(a, b, strict=False):
        if left != right:
            if left[0] != right[0]:
                return -1 if left[0] < right[0] else 1
            return -1 if left[1] < right[1] else 1  # type: ignore[operator]
    return (len(a) > len(b)) - (len(a) < len(b))


def compare_natural(a: str, b: str) -> int:
    """Сравнить две строки «естественно»; возвращает ``-1``/``0``/``1``."""
    return _compare_keys(_natural_key(a), _natural_key(b))


def natural_sort(strings: list[str]) -> list[str]:
    """Отсортировать строки естественно через ``cmp_to_key``."""
    return sorted(strings, key=cmp_to_key(compare_natural))


def sort_files(filenames: list[str]) -> list[str]:
    """Отсортировать имена файлов естественно (стабильно, без reverse)."""
    return natural_sort(filenames)
