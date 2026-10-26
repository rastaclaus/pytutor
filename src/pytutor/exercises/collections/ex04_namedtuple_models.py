"""Упражнение 4. ``collections.namedtuple`` — именованные модели. Уровень 2.

``namedtuple`` — это кортеж с именованными полями: занимает меньше памяти, чем
словарь, но даёт доступ ``point.x`` вместо ``point["x"]``. Он остаётся
неизменяемым и распаковывается как обычный кортеж.

Два готовых типа объявлены ниже и менять их не нужно::

    Point = namedtuple("Point", ["x", "y"])
    Student = namedtuple("Student", ["name", "year", "grades"], defaults=["", 0])

Полезные возможности:

* ``_replace(**kwargs)`` — **новая** копия с изменёнными полями (исходный
  объект не меняется);
* ``_asdict()`` — ``dict`` из полей;
* ``_fields`` — имена полей.

``defaults`` заполняет **хвостовые** поля: здесь это ``year = ""`` и
``grades = 0``, поэтому ``Student("Ада")`` валиден, а ``name`` обязателен.
Значения по умолчанию в этой модели намеренно «пустые» — тесты всегда передают
осмысленные ``year`` и ``grades``.

Термины, на которые ссылаются условия:

* **сдвиг** — прибавление ``dx``/``dy`` к координатам;
* **курс** — поле ``year``, целое число.
"""

from __future__ import annotations

from collections import namedtuple
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable

Point = namedtuple("Point", ["x", "y"])
Student = namedtuple("Student", ["name", "year", "grades"], defaults=["", 0])


def point_from_dict(data: dict[str, int]) -> Point:
    """Создать ``Point`` из словаря ``{"x": ..., "y": ...}``.

    ``point_from_dict({"x": 3, "y": 4})`` -> ``Point(x=3, y=4)``;
    ``point_from_dict({"y": 1, "x": 2})`` -> ``Point(x=2, y=1)`` — порядок
    ключей в словаре не важен, важно имя;
    ``point_from_dict({"x": 1})`` -> ``TypeError`` — поля ``y`` не хватает.

    Подсказка: ``Point(**data)``. Именно именованные аргументы, а не
    ``Point(*data.values())``: словарь не гарантирует порядок «x, y» по смыслу.
    """
    raise NotImplementedError


def distance(p1: Point, p2: Point) -> float:
    """Евклидово расстояние между двумя точками.

    ``distance(Point(0, 0), Point(3, 4))`` -> ``5.0``;
    ``distance(Point(1, 1), Point(1, 1))`` -> ``0.0``;
    ``distance(Point(0, 0), Point(0, -2))`` -> ``2.0`` — знак координаты не
    важен, он возводится в квадрат.

    Подсказка: ``((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5``. Тест
    сравнивает с ``5.0``, поэтому возвращайте именно ``float`` (корень из
    ``int`` уже даёт ``float``).
    """
    raise NotImplementedError


def shift(point: Point, dx: int, dy: int) -> Point:
    """Вернуть новую точку, сдвинутую на ``(dx, dy)``.

    ``shift(Point(1, 2), 10, -5)`` -> ``Point(11, -3)``;
    ``shift(Point(0, 0), 0, 0)`` -> ``Point(0, 0)``;
    исходная точка не меняется — ``Point`` неизменяем.

    Подсказка: ``point._replace(x=point.x + dx, y=point.y + dy)``. Создавать
    заново через ``Point(...)`` можно, но ``_replace`` короче и не зависит от
    порядка полей.
    """
    raise NotImplementedError


def as_serializable(point: Point) -> dict[str, int]:
    """Вернуть точку в виде словаря.

    ``as_serializable(Point(1, 2))`` -> ``{"x": 1, "y": 2}``;
    ``as_serializable(Point(-3, 0))`` -> ``{"x": -3, "y": 0}``.

    Подсказка: ``point._asdict()``. Тест сравнивает с обычным ``dict``, поэтому
    ``dict(point._asdict())`` тоже подойдёт.
    """
    raise NotImplementedError


def make_students(records: Iterable[tuple[str, int, list[int]]]) -> list[Student]:
    """Создать список ``Student`` из записей ``(имя, курс, оценки)``.

    ``make_students([("Иван", 2, [5, 4])])`` -> ``[Student(name="Иван", year=2,
    grades=[5, 4])]``;
    ``make_students([])`` -> ``[]``;
    ``make_students(iter([("Ада", 1, [])]))`` -> один студент — вход может быть
    одноразовым итератором.

    Порядок студентов — как в записях.

    Подсказка: списочное включение с распаковкой
    ``for name, year, grades in records`` и ``Student(name, year, grades)``.
    """
    raise NotImplementedError


def class_head(student: Student) -> Student:
    """Вернуть копию студента с увеличенным на 1 курсом.

    ``class_head(Student("Иван", 2, [5, 4]))`` -> ``Student(name="Иван", year=3,
    grades=[5, 4])``;
    исходный студент остаётся с прежним ``year`` — ``_replace`` создаёт новый
    объект;
    ``class_head(Student("Ада", 0, []))`` -> ``year == 1``.

    Внимание: дефолт ``year`` — пустая строка, поэтому
    ``class_head(Student("Ада"))`` упадёт с ``TypeError`` на ``"" + 1``. Это
    свойство модели, а не ошибка реализации; передавайте ``year`` числом.

    Подсказка: ``student._replace(year=student.year + 1)``.
    """
    raise NotImplementedError
