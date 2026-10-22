"""Упражнение 8. Вложенные ``defaultdict`` — автосоздание уровней. Уровень 4.

``defaultdict`` можно вкладывать друг в друга: ``defaultdict(lambda: defaultdict(list))``
создаёт двухуровневую структуру, где каждый отсутствующий ключ первого уровня
автоматически порождает ``defaultdict(list)`` второго.

Это удобно для деревьев каталогов, «толстых» таблиц и любых структур, где
пути/ключи заранее неизвестны.
"""

from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def nested_defaultdict() -> defaultdict:
    """Создать двухуровневый ``defaultdict``.

    ``defaultdict(list)`` — на втором уровне, так что ``d["a"]["x"].append(1)``
    не должно бросать ``KeyError``.
    """
    raise NotImplementedError


def add_path(tree: defaultdict, path: list[str], value: int) -> defaultdict:
    """Добавить ``value`` в дерево по пути ``path``.

    ``path`` — список ключей; по каждому ключу (кроме последнего) создаётся
    вложенный узел. Последний ключ получает ``value`` в свой список.

    ``add_path(nested_defaultdict(), ["a", "x"], 1)`` -> ``{"a": {"x": [1]}}``.
    """
    raise NotImplementedError


def get_path(tree: defaultdict, path: list[str], default: int | None = None) -> list[int] | None:
    """Вернуть список значений по пути ``path``.

    Если какого-то ключа в пути нет — вернуть ``default``. Не создавать
    отсутствующие узлы.
    """
    raise NotImplementedError


def build_counts(words: Iterable[str]) -> defaultdict:
    """Построить ``defaultdict``: длина слова -> ``Counter`` букв слова.

    ``build_counts(["ab", "abc"])`` -> ``{2: Counter(a=1, b=1), 3: Counter(a=1,
    b=1, c=1)}``. Второй уровень — ``Counter``.
    """
    raise NotImplementedError


def merge_trees(left: defaultdict, right: defaultdict) -> defaultdict:
    """Слить два вложенных ``defaultdict``.

    Для каждой длины слова списки значений объединяются (порядок: сначала все из
    ``left``, потом все из ``right``). Вернуть новое дерево.
    """
    raise NotImplementedError
