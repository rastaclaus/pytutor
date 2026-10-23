"""Упражнение 11. Сериализация: ``asdict`` и ``astuple``. Уровень 4.

``dataclasses.asdict(obj)`` рекурсивно превращает dataclass в словарь:

* вложенные dataclass → тоже словари;
* ``dict``/``list``/``tuple`` обходятся рекурсивно;
* прочие объекты копируются через ``copy.deepcopy``.

``astuple`` делает то же, но корнем служит кортеж. Оба метода:

* не включают ``ClassVar`` и ``InitVar``;
* бросают ``TypeError``, если аргумент — не экземпляр dataclass.

Важная деталь: результат — **глубокая копия**. Изменение полученного словаря не
затрагивает исходный объект.
"""

from __future__ import annotations

from dataclasses import dataclass


def declare_models() -> tuple[type, type]:
    """Создать два dataclass и вернуть их ``(Point, Segment)``.

    * ``Point``: ``x: int``, ``y: int``;
    * ``Segment``: ``start: Point``, ``end: Point``, ``weight: float = 1.0``.
    """
    raise NotImplementedError


def to_dict(obj: object) -> dict:  # type: ignore[type-arg]
    """Вернуть ``asdict(obj)``."""
    raise NotImplementedError


def to_tuple(obj: object) -> tuple:  # type: ignore[type-arg]
    """Вернуть ``astuple(obj)``."""
    raise NotImplementedError


def nested_roundtrip() -> dict:  # type: ignore[type-arg]
    """Построить ``Segment(Point(0, 0), Point(3, 4), 2.5)`` и вернуть его ``asdict``.

    Ожидаемый результат::

        {
            "start": {"x": 0, "y": 0},
            "end": {"x": 3, "y": 4},
            "weight": 2.5,
        }
    """
    raise NotImplementedError


def is_deep_copy() -> bool:
    """Вернуть ``True``, если ``asdict`` даёт независимую копию.

    Сделайте ``Segment``, получите его словарь, измените ``weight`` в словаре и
    проверьте, что у исходного объекта ``weight`` не изменился.
    """
    raise NotImplementedError
