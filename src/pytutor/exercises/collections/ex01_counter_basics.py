"""Упражнение 1. ``collections.Counter`` — простой счёт частот. Уровень 1.

``Counter`` — это ``dict``, где ключ — элемент, а значение — сколько раз он
встретился. В отличие от обычного словаря, ``Counter`` умеет считать сам:

* ``Counter(iterable)`` / ``Counter(mapping)`` — построить счётчик;
* ``most_common(n)`` — ``n`` самых частых пар ``(ключ, частота)``;
* ``total()`` — сумма всех счётчиков (общее число элементов);
* ``elements()`` — развёрнутый итератор элементов с учётом кратности.

Ключевая деталь: ``Counter`` **не удаляет** ключи с нулевым или отрицательным
счётчиком. Такой ключ остаётся в словаре, но ``elements()`` его пропустит,
а ``len(counter)`` его посчитает. Поэтому «уникальные элементы» — это не
``list(counter)``, а ключи с положительным счётчиком.

``Counter`` — подкласс ``dict``, поэтому сравнение ``==`` учитывает все ключи
вместе со значениями, включая нулевые.

Реализуйте функции ниже. Это разминка: почти везде достаточно одного вызова
метода ``Counter``.

Термины, на которые ссылаются условия:

* **частота** — значение счётчика для ключа;
* **пустой счётчик** — ``Counter()``, а не ``{}`` и не ``None``.
"""

from __future__ import annotations

from collections import Counter
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def count_characters(text: str) -> Counter[str]:
    """Посчитать вхождения символов в строку.

    ``count_characters("aab")`` -> ``Counter({"a": 2, "b": 1})``;
    ``count_characters("")`` -> ``Counter()`` — пустой вход даёт пустой счётчик;
    ``count_characters("ab")`` -> ``Counter({"a": 1, "b": 1})``.

    Регистр **не** нормализуется: ``"A"`` и ``"a"`` — разные ключи.

    Подсказка: ``Counter`` сам разбирает строку на символы, отдельный цикл не
    нужен.
    """
    raise NotImplementedError


def count_words(words: Iterable[str]) -> Counter[str]:
    """Посчитать вхождения слов в последовательность.

    ``count_words(["a", "b", "a"])`` -> ``Counter({"a": 2, "b": 1})``;
    ``count_words([])`` -> ``Counter()``;
    ``count_words(iter(["x"]))`` -> ``Counter({"x": 1})`` — вход может быть
    одноразовым итератором.

    Подсказка: ``Counter`` принимает любое итерируемое, включая генератор.
    """
    raise NotImplementedError


def most_common_items(counter: Counter[str], n: int) -> list[tuple[str, int]]:
    """Вернуть ``n`` самых частых элементов с их частотами.

    ``most_common_items(Counter(a=3, b=1, c=2), 2)`` -> ``[("a", 3), ("c", 2)]``;
    ``most_common_items(Counter(a=3, b=1, c=2), 10)`` -> ``[("a", 3), ("c", 2),
    ("b", 1)]`` — если ``n`` больше числа уникальных элементов, вернуть все;
    ``most_common_items(Counter(), 1)`` -> ``[]``;
    ``most_common_items(counter, -1)`` -> ``ValueError`` (в сообщении есть ``n``).

    Обратите внимание: сам ``Counter.most_common(-1)`` вернул бы пустой список
    молча, поэтому отрицательный ``n`` нужно проверять явно.

    Подсказка: проверка ``n < 0`` + один вызов ``counter.most_common(n)``.
    Порядок при равных частотах здесь не задан — это тема упражнения 10.
    """
    raise NotImplementedError


def total_count(counter: Counter[str]) -> int:
    """Вернуть сумму всех счётчиков (общее число элементов).

    ``total_count(Counter(a=2, b=3))`` -> ``5``;
    ``total_count(Counter())`` -> ``0``.

    Суммируются **все** значения, включая отрицательные, поэтому результат
    может быть отрицательным. Отдельная проверка не нужна.

    Подсказка: ``counter.total()`` — метод, появившийся в Python 3.10; ручной
    ``sum`` не требуется.
    """
    raise NotImplementedError


def unique_items(counter: Counter[str]) -> list[str]:
    """Все элементы, которые встречаются хотя бы один раз (без повторов).

    ``unique_items(Counter(a=2, b=0, c=1))`` -> ``["a", "c"]`` — ключ ``b`` с
    нулевым счётчиком отброшен;
    ``unique_items(Counter())`` -> ``[]``;
    ``unique_items(Counter(x=-1, y=1))`` -> ``["y"]`` — отрицательные тоже не
    считаются «встреченными».

    Порядок — как в словаре, то есть по первому появлению ключа.

    Подсказка: ``[key for key, count in counter.items() if count > 0]``.
    ``list(counter)`` не подойдёт: оно вернёт и нулевые ключи.
    """
    raise NotImplementedError


def expand(counter: Counter[str]) -> list[str]:
    """Развернуть счётчик в список с учётом кратности.

    ``expand(Counter(a=2, b=1))`` -> ``["a", "a", "b"]``;
    ``expand(Counter(a=0))`` -> ``[]`` — нулевые и отрицательные ключи
    пропускаются;
    ``expand(Counter())`` -> ``[]``.

    Порядок — как в ``elements()``: ключи обходятся в порядке словаря, каждый
    повторяется ``count`` раз.

    Подсказка: ``list(counter.elements())``. Ручной ``for`` с ``extend`` даст
    тот же результат, но метод короче.
    """
    raise NotImplementedError
