"""Упражнение 3. Срезы итераторов: ``islice``. Уровень 2.

``islice(iterable, stop)`` и ``islice(iterable, start, stop, step)`` работают как
срезы, но **по итератору**, а не по последовательности:

* отрицательных индексов нет — ``islice(it, -1)`` бросает ``ValueError``;
* ``start`` и ``stop`` могут быть ``None`` (``None`` в ``stop`` — «до конца»);
* итератор потребляется: после ``islice`` он уже сдвинут вперёд;
* для последовательностей ``islice`` тоже работает, но выгода — именно в ленивости.

Реализуйте функции так, чтобы они не превращали вход в список.

Термины, на которые ссылаются условия:

* **поток** — любое итерируемое, в том числе бесконечное (``itertools.count()``);
* **потребление** — сколько элементов реально запрошено у источника; ``islice``
  не читает ничего сверх нужного.
"""

from __future__ import annotations

from itertools import islice
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator


def head(n: int, iterable: Iterable[int]) -> list[int]:
    """Вернуть первые ``n`` элементов потока.

    ``head(3, count(10))`` -> ``[10, 11, 12]``;
    ``head(0, count())`` -> ``[]``;
    ``head(5, [1, 2])`` -> ``[1, 2]`` — вход короче ``n``, ошибки нет.

    ``head(-1, [1, 2])`` -> ``ValueError`` с stdlib-текстом ``0 <= x``:
    отрицательного ``stop`` у ``islice`` нет, и перехватывать эту ошибку не надо.
    """
    raise NotImplementedError


def drop_first(n: int, iterable: Iterable[int]) -> list[int]:
    """Всё, кроме первых ``n`` элементов.

    ``drop_first(2, [0, 1, 2, 3])`` -> ``[2, 3]``;
    ``drop_first(0, [1, 2])`` -> ``[1, 2]`` — ничего не отбрасываем;
    ``drop_first(5, [1, 2])`` -> ``[]`` — вход короче ``n``.

    Итератор после вызова исчерпан: ``drop_first(2, iter(range(5)))`` вернёт
    ``[2, 3, 4]``, а сам итератор больше ничего не отдаст.

    Подсказка: ``islice(iterable, n, None)``.
    """
    raise NotImplementedError


def every_nth(n: int, iterable: Iterable[int]) -> list[int]:
    """Каждый ``n``-й элемент, начиная с нулевого.

    ``every_nth(3, range(7))`` -> ``[0, 3, 6]``;
    ``every_nth(1, [1, 2, 3])`` -> ``[1, 2, 3]`` — шаг 1 берёт всё;
    ``every_nth(10, range(3))`` -> ``[0]`` — попадает только нулевой;
    ``every_nth(0, range(3))`` -> ``ValueError`` (в сообщении есть ``n``).

    Подсказка: ``islice(iterable, 0, None, n)``; для ``n <= 0`` бросьте
    ``ValueError`` сами — шаг ``0`` у ``islice`` тоже даёт ``ValueError``, но
    с stdlib-текстом без буквы ``n``, а тест ищет именно её.
    """
    raise NotImplementedError


def nth(iterable: Iterable[int], index: int, default: int | None = None) -> int | None:
    """Вернуть элемент с номером ``index``, не читая весь поток.

    ``nth(count(), 0)`` -> ``0``;
    ``nth(count(100), 4)`` -> ``104``;
    ``nth([1, 2], 5)`` -> ``None`` — элемента нет, вернулся ``default``;
    ``nth([1, 2], 5, default=-1)`` -> ``-1``;
    ``nth([1, 2, 3], -1)`` -> ``ValueError`` (в сообщении есть ``index``).

    Поток потребляется ровно до нужного элемента: ``nth(count(), 10_000)``
    не должен зависнуть.

    Подсказка: ``next(islice(iterable, index, None), default)``.
    """
    raise NotImplementedError


def first_three(iterable: Iterable[int]) -> Iterator[int]:
    """Вернуть именно итератор первых трёх элементов (не список).

    ``list(first_three(count()))`` -> ``[0, 1, 2]``;
    повторный проход по результату даёт ``[]`` — это обычный одноразовый
    итератор, а не список;
    ``list(first_three([1]))`` -> ``[1]``.

    Тип результата проверяется в тесте через ``isinstance(result, Iterator)``,
    поэтому ``list(...)`` здесь не годится.

    Подсказка: верните сам объект ``islice(iterable, 3)``, не оборачивая его.
    """
    raise NotImplementedError
