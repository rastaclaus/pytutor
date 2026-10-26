"""Упражнение 11. Сериализация: ``asdict`` и ``astuple``. Уровень 4.

``dataclasses.asdict(obj)`` рекурсивно превращает dataclass в словарь:

* вложенные dataclass → тоже словари;
* ``dict``/``list``/``tuple`` обходятся рекурсивно;
* прочие объекты копируются через ``copy.deepcopy``.

``astuple`` делает то же, но корнем служит кортеж. Оба метода:

* не включают ``ClassVar`` и ``InitVar``;
* бросают ``TypeError``, если аргумент — не экземпляр dataclass.

Важная деталь: результат — **глубокая копия**. Изменение полученного словаря не
затрагивает исходный объект. Проверить это на числе нельзя (числа неизменяемы),
поэтому в модели есть поле-список: ``Segment.labels``. Мутация списка внутри
снимка не должна менять список у исходного объекта.
"""

from __future__ import annotations

from dataclasses import dataclass


def declare_models() -> tuple[type, type]:
    """Создать два dataclass и вернуть их ``(Point, Segment)``.

    * ``Point``: ``x: int``, ``y: int``;
    * ``Segment``: ``start: Point``, ``end: Point``, ``weight: float = 1.0``,
      ``labels: list[str] = field(default_factory=list)``.

    ``labels`` — изменяемый дефолт, поэтому только через ``default_factory``:
    иначе ``@dataclass`` бросит ``ValueError``, а все отрезки делили бы один
    список.

    Тест проверяет, что у двух сегментов списки — разные объекты.
    """
    raise NotImplementedError


def to_dict(obj: object) -> dict:  # type: ignore[type-arg]
    """Вернуть ``asdict(obj)``.

    ``to_dict(Point(1, 2))`` -> ``{"x": 1, "y": 2}``;
    для не-dataclass аргумента ``asdict`` бросает ``TypeError`` —
    перехватывать не нужно.

    Подсказка: тело — один вызов ``asdict``.
    """
    raise NotImplementedError


def to_tuple(obj: object) -> tuple:  # type: ignore[type-arg]
    """Вернуть ``astuple(obj)``.

    ``to_tuple(Segment(Point(0, 0), Point(3, 4), 2.5))`` ->
    ``((0, 0), (3, 4), 2.5, [])`` — вложенные dataclass становятся кортежами,
    а поля идут в порядке объявления.

    Подсказка: тело — один вызов ``astuple``.
    """
    raise NotImplementedError


def nested_roundtrip() -> dict:  # type: ignore[type-arg]
    """Построить ``Segment(Point(0, 0), Point(3, 4), 2.5)`` и вернуть его ``asdict``.

    Ожидаемый результат::

        {
            "start": {"x": 0, "y": 0},
            "end": {"x": 3, "y": 4},
            "weight": 2.5,
            "labels": [],
        }

    Подсказка: ``declare_models()`` возвращает ``(Point, Segment)`` — не
    перепутайте порядок.
    """
    raise NotImplementedError


def is_deep_copy() -> bool:
    """Вернуть ``True``, если ``asdict`` даёт независимую копию.

    Сделайте ``Segment`` с непустым ``labels`` (например, ``["main"]``),
    получите его словарь и мутируйте **список** в снимке:
    ``data["labels"].append("mutated")``. Если у исходного объекта
    ``labels == ["main"]``, копия независима.

    Проверять только скалярное поле (например ``weight``) бессмысленно: числа
    неизменяемы, и такая проверка пройдёт при любой реализации.

    Подсказка: сравните ``segment.labels`` со списком-эталоном после мутации
    снимка и верните результат сравнения.
    """
    raise NotImplementedError
