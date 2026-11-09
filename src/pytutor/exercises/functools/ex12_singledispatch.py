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
попадёт в обработчик ``int`` (специфичнее зарегистрированных нет) и выдаст
``"целое: True"`` — приведение к ``int`` делать не нужно, f-строка печатает
значение как есть.

Диспетчеризация идёт по MRO: ``Point`` — это ``NamedTuple``, то есть подкласс
``tuple``. Регистрируйте его явно; обработчик ``tuple`` зарегистрирован не будет,
поэтому другие кортежи уйдут в fallback.
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
    """Общая реализация (fallback) для неизвестных типов.

    ``describe(3.14)`` -> ``"неизвестный тип: float"``;
    ``describe({1: 2})`` -> ``"неизвестный тип: dict"``;
    ``describe(None)`` -> ``"неизвестный тип: NoneType"``.

    Имя типа берётся через ``type(value).__name__``, а не ``repr`` —
    поэтому получается ``float``, а не ``<class 'float'>``.
    """
    raise NotImplementedError


# TODO: зарегистрируйте обработчики для int, str, list и Point, например:
#   @describe.register
#   def _(value: int) -> str:
#       ...
