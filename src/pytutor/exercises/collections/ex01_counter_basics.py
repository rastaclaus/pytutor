"""Упражнение 1. ``collections.Counter`` — простой счёт частот. Уровень 1.

Counter — это словарь, где ключ — элемент, а значение — сколько раз он
встретился. В отличие от обычного ``dict``, ``Counter`` умеет считать сам и
предоставляет удобные методы: ``most_common`` (топ по частоте), ``total``
(сумма всех счётчиков) и ``elements`` (развёрнутый список элементов с учётом
кратности).

Реализуйте функции ниже. Это разминка: почти везде достаточно одного вызова
метода ``Counter``.
"""

from __future__ import annotations

from collections import Counter
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def count_characters(text: str) -> Counter[str]:
    """Посчитать вхождения символов в строку."""
    raise NotImplementedError


def count_words(words: Iterable[str]) -> Counter[str]:
    """Посчитать вхождения слов в последовательность."""
    raise NotImplementedError


def most_common_items(counter: Counter[str], n: int) -> list[tuple[str, int]]:
    """Вернуть ``n`` самых частых элементов с их частотами.

    Если ``n`` больше числа уникальных элементов — вернуть все. Для ``n < 0`` —
    ``ValueError``.
    """
    raise NotImplementedError


def total_count(counter: Counter[str]) -> int:
    """Вернуть сумму всех счётчиков (общее число элементов)."""
    raise NotImplementedError


def unique_items(counter: Counter[str]) -> list[str]:
    """Все элементы, которые встречаются хотя бы один раз (без повторов)."""
    raise NotImplementedError


def expand(counter: Counter[str]) -> list[str]:
    """Развернуть счётчик в список с учётом кратности.

    Каждый элемент повторён столько раз, сколько раз он встретился:
    ``expand(Counter(a=2, b=1))`` -> ``["a", "a", "b"]`` (порядок — как в
    ``elements``).
    """
    raise NotImplementedError
