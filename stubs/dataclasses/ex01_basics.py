"""Упражнение 1. Основы ``@dataclass``. Уровень 1.

Декоратор ``@dataclass`` читает аннотации полей класса и генерирует методы
``__init__``, ``__repr__`` и ``__eq__``. Порядок параметров ``__init__`` — это
порядок объявления полей.

Метод ``__eq__`` сравнивает только экземпляры одного и того же класса: два
разных dataclass-класса с одинаковыми полями не равны, даже если значения
совпадают.

Реализуйте функции ниже. Внутри ``declare_point`` объявите класс через
декоратор; в остальных функциях просто используйте готовые объекты.

Обратите внимание: класс объявлен **внутри** функции, поэтому ``repr`` содержит
полное имя вида ``declare_point.<locals>.Point(x=1, y=2)``. Сравнивать ``repr``
с жёсткой строкой ``"Point(x=1, y=2)"`` не нужно — тест подставляет
``point_cls.__qualname__``.
"""

from __future__ import annotations

from dataclasses import dataclass


def declare_point() -> type:
    """Создать и вернуть dataclass ``Point`` с полями ``x: int`` и ``y: int``.

    ``point_cls = declare_point()``: ``point_cls.__name__ == "Point"``;
    ``point_cls(1, 2)`` даёт объект с ``x == 1``, ``y == 2``;
    ``repr(point_cls(1, 2))`` -> ``f"{point_cls.__qualname__}(x=1, y=2)"``;
    ``point_cls(1, 2) == point_cls(1, 2)`` -> ``True``, а
    ``point_cls(1, 2) != point_cls(1, 3)``;
    ``[item.name for item in fields(point_cls)] == ["x", "y"]``.

    Класс должен называться ровно ``Point``, поля идут в порядке ``x``, ``y``.

    Подсказка: объявите класс внутри функции и не забудьте навесить
    ``@dataclass`` — без декоратора не будет ни ``__init__``, ни ``__eq__``.
    """
    raise NotImplementedError


def same(a: object, b: object) -> bool:
    """Вернуть ``True``, если ``a`` и ``b`` равны по значению (``==``).

    ``same(Point(1, 2), Point(1, 2))`` -> ``True``;
    ``same(Point(1, 2), Other(1, 2))`` -> ``False`` — разные классы не равны,
    даже если поля совпадают;
    ``same([1, 2], [1, 2])`` -> ``True`` — функция про сравнение, а не про
    dataclass.

    Подсказка: просто ``a == b``.
    """
    raise NotImplementedError


def as_text(obj: object) -> str:
    """Вернуть строковое представление объекта (``repr``).

    ``as_text(Point(3, 4))`` -> ``f"{Point.__qualname__}(x=3, y=4)"``;
    ``as_text([1, 2])`` -> ``"[1, 2]"`` — подойдёт любой объект, не только
    dataclass.

    Подсказка: ``str(obj)`` не подойдёт — у dataclass нет своего ``__str__``,
    и результат зависит от того, что вернёт ``__repr__``; задача именно про
    ``repr``.
    """
    raise NotImplementedError
