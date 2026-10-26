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

Термины, на которые ссылаются условия:

* **серия** — максимальный блок подряд идущих одинаковых значений;
* **порядок** — для отсортированных функций он диктуется сортировкой, для
  остальных — первым появлением.
"""

from __future__ import annotations

from itertools import groupby
from operator import itemgetter
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable


def runs(values: Iterable[str]) -> list[tuple[str, int]]:
    """Длины серий подряд идущих одинаковых значений.

    ``runs("AAABBC")`` -> ``[("A", 3), ("B", 2), ("C", 1)]``;
    ``runs("")`` -> ``[]``;
    ``runs("AB")`` -> ``[("A", 1), ("B", 1)]``;
    ``runs("ABA")`` -> ``[("A", 1), ("B", 1), ("A", 1)]`` — подряд идущих
    серий три, хотя значений всего два.

    Подсказка: ``[(key, sum(1 for _ in group)) for key, group in groupby(values)]``.
    """
    raise NotImplementedError


def groups_as_lists(
    values: Iterable[str], key: Callable[[str], object] | None = None
) -> list[tuple[object, list[str]]]:
    """Сгруппировать подряд идущие элементы, сразу материализуя группы.

    ``groups_as_lists("AAB")`` -> ``[("A", ["A", "A"]), ("B", ["B"])]``;
    ``groups_as_lists("aAbB", key=str.lower)`` -> ``[("a", ["a", "A"]),
    ("b", ["b", "B"])]`` — в группе исходные элементы, а не ключ;
    ``groups_as_lists("")`` -> ``[]``.

    ``key`` — функция или ``None`` (тогда ключ — сам элемент).

    Подсказка: список внутри обязателен. Если вернуть сами под-итераторы,
    после перехода к следующей группе они окажутся пустыми.
    """
    raise NotImplementedError


def unique_justseen(values: Iterable[str]) -> list[str]:
    """Убрать только соседние дубликаты, сохранив порядок.

    ``unique_justseen("AAABBCA")`` -> ``["A", "B", "C", "A"]`` — последняя
    ``"A"`` не соседняя с первой и остаётся;
    ``unique_justseen("")`` -> ``[]``;
    ``unique_justseen("ABA")`` -> ``["A", "B", "A"]``.

    Подсказка: ``map(itemgetter(0), groupby(values))`` — рецепт
    ``unique_justseen`` из документации.
    """
    raise NotImplementedError


def group_by_parity(values: Iterable[int]) -> dict[str, list[int]]:
    """Разложить числа по чётности, не полагаясь на порядок входа.

    Ключи результата — ровно две строки: ``"чётные"`` и ``"нечётные"``.
    ``group_by_parity([1, 2, 3, 4])`` -> ``{"нечётные": [1, 3], "чётные": [2, 4]}``;
    ``group_by_parity([4, 1, 3, 2])`` -> ``{"нечётные": [1, 3], "чётные": [4, 2]}``
    — группы идут по возрастанию остатка, внутри — исходный порядок;
    ``group_by_parity([])`` -> ``{}`` — пустой словарь, а не два пустых списка.

    Здесь ``groupby`` недостаточно: сначала отсортируйте по ключу
    (``key=lambda value: value % 2``), иначе группы разорвутся.

    Подсказка: ``0 % 2 == 0`` — это чётные, ``1`` — нечётные.
    """
    raise NotImplementedError


def longest_run(values: Iterable[str]) -> tuple[str, int] | None:
    """Самая длинная серия подряд идущих одинаковых значений.

    ``longest_run("AABBBCC")`` -> ``("B", 3)``;
    ``longest_run("")`` -> ``None``;
    ``longest_run("AABB")`` -> ``("A", 2)`` — при равной длине побеждает первая
    встреченная серия.

    Подсказка: обходите ``groupby`` и сравнивайте строго (``>``), а не ``>=`` —
    иначе при равенстве победит последняя.
    """
    raise NotImplementedError


def group_words_by_length(words: Iterable[str]) -> dict[int, list[str]]:
    """Сгруппировать слова по длине (порядок слов внутри группы сохранить).

    ``group_words_by_length(["ab", "c", "de", "f"])`` -> ``{1: ["c", "f"],
    2: ["ab", "de"]}``;
    ``group_words_by_length([])`` -> ``{}``;
    ``group_words_by_length(["a"])`` -> ``{1: ["a"]}``.

    Ключи идут по возрастанию длины. Внутри группы — исходный порядок слов,
    поэтому сортировка должна быть стабильной: ``sorted(words, key=len)``.

    Подсказка: отсортируйте по ``len``, затем ``groupby(..., key=len)`` и
    ``list(group)``.
    """
    raise NotImplementedError
