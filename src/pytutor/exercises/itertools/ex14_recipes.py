"""Упражнение 14. Рецепты из документации. Уровень 7.

В документации ``itertools`` есть раздел «Itertools Recipes» — готовые комбинации
инструментов для типовых задач. Здесь четыре из них:

* ``sliding_window`` — окно на ``deque(maxlen=n)``;
* ``running_mean`` — ``map(truediv, accumulate(values), count(1))``: бегущая
  сумма делится на бегущий счётчик;
* ``sum_of_squares`` — ``sumprod(*tee(values))``: две копии одного потока,
  скалярное произведение вектора с самим собой;
* ``tail`` — последние ``n`` элементов через ``deque(maxlen=n)``.

Ещё три функции (``running_extremes``, ``average_of_top``, ``moving_average``) —
комбинации этих рецептов: сначала соберите примитивы, затем переиспользуйте их.

Общая идея рецептов: не материализовать вход и переиспользовать уже изученные
примитивы вместо ручных циклов.

Термины, на которые ссылаются условия:

* **префикс длины k** — первые ``k`` элементов входа (``values[:k]``);
* **окно длины n** — ``n`` подряд идущих элементов (``values[i:i + n]``).

Если функция возвращает список, его длина равна числу полных префиксов или окон,
которые удалось собрать; конкретика — в примерах у каждой функции.
"""

from __future__ import annotations

from collections import deque
from itertools import accumulate, count, islice, tee
from math import sumprod
from operator import truediv
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def sliding_window(values: Iterable[int], size: int) -> list[tuple[int, ...]]:
    """Все перекрывающиеся окна длины ``size``, слева направо.

    ``sliding_window("ABCDEFG", 3)`` -> ``ABC BCD CDE DEF EFG`` (5 окон);
    ``sliding_window([1, 2, 3], 1)`` -> ``[(1,), (2,), (3,)]``;
    ``sliding_window([1, 2], 3)`` -> ``[]`` — элементов меньше окна;
    ``sliding_window([1], 0)`` -> ``ValueError`` (в сообщении есть ``size``).

    Подсказка: рецепт на ``deque(maxlen=size)``; первые ``size - 1`` элементов
    надо забрать заранее через ``islice``, иначе первое окно окажется неполным.
    """
    if size <= 0:
        msg = "size must be > 0"
        raise ValueError(msg)
    res: list[tuple[int, ...]] = []
    if size < 0:
        msg = "size must be >= 0"
        raise ValueError(msg)

    iterator = iter(values)
    window = deque(islice(iterator, size - 1), maxlen=size)
    for value in iterator:
        window.append(value)
        res.append(tuple(window))
    return res


def running_mean(values: Iterable[int]) -> list[float]:
    """Бегущее среднее: i-й элемент — среднее ``values[:i + 1]``.

    ``running_mean([2, 4, 6])`` -> ``[2.0, 3.0, 4.0]`` (2/1, 6/2, 12/3);
    ``running_mean([])`` -> ``[]``. Длина результата равна длине входа.

    Подсказка: ``accumulate`` — бегущая сумма, ``count(1)`` — бегущий
    знаменатель, ``map(truediv, ...)`` делит одно на другое лениво.
    """
    return list(map(truediv, accumulate(values), count(1)))


def sum_of_squares(values: Iterable[int]) -> float:
    """Сумма квадратов всех элементов, без промежуточного списка.

    ``sum_of_squares([1, 2, 3])`` -> ``14`` (1 + 4 + 9);
    ``sum_of_squares([])`` -> ``0`` — сумма пустого набора.

    Подсказка: ``sumprod(a, b)`` — скалярное произведение; две копии одного
    потока (``tee``) дают вектор, умноженный сам на себя.
    """
    return sumprod(*tee(values, 2))


def tail(values: Iterable[int], size: int) -> list[int]:
    """Последние ``size`` элементов в исходном порядке, за один проход.

    ``tail([1, 2, 3, 4], 2)`` -> ``[3, 4]``;
    ``tail([1, 2], 5)`` -> ``[1, 2]`` — элементов меньше, вернуть все;
    ``tail([1], 0)`` -> ``[]``.

    Вход целиком материализовать нельзя: решение должно работать и на
    бесконечном потоке. Подсказка: ``deque(values, maxlen=size)``.
    """
    if size < 0:
        msg = "size must be > 0"
        raise ValueError(msg)
    if size == 0:
        return []
    return list(deque(values, maxlen=size))


def running_extremes(values: Iterable[int]) -> list[tuple[int, int]]:
    """Для каждого префикса — пара ``(минимум, максимум)`` этого префикса.

    i-й элемент результата — ``(min(values[:i + 1]), max(values[:i + 1]))``,
    то есть минимум и максимум среди первых ``i + 1`` элементов, включая
    текущий. Длина результата равна длине входа.

    ``running_extremes([3, 1, 4])`` -> ``[(3, 3), (1, 3), (1, 4)]``
        префикс ``[3]``       -> ``(3, 3)``
        префикс ``[3, 1]``    -> ``(1, 3)``
        префикс ``[3, 1, 4]`` -> ``(1, 4)``
    ``running_extremes([])`` -> ``[]``

    Оба значения накопительные: минимум может только уменьшаться, максимум —
    только расти, пересчитывать их «с нуля» на каждом шаге не нужно.
    Подсказка: ``accumulate(values, min)`` и ``accumulate(values, max)`` дают
    два бегущих ряда, ``zip(..., strict=True)`` склеивает их в пары.
    """
    raise NotImplementedError


def average_of_top(values: Iterable[int], size: int) -> float:
    """Среднее последних ``size`` элементов — тех же, что вернул бы ``tail``.

    ``average_of_top([1, 2, 3, 4], 2)`` -> ``3.5`` ((3 + 4) / 2);
    ``average_of_top([5], 3)`` -> ``5.0`` — элементов меньше, берём все;
    ``average_of_top([], 2)`` -> ``ValueError`` (в сообщении есть «пустой»).

    Подсказка: переиспользуйте ``tail``.
    """
    raise NotImplementedError


def moving_average(values: Iterable[float], size: int) -> list[float]:
    """Скользящее среднее: среднее каждого окна длины ``size``.

    ``moving_average([1.0, 2.0, 3.0], 2)`` -> ``[1.5, 2.5]``;
    ``moving_average([1.0], 2)`` -> ``[]`` — окно не набралось.

    Длина результата — ``len(values) - size + 1`` при ``len(values) >= size``.
    Подсказка: переиспользуйте ``sliding_window`` и делите сумму окна на
    ``size``; ``size <= 0`` отсекается внутри ``sliding_window``.
    """
    raise NotImplementedError
