"""Упражнение 19. Кросс-наборная связка: collections × itertools × functools. Уровень 7.

Модуль ``collections`` редко работает в одиночку: его типы отлично сочетаются с
``itertools`` и ``functools``. Здесь мы соединяем наборы:

* ``itertools.groupby`` + ``Counter`` — агрегация серий;
* ``itertools.batched`` + ``Counter`` — частоты по пакетам;
* ``functools.partial`` + ``defaultdict`` — фабрики с параметрами;
* ``itertools.count``/``islice`` + ``deque`` — потоковый хвост.

Главная идея упражнения: тип-приёмник (``Counter``, ``defaultdict``, ``deque``)
подключается к готовому ленивому источнику, и ручные циклы почти везде
оказываются лишними.

Термины, на которые ссылаются условия:

* **серия** — максимальный блок подряд идущих одинаковых значений;
* **пакет (chunk)** — кортеж из ``size`` подряд идущих элементов, хвост может
  быть короче;
* **хвост** — последние ``size`` элементов, увиденных к текущему моменту.

Подсказка по ``groupby``: он группирует только **подряд идущие** элементы и
отдаёт под-итератор, который становится пустым при переходе к следующей группе.
Поэтому группу сразу материализуют (``len(list(group))``).
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from functools import partial
from itertools import batched, count, groupby
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator


def count_by_value(values: Iterable[int]) -> Counter[int]:
    """Посчитать, сколько раз встречается каждое значение.

    ``count_by_value([1, 2, 1, 3, 1])`` -> ``Counter({1: 3, 2: 1, 3: 1})``;
    ``count_by_value([])`` -> ``Counter()``;
    ``count_by_value(iter([5, 5]))`` -> ``Counter({5: 2})`` — вход может быть
    одноразовым итератором.

    Подсказка: ``Counter(values)`` — весь цикл уже внутри конструктора.
    """
    raise NotImplementedError


def aggregate_runs(values: Iterable[str]) -> list[tuple[str, int]]:
    """Сгруппировать подряд идущие одинаковые значения.

    Вернуть список ``(значение, длина_серии)`` в порядке серий.

    ``aggregate_runs("aaabbc")`` -> ``[("a", 3), ("b", 2), ("c", 1)]``;
    ``aggregate_runs("")`` -> ``[]``;
    ``aggregate_runs("aba")`` -> ``[("a", 1), ("b", 1), ("a", 1)]`` — серий три,
    хотя значений два;
    ``aggregate_runs(["x", "x"])`` -> ``[("x", 2)]`` — работает не только со
    строкой.

    Подсказка: ``[(key, len(list(group))) for key, group in groupby(values)]``.
    ``len(group)`` не сработает: группа — итератор без ``__len__``.
    """
    raise NotImplementedError


def chunk_frequencies(values: Iterable[int], size: int) -> list[Counter[int]]:
    """Разбить ``values`` на пакеты по ``size`` и посчитать частоты в каждом.

    ``chunk_frequencies([1, 1, 2, 3, 3, 3], 2)`` -> ``[Counter({1: 2}),
    Counter({2: 1, 3: 1}), Counter({3: 2})]``;
    ``chunk_frequencies([], 3)`` -> ``[]``;
    ``chunk_frequencies([1, 2, 3], 5)`` -> ``[Counter({1: 1, 2: 1, 3: 1})]`` —
    неполный хвост сохраняется;
    ``chunk_frequencies([1], 0)`` -> ``ValueError`` (от ``batched``, в
    сообщении есть ``at least one``).

    Каждый элемент результата — ``Counter``, а не список.

    Подсказка: ``[Counter(chunk) for chunk in batched(values, size)]``.
    Проверку ``size`` не дублируйте — её делает ``batched``.
    """
    raise NotImplementedError


def make_incrementing_counter(start: int, step: int) -> defaultdict[str, int]:
    """Создать ``defaultdict``, фабрика которого раздаёт возрастающие значения.

    Каждый **новый** ключ получает следующее значение из последовательности
    ``start, start + step, start + 2 * step, ...``. Повторные обращения к уже
    существующему ключу возвращают сохранённое значение.

    ``counter = make_incrementing_counter(10, 5)``:
    ``counter["x"]`` -> ``10``, ``counter["y"]`` -> ``15``, ``counter["x"]``
    снова -> ``10``, ``counter["z"]`` -> ``20``;
    ``make_incrementing_counter(0, -1)["a"]`` -> ``0``, второй новый ключ -> ``-1``.

    Порядок ключей — порядок первого обращения.

    Подсказка: фабрика ``defaultdict`` — вызываемый объект без аргументов.
    ``partial(next, count(start, step))`` как раз такой: каждый вызов делает
    ``next(items)``. Прямо передать ``count(...)`` нельзя — это итератор, а не
    вызываемый объект.
    """
    raise NotImplementedError


def tail_stream(values: Iterable[int], size: int) -> Iterator[list[int]]:
    """Потоково выдавать хвост из последних ``size`` элементов.

    После каждого нового элемента выдаётся текущее окно:
    ``list(tail_stream([1, 2, 3], 2))`` -> ``[[1], [1, 2], [2, 3]]`` — первый
    снимок короче размера, это нормально;
    ``list(tail_stream([1], 5))`` -> ``[[1]]``;
    ``list(tail_stream([], 2))`` -> ``[]``;
    ``list(tail_stream([1, 2], 0))`` -> ``[[], []]`` — при ``maxlen=0`` очередь
    всегда пуста, но событие всё равно даёт снимок;
    ``list(tail_stream([1], -1))`` -> ``ValueError`` от ``deque``.

    Потоковый характер: результат — генератор, и вход читается по мере
    потребления.

    Подсказка: ``deque(maxlen=size)``, на каждом элементе ``append`` и
    ``yield list(window)``. Именно ``list(...)``: иначе все снимки будут ссылкой
    на одну и ту же изменяемую очередь.
    """
    raise NotImplementedError
