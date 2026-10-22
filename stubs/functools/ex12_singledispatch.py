"""Упражнение 12. Обобщённые функции: ``functools.singledispatch``. Уровень 6.

``singledispatch`` позволяет одной функции вести себя по-разному в зависимости от
типа **первого** аргумента. Базовая реализация — это fallback, а конкретные типы
регистрируются через ``@describe.register`` с аннотацией типа.

Реализуйте ``describe`` и зарегистрируйте обработчики, возвращающие ровно такие
строки:

* ``int``   -> ``f"целое: {value}"``
* ``str``   -> ``f"строка длиной {len(value)}"``
* ``list``  -> ``f"список из {len(value)} элементов"``
* ``Point`` -> ``f"точка ({value.x}, {value.y})"``
* fallback  -> ``f"неизвестный тип: {type(value).__name__}"``

Подсказка: у ``bool`` базовым типом является ``int``, поэтому ``describe(True)``
попадёт в обработчик ``int`` (специфичнее зарегистрированных нет).
"""

from __future__ import annotations

from functools import singledispatch
from typing import NamedTuple


class Point(NamedTuple):
    """Точка на плоскости — пример для регистрации обработчика."""

    x: int
    y: int


@singledispatch
def describe(value: object) -> str:
    """Общая реализация (fallback) для неизвестных типов."""
    raise NotImplementedError


# TODO: зарегистрируйте обработчики для int, str, list и Point, например:
#   @describe.register
#   def _(value: int) -> str:
#       ...
