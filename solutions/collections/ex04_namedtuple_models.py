"""Эталон упражнения 4: ``collections.namedtuple`` — именованные модели."""

from __future__ import annotations

from collections import namedtuple
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable

Point = namedtuple("Point", ["x", "y"])
Student = namedtuple("Student", ["name", "year", "grades"], defaults=["", 0])


def point_from_dict(data: dict[str, int]) -> Point:
    return Point(**data)


def distance(p1: Point, p2: Point) -> float:
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


def shift(point: Point, dx: int, dy: int) -> Point:
    return point._replace(x=point.x + dx, y=point.y + dy)


def as_serializable(point: Point) -> dict[str, int]:
    return point._asdict()


def make_students(records: Iterable[tuple[str, int, list[int]]]) -> list[Student]:
    return [Student(name, group, grades) for name, group, grades in records]


def class_head(student: Student) -> Student:
    return student._replace(year=student.year + 1)
