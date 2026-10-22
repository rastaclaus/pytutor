"""Упражнение 4. ``collections.namedtuple`` — именованные модели. Уровень 2.

``namedtuple`` — это кортеж с именованными полями: занимает меньше памяти, чем
словарь, но даёт доступ ``point.x`` вместо ``point["x"]``.

Полезные возможности: ``defaults`` (значения по умолчанию для хвостовых полей),
``_replace`` (копия с изменёнными полями), ``_asdict`` (превращение в словарь),
``_fields`` (имена полей), ``rename`` (авто-переименование некорректных имён).

В этом упражнении мы работаем с моделью ``Point`` (координаты) и ``Student``
(имя, курс, оценки).
"""

from __future__ import annotations

from collections import namedtuple
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable

Point = namedtuple("Point", ["x", "y"])
Student = namedtuple("Student", ["name", "year", "grades"], defaults=["", 0])


def point_from_dict(data: dict[str, int]) -> Point:
    """Создать ``Point`` из словаря ``{"x": ..., "y": ...}``."""
    raise NotImplementedError


def distance(p1: Point, p2: Point) -> float:
    """Евклидово расстояние между двумя точками."""
    raise NotImplementedError


def shift(point: Point, dx: int, dy: int) -> Point:
    """Вернуть новую точку, сдвинутую на ``(dx, dy)``."""
    raise NotImplementedError


def as_serializable(point: Point) -> dict[str, int]:
    """Вернуть точку в виде словаря."""
    raise NotImplementedError


def make_students(records: Iterable[tuple[str, int, list[int]]]) -> list[Student]:
    """Создать список ``Student`` из записей ``(имя, курс, оценки)``."""
    raise NotImplementedError


def class_head(student: Student) -> Student:
    """Вернуть копию студента с увеличенным на 1 курсом."""
    raise NotImplementedError
