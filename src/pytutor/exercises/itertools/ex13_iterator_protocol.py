"""Упражнение 13. Протокол итератора: ленивость и одноразовость. Уровень 6.

Итератор — это объект с ``__next__``, который отдаёт элементы по одному и после
исчерпания остаётся исчерпанным. Отсюда главное правило: **итератор одноразовый**.

* ``list(it)`` / ``sum(it)`` / ``for x in it`` опустошают итератор;
* повторный проход по нему даёт пустой результат;
* список и кортеж — не итераторы, а итерируемые: каждый ``iter()`` создаёт новый
  итератор, поэтому их можно обходить сколько угодно;
* ``iter(callable, sentinel)`` вызывает функцию до тех пор, пока она не вернёт
  ``sentinel``. Так читают из потока или файла без ``while True``.

Проверить ленивость можно счётчиком: пока результат не потребляют, генератор
не выполняет ни одной итерации.
"""

from __future__ import annotations

from itertools import count
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable, Iterable, Iterator


def exhaust(values: Iterable[int]) -> tuple[list[int], list[int]]:
    """Вернуть два последовательных прохода по ``values``.

    Для итератора второй проход пуст — это и есть демонстрация одноразовости.
    """
    return list(values), list(values)


def materialise(values: Iterable[int]) -> tuple[list[int], list[int]]:
    """Вернуть два одинаковых прохода, гарантированно сохранив данные."""
    saved = list(values)
    return saved, saved


def is_iterator(value: object) -> bool:
    """Проверить, что объект — итератор, а не просто итерируемое.

    Подсказка: у итератора есть и ``__iter__``, и ``__next__``; ``iter(obj) is obj``.
    """
    return iter(value) is value if hasattr(value, "__iter__") else False


def read_until_sentinel(read: Callable[[], int], sentinel: int) -> list[int]:
    """Читать значения, пока ``read()`` не вернёт ``sentinel``.

    Сам ``sentinel`` в результат не попадает.
    """
    return list(iter(read, sentinel))


def lazy_map_side_effects(values: Iterable[int], seen: list[int]) -> tuple[Iterator[int], list[int]]:
    """Вернуть ленивый итератор и журнал побочных эффектов.

    Итератор умножает элементы на 2 и дописывает исходное значение в ``seen``.
    До первого ``next()`` журнал должен оставаться пустым.
    """
    def doubled() -> Iterator[int]:
        for value in values:
            seen.append(value)
            yield value * 2
    return doubled(), seen


def count_until_limit(limit: int, seen: list[int]) -> int:
    """Потреблять генератор, пока сумма не превысит ``limit``.

    Генератор бесконечный: ``(i for i in range(...))``, но забирать нужно
    ровно столько, сколько требуется. Вернуть последнее добавленное число.
    Подсказка: ``itertools.count(1)`` + ранний ``break``.
    """
    total = 0
    last = 0
    for value in count(1):
        total += value
        seen.append(value)
        last = value
        if total > limit:
            break
    return last
