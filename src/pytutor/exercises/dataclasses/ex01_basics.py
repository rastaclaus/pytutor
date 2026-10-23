"""Упражнение 1. Основы ``@dataclass``. Уровень 1.

Декоратор ``@dataclass`` читает аннотации полей класса и генерирует методы
``__init__``, ``__repr__`` и ``__eq__``. Порядок параметров ``__init__`` — это
порядок объявления полей.

Метод ``__eq__`` сравнивает только экземпляры одного и того же класса: два
разных dataclass-класса с одинаковыми полями не равны, даже если значения
совпадают.

Реализуйте функции ниже. Внутри ``declare_point`` объявите класс через
декоратор; в остальных функциях просто используйте готовые объекты.
"""

from __future__ import annotations

from dataclasses import dataclass


def declare_point() -> type:
    """Создать и вернуть dataclass ``Point`` с полями ``x: int`` и ``y: int``.

    Класс должен называться ровно ``Point``, поля идут в порядке ``x``, ``y``.
    """
    raise NotImplementedError


def same(a: object, b: object) -> bool:
    """Вернуть ``True``, если ``a`` и ``b`` равны по значению (``==``)."""
    raise NotImplementedError


def as_text(obj: object) -> str:
    """Вернуть строковое представление объекта (``repr``)."""
    raise NotImplementedError
