"""Упражнение 9. Группировка подряд идущих: ``groupby``. Уровень 5.

``groupby(iterable, key)`` отдаёт пары ``(ключ, под-итератор)``, но группирует
только **подряд идущие** элементы с одинаковым ключом. Это не SQL ``GROUP BY``:

* вход нужно предварительно отсортировать по тому же ключу, иначе одинаковые
  ключи окажутся в разных группах;
* под-итератор разделяет данные с ``groupby``: как только вы перешли к следующей
  группе, предыдущая становится пустой. Поэтому группу нужного размера сразу
  превращают в ``list``;
* пустой вход даёт пустой результат.

Здесь же пригодится рецепт ``unique_justseen``: ``map(itemgetter(0), groupby(...))``
убирает только соседние дубликаты.
"""

from __future__ import annotations

from itertools import groupby
from operator import itemgetter
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable


def runs(values: Iterable[str]) -> list[tuple[str, int]]:
    """Длины серий подряд идущих одинаковых значений.

    ``"AAABBC"`` даёт ``[("A", 3), ("B", 2), ("C", 1)]``.
    """
    raise NotImplementedError


def groups_as_lists(
    values: Iterable[str], key: Callable[[str], object] | None = None
) -> list[tuple[object, list[str]]]:
    """Сгруппировать подряд идущие элементы, сразу материализуя группы.

    ``key`` — функция или ``None`` (тогда ключ — сам элемент).
    """
    raise NotImplementedError


def unique_justseen(values: Iterable[str]) -> list[str]:
    """Убрать только соседние дубликаты, сохранив порядок.

    ``"AAABBCA"`` даёт ``["A", "B", "C", "A"]``.
    """
    raise NotImplementedError


def group_by_parity(values: Iterable[int]) -> dict[str, list[int]]:
    """Разложить числа по чётности, не полагаясь на порядок входа.

    Здесь ``groupby`` недостаточно: сначала отсортируйте по ключу.
    """
    raise NotImplementedError


def longest_run(values: Iterable[str]) -> tuple[str, int] | None:
    """Самая длинная серия подряд идущих одинаковых значений.

    При равной длине побеждает первая встреченная. Для пустого входа — ``None``.
    """
    raise NotImplementedError


def group_words_by_length(words: Iterable[str]) -> dict[int, list[str]]:
    """Сгруппировать слова по длине (порядок слов внутри группы сохранить)."""
    raise NotImplementedError
