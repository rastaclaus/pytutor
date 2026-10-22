"""Упражнение 3. ``collections.defaultdict`` — группировка. Уровень 2.

``defaultdict`` — словарь, который для отсутствующего ключа сам вызывает фабрику
и создаёт значение по умолчанию. Это убирает типичный шаблон
``if key not in d: d[key] = []``.

Самый частый сценарий — группировка: ``defaultdict(list)`` собирает элементы по
ключам, ``defaultdict(set)`` — уникальные значения.
"""

from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def group_by_key(pairs: Iterable[tuple[str, int]]) -> dict[str, list[int]]:
    """Сгруппировать пары ``(ключ, значение)`` по ключу.

    ``group_by_key([("a", 1), ("b", 2), ("a", 3)])`` ->
    ``{"a": [1, 3], "b": [2]}``.
    """
    raise NotImplementedError


def group_unique(pairs: Iterable[tuple[str, int]]) -> dict[str, set[int]]:
    """Сгруппировать пары по ключу, сохраняя уникальные значения.

    ``group_unique([("a", 1), ("a", 1), ("a", 2)])`` ->
    ``{"a": {1, 2}}``.
    """
    raise NotImplementedError


def index_by_field(records: Iterable[tuple[str, str]], field: int) -> dict[str, list[tuple[str, str]]]:
    """Сгруппировать записи по значению поля с индексом ``field``.

    ``index_by_field([("a", "x"), ("b", "y"), ("c", "x")], 1)`` ->
    ``{"x": [("a", "x"), ("c", "x")], "y": [("b", "y")]}``.
    """
    raise NotImplementedError


def invert_mapping(mapping: dict[str, int]) -> dict[int, list[str]]:
    """Инвертировать словарь: значения -> список ключей.

    ``invert_mapping({"a": 1, "b": 2, "c": 1})`` ->
    ``{1: ["a", "c"], 2: ["b"]}``. Порядок ключей в списках — как в исходном
    словаре.
    """
    raise NotImplementedError


def group_by_first_letter(words: Iterable[str]) -> dict[str, list[str]]:
    """Сгруппировать слова по первой букве, отсортировав группы.

    ``group_by_first_letter(["apple", "avocado", "banana"])`` ->
    ``{"a": ["apple", "avocado"], "b": ["banana"]}``. Для пустого слова
    пропустить его. Группы и элементы внутри — в порядке появления.
    """
    raise NotImplementedError
