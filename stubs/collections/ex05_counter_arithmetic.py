"""Упражнение 5. Арифметика ``Counter``. Уровень 3.

``Counter`` умеет вести себя как мультимножество. Операции:

* ``+`` — сумма счётчиков (складываются только положительные итоги);
* ``-`` — разность (результат обрезается снизу нулём);
* ``&`` — пересечение: min по каждому ключу;
* ``|`` — объединение: max по каждому ключу;
* ``subtract`` — вычитание «на месте», допускающее отрицательные итоги.

Здесь важно понимать, что ``+`` и ``|`` дают разные результаты, когда счётчики
различаются.
"""

from __future__ import annotations

from collections import Counter
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def combine(*counters: Counter[str]) -> Counter[str]:
    """Сложить несколько счётчиков в один.

    ``combine(Counter(a=1), Counter(a=2, b=1))`` -> ``Counter(a=3, b=1)``.
    """
    raise NotImplementedError


def add_counts(left: Counter[str], right: Counter[str]) -> Counter[str]:
    """Сумма двух счётчиков (``+``)."""
    raise NotImplementedError


def difference_counts(left: Counter[str], right: Counter[str]) -> Counter[str]:
    """Разность двух счётчиков (``-``), с обрезкой снизу нулём.

    ``difference_counts(Counter(a=3, b=1), Counter(a=5))`` -> ``Counter(b=1)``.
    """
    raise NotImplementedError


def overlap_counts(left: Counter[str], right: Counter[str]) -> Counter[str]:
    """Пересечение: для каждого ключа — минимум из двух значений (``&``)."""
    raise NotImplementedError


def union_counts(left: Counter[str], right: Counter[str]) -> Counter[str]:
    """Объединение: для каждого ключа — максимум из двух значений (``|``)."""
    raise NotImplementedError


def subtract_inplace(left: Counter[str], right: Counter[str]) -> Counter[str]:
    """Вычесть ``right`` из ``left`` на месте (``subtract``).

    В отличие от ``-``, итоги могут стать отрицательными. Вернуть ``left``.
    """
    raise NotImplementedError


def merge_strategies(left: Counter[str], right: Counter[str], strategy: str) -> Counter[str]:
    """Объединить два счётчика по стратегии ``strategy``.

    ``strategy`` может быть ``"add"``, ``"max"``, ``"min"`` или ``"sub"``
    (соответствует ``+``, ``|``, ``&``, ``-``). Неизвестная стратегия — ``ValueError``.
    """
    raise NotImplementedError
