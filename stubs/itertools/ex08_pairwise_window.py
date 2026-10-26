"""Упражнение 8. Соседние пары и скользящее окно. Уровень 4.

``pairwise(iterable)`` отдаёт перекрывающиеся пары ``(p0, p1), (p1, p2), ...``.
На входе короче двух элементов результат пуст. Это самый частый способ считать
разности, скорости и «соседние» переходы без индексов.

Скользящего окна в ``itertools`` нет — его собирают из ``deque(maxlen=N)``:
очередь автоматически вытесняет старый элемент при переполнении. Тот же приём
даёт «хвост» из последних ``N`` элементов.

Обратите внимание: ``pairwise`` возвращает генератор, поэтому результат нужно
материализовать самим.

Термины, на которые ссылаются условия:

* **окно длины n** — ``n`` подряд идущих элементов;
* **длина результата** — для окна ``len(values) - n + 1`` при
  ``len(values) >= n`` и ``0`` иначе; для пар — ``len(values) - 1``.
"""

from __future__ import annotations

from collections import deque
from itertools import islice, pairwise
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator


def adjacent_pairs(values: Iterable[str]) -> list[tuple[str, str]]:
    """Все соседние пары подряд.

    ``adjacent_pairs("ABC")`` -> ``[("A", "B"), ("B", "C")]``;
    ``adjacent_pairs("A")`` -> ``[]``;
    ``adjacent_pairs("")`` -> ``[]``.

    Подсказка: ``list(pairwise(values))``.
    """
    raise NotImplementedError


def differences(values: Iterable[int]) -> list[int]:
    """Разности соседних элементов: ``[1, 4, 9] -> [3, 5]``.

    ``differences([1, 4, 9])`` -> ``[3, 5]`` — считается «правый минус левый»;
    ``differences([5])`` -> ``[]`` — одной пары нет;
    ``differences([3, 2])`` -> ``[-1]`` — разности бывают отрицательными.

    Подсказка: ``[right - left for left, right in pairwise(values)]``.
    """
    raise NotImplementedError


def all_increasing(values: Iterable[int]) -> bool:
    """Проверить, что последовательность строго возрастает.

    ``all_increasing([1, 2, 3])`` -> ``True``;
    ``all_increasing([1, 1, 2])`` -> ``False`` — равенство уже нарушает
    строгость;
    ``all_increasing([3, 2])`` -> ``False``;
    ``all_increasing([])`` -> ``True`` и ``all_increasing([7])`` -> ``True`` —
    для 0 и 1 элемента нарушать нечего.

    Подсказка: ``all(left < right for left, right in pairwise(values))``;
    для пустого ``pairwise`` результат ``all`` — ``True`` по определению.
    """
    raise NotImplementedError


def sliding_window(values: Iterable[int], size: int) -> list[tuple[int, ...]]:
    """Скользящее окно длины ``size``, слева направо.

    ``sliding_window("ABCDEFG", 3)`` -> ``[("A","B","C"), ("B","C","D"),
    ("C","D","E"), ("D","E","F"), ("E","F","G")]`` (5 окон);
    ``sliding_window([1, 2], 3)`` -> ``[]`` — элементов меньше окна;
    ``sliding_window([1, 2, 3], 1)`` -> ``[(1,), (2,), (3,)]``;
    ``sliding_window([1], 0)`` -> ``ValueError`` (в сообщении есть ``size``).

    Окна перекрываются: соседние отличаются одним элементом.

    Подсказка: ``deque(islice(iterator, size), maxlen=size)``; если после
    первого заполнения длина меньше ``size``, верните ``[]``.
    """
    raise NotImplementedError


def tail(values: Iterable[int], size: int) -> list[int]:
    """Последние ``size`` элементов, без материализации всего входа.

    ``tail([1, 2, 3, 4], 2)`` -> ``[3, 4]``;
    ``tail([1, 2], 5)`` -> ``[1, 2]`` — элементов меньше, вернуть все;
    ``tail([1, 2], 0)`` -> ``[]``;
    ``tail(iter([1, 2, 3, 4]), 3)`` -> ``[2, 3, 4]`` — вход может быть
    одноразовым итератором.

    Подсказка: ``deque(values, maxlen=size)``; для ``size <= 0`` верните
    пустой список, иначе ``maxlen=0`` молча съест весь вход и даст ``[]`` —
    результат тот же, но проверка явнее.
    """
    raise NotImplementedError


def window_sums(values: Iterable[int], size: int) -> list[int]:
    """Суммы по каждому скользящему окну длины ``size``.

    ``window_sums([1, 2, 3, 4], 2)`` -> ``[3, 5, 7]``;
    ``window_sums([1], 2)`` -> ``[]``;
    ``window_sums([], 1)`` -> ``[]``.

    Подсказка: переиспользуйте ``sliding_window`` — ошибку на ``size <= 0``
    он уже обработает сам.
    """
    raise NotImplementedError


def pairwise_iter(values: Iterable[int]) -> Iterator[tuple[int, int]]:
    """Вернуть именно итератор пар, не список.

    ``result = pairwise_iter(count())`` даёт итератор;
    ``[next(result) for _ in range(2)]`` -> ``[(0, 1), (1, 2)]``;
    список здесь не годится — на бесконечном входе он бы не построился.

    Подсказка: верните сам ``pairwise(values)``, не оборачивая в ``list``.
    """
    raise NotImplementedError


def first_window_above(values: Iterable[int], size: int, limit: int) -> tuple[int, ...] | None:
    """Первое окно длины ``size``, сумма которого больше ``limit``.

    ``first_window_above([1, 2, 3, 4], 2, 6)`` -> ``(3, 4)``: суммы окон
    равны 3, 5, 7 — первая превышающая 6 это последняя;
    ``first_window_above([1, 2, 3], 2, 100)`` -> ``None`` — ни одно окно не
    подошло;
    ``first_window_above([], 2, 0)`` -> ``None``.

    Сравнение строгое: сумма, равная ``limit``, не подходит.

    Подсказка: ``next((window for window in sliding_window(values, size) if
    sum(window) > limit), None)`` — второй аргумент ``next`` и есть ``None``.
    """
    raise NotImplementedError
