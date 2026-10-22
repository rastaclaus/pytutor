"""Тесты упражнения 4: ``namedtuple`` — именованные модели."""

from __future__ import annotations

from pytutor.exercises.collections import ex04_namedtuple_models as ex


def test_point_from_dict() -> None:
    point = ex.point_from_dict({"x": 3, "y": 4})
    assert point.x == 3
    assert point.y == 4


def test_distance() -> None:
    assert ex.distance(ex.Point(0, 0), ex.Point(3, 4)) == 5.0
    assert ex.distance(ex.Point(1, 1), ex.Point(1, 1)) == 0.0


def test_shift() -> None:
    assert ex.shift(ex.Point(1, 2), 10, -5) == ex.Point(11, -3)


def test_as_serializable() -> None:
    assert ex.as_serializable(ex.Point(1, 2)) == {"x": 1, "y": 2}


def test_make_students() -> None:
    students = ex.make_students([("Иван", 2, [5, 4]), ("Мария", 1, [3])])
    assert students[0].name == "Иван"
    assert students[0].year == 2
    assert students[0].grades == [5, 4]
    assert len(students) == 2


def test_class_head() -> None:
    student = ex.Student("Иван", 2, [5, 4])
    promoted = ex.class_head(student)
    assert promoted.year == 3
    assert promoted.name == "Иван"
    assert student.year == 2  # исходный не изменился
