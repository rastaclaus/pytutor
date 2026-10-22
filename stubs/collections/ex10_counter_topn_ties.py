"""Упражнение 10. Top-N с развязкой ничьих. Уровень 4.

``Counter.most_common(n)`` возвращает ``n`` самых частых элементов, но при
равных частотах порядок среди них не гарантирован (на практике это порядок
первого вхождения). Во многих задачах нужен детерминированный порядок: при
равенстве частот сортируем по ключу (например, по алфавиту).

Задача — реализовать выборку top-N и bottom-N с чётким правилом развязки.
"""

from __future__ import annotations

from collections import Counter
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def top_n(counter: Counter[str], n: int) -> list[tuple[str, int]]:
    """Вернуть ``n`` самых частых пар ``(ключ, частота)``.

    Сортировка: по убыванию частоты; при равенстве — по возрастанию ключа
    (лексикографически). Если ``n`` больше числа уникальных элементов — вернуть
    все.
    """
    raise NotImplementedError


def bottom_n(counter: Counter[str], n: int) -> list[tuple[str, int]]:
    """Вернуть ``n`` самых редких пар ``(ключ, частота)``.

    Сортировка: по возрастанию частоты; при равенстве — по возрастанию ключа.
    Если ``n`` больше числа уникальных элементов — вернуть все.
    """
    raise NotImplementedError


def top_n_by_key(counter: Counter[str], n: int) -> list[tuple[str, int]]:
    """Вернуть первые ``n`` пар после сортировки только по ключу (по возрастанию)."""
    raise NotImplementedError


def rank_words(text: str, n: int) -> list[tuple[str, int]]:
    """Вернуть top-N самых частых слов в ``text``.

    Разбить текст на слова по пробелам (регистр игнорировать). Использовать
    ``top_n``.
    """
    raise NotImplementedError
