"""Упражнение 12. Комбинаторика. Уровень 6.

Три генератора подмножеств, которые различаются двумя вопросами: важен ли
порядок и разрешены ли повторы.

* ``product(a, b, ..., repeat=k)`` — декартово произведение, как вложенные циклы;
* ``permutations(p, r)`` — упорядоченные выборки длины ``r``, без повторов;
* ``combinations(p, r)`` — неупорядоченные выборки без повторов, в лексикографи-
  ческом порядке;
* ``combinations_with_replacement(p, r)`` — как ``combinations``, но элементы
  могут повторяться.

Количества считают ``math.perm`` и ``math.comb``. Все генераторы потребляют вход
целиком (кроме ``product`` с бесконечными аргументами — так нельзя), поэтому для
больших входов результат нужно обрезать.
"""

from __future__ import annotations

from itertools import combinations, combinations_with_replacement, permutations, product
from math import comb, perm
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def all_pairs(values: Iterable[str]) -> list[tuple[str, str]]:
    """Все упорядоченные пары, включая повторы: ``AA AB BA BB``."""
    raise NotImplementedError


def permutations_of(values: Iterable[str], r: int) -> list[tuple[str, ...]]:
    """Все размещения длины ``r``."""
    raise NotImplementedError


def combinations_of(values: Iterable[str], r: int) -> list[tuple[str, ...]]:
    """Все сочетания длины ``r``."""
    raise NotImplementedError


def combinations_with_repeats(values: Iterable[str], r: int) -> list[tuple[str, ...]]:
    """Все сочетания длины ``r`` с повторами."""
    raise NotImplementedError


def powerset(values: Iterable[str]) -> list[tuple[str, ...]]:
    """Все подмножества, от пустого до полного, по возрастанию длины."""
    raise NotImplementedError


def count_permutations(n: int, r: int) -> int:
    """Сколько элементов вернёт ``permutations(range(n), r)``."""
    raise NotImplementedError


def count_combinations(n: int, r: int) -> int:
    """Сколько элементов вернёт ``combinations(range(n), r)``."""
    raise NotImplementedError


def dice_sums(sides: int = 6, dice: int = 2) -> dict[int, int]:
    """Распределение сумм при броске ``dice`` кубиков с ``sides`` гранями.

    Вернуть словарь ``сумма -> количество комбинаций``, отсортированный по сумме.
    Подсказка: ``product(range(1, sides + 1), repeat=dice)``.
    """
    raise NotImplementedError
