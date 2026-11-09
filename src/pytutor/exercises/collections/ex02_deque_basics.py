"""Упражнение 2. ``collections.deque`` — очередь и стек. Уровень 1.

``deque`` (double-ended queue) — двусторонняя очередь: добавляет и удаляет
элементы с обоих концов за O(1). Для списка ``pop(0)`` и ``insert(0, x)`` — O(n),
поэтому очередь на списке работает квадратично.

Ключевые операции:

* ``append`` / ``appendleft`` — добавить справа / слева;
* ``pop`` / ``popleft`` — забрать справа / слева;
* ``maxlen`` — жёсткое ограничение длины: при переполнении элемент с
  противоположного конца вытесняется автоматически.

Правила, которые проверяют тесты:

* ``maxlen`` — целое **больше нуля**; ``deque(..., maxlen=0)`` молча съест весь
  вход, поэтому неположительное значение нужно отклонить самим;
* у ``deque`` с ``maxlen`` длина никогда не превышает лимит, так что после
  ``append`` вытеснение уже произошло.

Термины, на которые ссылаются условия:

* **очередь (FIFO)** — забираем с того конца, куда не добавляли: первым пришёл,
  первым ушёл;
* **стек (LIFO)** — забираем с того же конца, куда добавляли: последним пришёл,
  первым ушёл.
"""

from __future__ import annotations

from collections import deque
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def make_queue(initial: Iterable[int]) -> deque[int]:
    """Создать ``deque`` из элементов ``initial``.

    ``list(make_queue([1, 2, 3]))`` -> ``[1, 2, 3]``;
    ``list(make_queue([]))`` -> ``[]``;
    ``isinstance(make_queue([1]), deque)`` -> ``True`` — вернуть нужно именно
    ``deque``, а не список.

    Подсказка: ``deque(initial)``.
    """
    raise NotImplementedError


def queue_push_pop(initial: Iterable[int], values: list[int]) -> list[int]:
    """Повести себя как очередь (FIFO).

    Добавить ``values`` в конец очереди из ``initial``, затем извлечь все
    элементы по одному с начала. Вернуть список извлечённых элементов.

    ``queue_push_pop([1, 2], [3, 4])`` -> ``[1, 2, 3, 4]`` — сначала старые,
    потом новые;
    ``queue_push_pop([], [5])`` -> ``[5]``;
    ``queue_push_pop([1], [])`` -> ``[1]``.

    Подсказка: ``extend(values)``, затем список из ``popleft()``. Длину берите
    до извлечения: ``range(len(dq))``.
    """
    raise NotImplementedError


def stack_push_pop(initial: Iterable[int], values: list[int]) -> list[int]:
    """Повести себя как стек (LIFO).

    Добавить ``values`` в конец стека из ``initial``, затем извлечь все элементы
    по одному с конца. Вернуть список извлечённых элементов.

    ``stack_push_pop([1, 2], [3, 4])`` -> ``[4, 3, 2, 1]`` — последний
    добавленный выходит первым;
    ``stack_push_pop([], [5])`` -> ``[5]``;
    ``stack_push_pop([1], [])`` -> ``[1]``.

    Подсказка: то же, что и в очереди, но ``pop()`` вместо ``popleft()``.
    """
    raise NotImplementedError


def bounded_history(values: Iterable[int], maxlen: int) -> list[int]:
    """Вернуть последние ``maxlen`` элементов.

    ``bounded_history([1, 2, 3, 4], 2)`` -> ``[3, 4]`` — старые вытеснены;
    ``bounded_history([1, 2], 5)`` -> ``[1, 2]`` — вход короче лимита, вернуть
    всё;
    ``bounded_history([], 3)`` -> ``[]``;
    ``bounded_history([1], 0)`` -> ``ValueError`` (в сообщении есть ``maxlen``).

    Ноль и отрицательное значение — ошибка, хотя ``deque(maxlen=0)`` формально
    допустим и просто выбрасывает все элементы.

    Подсказка: проверка ``maxlen <= 0``, затем ``list(deque(values,
    maxlen=maxlen))``.
    """
    raise NotImplementedError


def add_with_limit(history: deque[int], value: int, maxlen: int) -> deque[int]:
    """Добавить ``value`` в ``history``, не превышая ``maxlen``.

    Если длина очереди уже равна ``maxlen``, старый элемент вытесняется.
    Вернуть ту же очередь (тот же объект).

    ``history = deque([1, 2], maxlen=2)``: после ``add_with_limit(history, 3,
    2)`` в очереди ``[2, 3]``, а результат ``is history``;
    ``history = deque(maxlen=2)`` после трёх добавлений 1, 2, 3 содержит
    ``[2, 3]``;
    ``history = deque([1])`` и ``maxlen=5`` — просто ``[1, value]``.

    Подсказка: ``append``, затем ``while len(history) > maxlen: popleft()``.
    Цикл нужен на случай очереди без ``maxlen``; у очереди с ``maxlen`` он не
    выполнится ни разу. Не создавайте новый ``deque`` — тест проверяет
    тождество объекта.
    """
    raise NotImplementedError
