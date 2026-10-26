"""Упражнение 5. Арифметика ``Counter``. Уровень 3.

``Counter`` умеет вести себя как мультимножество. Операторные версии
**создают новый** счётчик, метод ``subtract`` меняет существующий:

* ``+`` — поэлементная сумма; ключи с итогом ``<= 0`` **отбрасываются**;
* ``-`` — разность; результат обрезается снизу нулём, пустые ключи уходят;
* ``&`` — пересечение: ``min`` по каждому ключу, но только для положительных
  значений;
* ``|`` — объединение: ``max`` по каждому ключу;
* ``subtract`` — вычитание на месте, допускающее отрицательные итоги.

Здесь важно понимать, что ``+`` и ``|`` дают разные результаты, когда счётчики
различаются: ``Counter(a=1) + Counter(a=2)`` -> ``a = 3``, а
``Counter(a=1) | Counter(a=2)`` -> ``a = 2``.

Ещё одно следствие: у ``+`` и ``-`` ключ со значением ``0`` исчезает, а у
``&`` и ``|`` — остаётся, если присутствует в обоих счётчиках.

Текст ошибки: для неизвестной стратегии нужно ``ValueError``, в сообщении
которого есть подстрока ``стратегия`` (например, ``"Неизвестная стратегия: x"``).
"""

from __future__ import annotations

from collections import Counter
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def combine(*counters: Counter[str]) -> Counter[str]:
    """Сложить несколько счётчиков в один.

    ``combine(Counter(a=1), Counter(a=2, b=1))`` -> ``Counter(a=3, b=1)``;
    ``combine()`` -> ``Counter()`` — без аргументов пустой счётчик;
    ``combine(Counter(a=1), Counter(a=-5))`` -> ``Counter()`` — отрицательный
    итог отброшен оператором ``+``.

    Подсказка: начните с пустого ``Counter()`` и в цикле делайте
    ``result += counter``. Не используйте ``sum(counters, Counter())`` — он
    тоже работает, но цикл понятнее.
    """
    raise NotImplementedError


def add_counts(left: Counter[str], right: Counter[str]) -> Counter[str]:
    """Сумма двух счётчиков (``+``).

    ``add_counts(Counter(a=1, b=2), Counter(b=1))`` -> ``Counter(a=1, b=3)``;
    ``add_counts(Counter(a=1), Counter(a=-1))`` -> ``Counter()`` — нулевой итог
    не сохраняется;
    ``add_counts(Counter(), Counter())`` -> ``Counter()``.

    Подсказка: ``left + right``. Исходные счётчики не меняются.
    """
    raise NotImplementedError


def difference_counts(left: Counter[str], right: Counter[str]) -> Counter[str]:
    """Разность двух счётчиков (``-``), с обрезкой снизу нулём.

    ``difference_counts(Counter(a=3, b=1), Counter(a=5))`` -> ``Counter(b=1)`` —
    ``a`` ушёл, потому что отрицательные результаты отбрасываются;
    ``difference_counts(Counter(a=1), Counter())`` -> ``Counter(a=1)``;
    ``difference_counts(Counter(), Counter(a=1))`` -> ``Counter()``.

    Подсказка: ``left - right``. Это именно оператор, а не ``subtract``: тот
    оставил бы ``a = -2``.
    """
    raise NotImplementedError


def overlap_counts(left: Counter[str], right: Counter[str]) -> Counter[str]:
    """Пересечение: для каждого ключа — минимум из двух значений (``&``).

    ``overlap_counts(Counter(a=3, b=2), Counter(a=1, c=5))`` ->
    ``Counter(a=1)`` — только общий ключ, взято меньшее значение;
    ``overlap_counts(Counter(a=1), Counter(b=2))`` -> ``Counter()``;
    ``overlap_counts(Counter(), Counter(a=1))`` -> ``Counter()``.

    Подсказка: ``left & right``. Ключи, которых нет в одном из счётчиков,
    не попадают в результат.
    """
    raise NotImplementedError


def union_counts(left: Counter[str], right: Counter[str]) -> Counter[str]:
    """Объединение: для каждого ключа — максимум из двух значений (``|``).

    ``union_counts(Counter(a=3, b=2), Counter(a=1, c=5))`` ->
    ``Counter(a=3, b=2, c=5)``;
    ``union_counts(Counter(a=1), Counter())`` -> ``Counter(a=1)``;
    ``union_counts(Counter(), Counter())`` -> ``Counter()``.

    Подсказка: ``left | right``. Для ``Counter`` это не «объединение
    множеств»: берётся максимум, а не сумма.
    """
    raise NotImplementedError


def subtract_inplace(left: Counter[str], right: Counter[str]) -> Counter[str]:
    """Вычесть ``right`` из ``left`` на месте (``subtract``).

    В отличие от ``-``, итоги могут стать отрицательными. Вернуть ``left``.

    ``left = Counter(a=3, b=1)``: после ``subtract_inplace(left, Counter(a=5))``
    результат ``is left`` и ``left == Counter(a=-2, b=1)``;
    ``subtract_inplace(Counter(), Counter(x=1))`` -> ``Counter(x=-1)`` —
    недостающий ключ создаётся с отрицательным значением;
    нулевые ключи **не** удаляются: ``Counter(a=1)`` минус ``Counter(a=1)``
    даёт ``Counter(a=0)``.

    Подсказка: ``left.subtract(right)`` возвращает ``None``, поэтому после него
    нужен ``return left``.
    """
    raise NotImplementedError


def merge_strategies(left: Counter[str], right: Counter[str], strategy: str) -> Counter[str]:
    """Объединить два счётчика по стратегии ``strategy``.

    ``strategy`` может быть ``"add"``, ``"max"``, ``"min"`` или ``"sub"``
    (соответствует ``+``, ``|``, ``&``, ``-``).

    ``merge_strategies(Counter(a=3, b=1), Counter(a=1, b=2, c=1), "add")`` ->
    ``Counter(a=4, b=3, c=1)``;
    та же пара со ``"max"`` -> ``Counter(a=3, b=2, c=1)``;
    со ``"min"`` -> ``Counter(a=1, b=1)``;
    со ``"sub"`` -> ``Counter(a=2)``;
    ``merge_strategies(Counter(), Counter(), "unknown")`` -> ``ValueError``
    (в сообщении есть ``стратегия``).

    Исходные счётчики не меняются ни в одной стратегии.

    Подсказка: цепочка ``if``/``elif`` с ранними ``return``, а в конце —
    ``raise ValueError(f"Неизвестная стратегия: {strategy}")``. Не используйте
    ``getattr`` по имени оператора: ошибка будет невнятной.
    """
    raise NotImplementedError
