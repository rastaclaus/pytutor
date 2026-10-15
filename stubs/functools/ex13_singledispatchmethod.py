"""Упражнение 13. ``functools.singledispatchmethod``. Уровень 7.

``singledispatchmethod`` — это ``singledispatch`` для методов: диспетчеризация
идёт по типу первого аргумента **после** ``self``.

Реализуйте класс ``Formatter.render`` и зарегистрируйте обработчики:

* ``int``   -> ``f"int:{value}"``
* ``str``   -> ``f"str:{value!r}"``
* fallback  -> ``f"?{value}"``
"""

from __future__ import annotations

from functools import singledispatchmethod


class Formatter:
    """Форматирует значения по-разному в зависимости от типа."""

    @singledispatchmethod
    def render(self, value: object) -> str:
        """Fallback для неизвестных типов."""
        raise NotImplementedError

    # TODO: зарегистрируйте обработчики int и str через @render.register.
