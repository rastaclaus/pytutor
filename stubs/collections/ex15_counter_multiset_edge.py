"""Упражнение 15. Крайние случаи ``Counter``: мультимножество. Уровень 6.

``Counter`` — это мультимножество, и его крайние случаи часто ловят в реальном
коде:

* счётчики могут стать **отрицательными** после ``subtract``;
* ``elements()`` игнорирует ключи со счётчиком <= 0;
* ``+`` отбрасывает неположительные итоги, а ``|`` — нет;
* после ``&``/``|`` нулевые ключи могут остаться.

Нужно уметь фильтровать и сравнивать мультимножества.
"""

from __future__ import annotations

from collections import Counter


def nonzero_items(counter: Counter[str]) -> Counter[str]:
    """Оставить только ключи с положительным счётчиком."""
    raise NotImplementedError


def keys_with_positive_count(counter: Counter[str]) -> list[str]:
    """Список ключей со счётчиком больше нуля (порядок — как в ``counter``)."""
    raise NotImplementedError


def is_submultiset(left: Counter[str], right: Counter[str]) -> bool:
    """Проверить, что ``left`` — под-мультимножество ``right``.

    Каждый ключ из ``left`` должен иметь счётчик не больше, чем в ``right``
    (отрицательные счётчики в ``left`` игнорируются).
    """
    raise NotImplementedError


def symmetric_difference(left: Counter[str], right: Counter[str]) -> Counter[str]:
    """Симметрическая разность: ключи, где счётчики различаются.

    Для каждого ключа — модуль разности счётчиков, отбрасывая нули.
    """
    raise NotImplementedError


def normalize(counter: Counter[str]) -> Counter[str]:
    """Вернуть счётчик без отрицательных и нулевых значений.

    Оставшиеся элементы отсортированы по ключу.
    """
    raise NotImplementedError
