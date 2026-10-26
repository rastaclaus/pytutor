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

Важная граница: ``r`` больше длины входа — это не ошибка, а пустой результат.
Исключение — ``r=0``: он всегда даёт ровно одну пустую выборку ``()``.
"""

from __future__ import annotations

from itertools import combinations, combinations_with_replacement, permutations, product
from math import comb, perm
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def all_pairs(values: Iterable[str]) -> list[tuple[str, str]]:
    """Все упорядоченные пары, включая повторы: ``AA AB BA BB``.

    ``all_pairs("AB")`` -> ``[("A","A"), ("A","B"), ("B","A"), ("B","B")]``;
    ``all_pairs("A")`` -> ``[("A", "A")]``;
    ``all_pairs("")`` -> ``[]``.

    Подсказка: ``product(values, repeat=2)``. Вход потребляется целиком, так
    что генератор тоже подойдёт.
    """
    raise NotImplementedError


def permutations_of(values: Iterable[str], r: int) -> list[tuple[str, ...]]:
    """Все размещения длины ``r``.

    ``permutations_of("ABC", 2)`` -> ``[("A","B"), ("A","C"), ("B","A"),
    ("B","C"), ("C","A"), ("C","B")]``;
    ``permutations_of("AB", 3)`` -> ``[]`` — ``r`` больше входа, пусто, а не
    ошибка;
    ``permutations_of("ABC", 0)`` -> ``[()]``.

    Подсказка: ``permutations(values, r)``.
    """
    raise NotImplementedError


def combinations_of(values: Iterable[str], r: int) -> list[tuple[str, ...]]:
    """Все сочетания длины ``r``.

    ``combinations_of("ABC", 2)`` -> ``[("A","B"), ("A","C"), ("B","C")]``;
    ``combinations_of("ABC", 0)`` -> ``[()]``;
    ``combinations_of("AB", 3)`` -> ``[]``.

    Подсказка: ``combinations(values, r)``.
    """
    raise NotImplementedError


def combinations_with_repeats(values: Iterable[str], r: int) -> list[tuple[str, ...]]:
    """Все сочетания длины ``r`` с повторами.

    ``combinations_with_repeats("AB", 2)`` -> ``[("A","A"), ("A","B"),
    ("B","B")]`` — порядок не важен, ``("B", "A")`` не появится;
    ``combinations_with_repeats("A", 3)`` -> ``[("A", "A", "A")]``;
    ``combinations_with_repeats("AB", 0)`` -> ``[()]``.

    Подсказка: ``combinations_with_replacement(values, r)``.
    """
    raise NotImplementedError


def powerset(values: Iterable[str]) -> list[tuple[str, ...]]:
    """Все подмножества, от пустого до полного, по возрастанию длины.

    ``powerset([1, 2])`` -> ``[(), (1,), (2,), (1, 2)]``;
    ``powerset([])`` -> ``[()]`` — пустое множество имеет одно подмножество,
    само себя;
    ``len(powerset([1, 2, 3]))`` -> ``8`` (``2 ** 3``).

    Подсказка: материализуйте вход в список один раз, затем для
    ``size in range(len(pool) + 1)`` соберите ``combinations(pool, size)``.
    """
    raise NotImplementedError


def count_permutations(n: int, r: int) -> int:
    """Сколько элементов вернёт ``permutations(range(n), r)``.

    ``count_permutations(4, 2)`` -> ``12``;
    ``count_permutations(3, 0)`` -> ``1``;
    ``count_permutations(0, 0)`` -> ``1``;
    ``count_permutations(2, 5)`` -> ``0`` — ``r > n``, выборок нет.

    Подсказка: ``math.perm(n, r)`` возвращает ровно это число.
    """
    raise NotImplementedError


def count_combinations(n: int, r: int) -> int:
    """Сколько элементов вернёт ``combinations(range(n), r)``.

    ``count_combinations(4, 2)`` -> ``6``;
    ``count_combinations(4, 0)`` -> ``1``;
    ``count_combinations(2, 5)`` -> ``0``.

    Подсказка: ``math.comb(n, r)``.
    """
    raise NotImplementedError


def dice_sums(sides: int = 6, dice: int = 2) -> dict[int, int]:
    """Распределение сумм при броске ``dice`` кубиков с ``sides`` гранями.

    Вернуть словарь ``сумма -> количество комбинаций``, отсортированный по сумме.
    ``dice_sums()[7]`` -> ``6`` и ``sum(dice_sums().values())`` -> ``36``;
    ``list(dice_sums())`` -> ``sorted(dice_sums())`` — ключи по возрастанию;
    ``dice_sums(1, 2)`` -> ``{2: 1, 3: 1, 4: 1, ...}`` — с одной гранью все
    суммы встречаются по разу.

    Подсказка: ``product(range(1, sides + 1), repeat=dice)``; словарь в конце
    упорядочьте через ``dict(sorted(totals.items()))``.
    """
    raise NotImplementedError
