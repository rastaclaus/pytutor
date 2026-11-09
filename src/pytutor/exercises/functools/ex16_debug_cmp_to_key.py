"""Упражнение 16. Найди баг: компаратор и ``cmp_to_key``. Уровень 6.

Ниже — естественная сортировка файлов: ``"file2"`` должен идти раньше
``"file10"``. Реализация выглядит законченной, но содержит **три бага**,
и на части входов она сортирует неправильно или падает. Исправьте их,
не переписывая подход.

Как искать: прогоните тесты (``uv run pytest -k ex16_debug``) и разберите
падения. Полезно вручную прогнать компаратор по парам из падающего теста.

Из упражнения 11: компаратор возвращает ``-1``/``0``/``1``; ``cmp_to_key``
оборачивает его для ``key=``; сортировка ``sorted`` стабильна.
"""

from __future__ import annotations

import re
from functools import cmp_to_key

_CHUNK = re.compile(r"(\d+)")


def _natural_key(text: str) -> list[tuple[int, int | str]]:
    """Разбить строку на куски: числа — как числа, остальное — как текст.

    Уже реализована: ``file2`` -> ``[("file", str), (2, int)]``-подобное
    представление, где числа сравниваются как числа.
    """
    parts: list[tuple[int, int | str]] = []
    for index, chunk in enumerate(_CHUNK.split(text)):
        if index % 2 == 1:
            parts.append((1, int(chunk)))
        elif chunk:
            parts.append((0, chunk))
    return parts


def compare_natural(a: str, b: str) -> int:
    """Сравнить две строки «естественно»; возвращает ``-1``/``0``/``1``."""
    return (a > b) - (a < b)


def natural_sort(strings: list[str]) -> list[str]:
    """Отсортировать строки естественно через ``cmp_to_key``."""
    return sorted(strings, key=cmp_to_key(compare_natural))


def sort_files(filenames: list[str]) -> list[str]:
    """Отсортировать имена файлов естественно; нестабильность недопустима.

    Должна использовать ``natural_sort``.
    """
    return sorted(filenames, key=cmp_to_key(compare_natural), reverse=True)
