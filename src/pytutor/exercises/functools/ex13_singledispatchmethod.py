"""Упражнение 13. ``functools.singledispatchmethod``. Уровень 7.

``singledispatchmethod`` — это ``singledispatch`` для методов: диспетчеризация
идёт по типу первого аргумента **после** ``self``.

Реализуйте класс ``Formatter.render`` и зарегистрируйте обработчики:

* ``int``   -> ``f"int:{value}"``
* ``str``   -> ``f"str:{value!r}"``
* fallback  -> ``f"?{value}"``

Обратите внимание на ``!r`` у строки: ``render("hi")`` даёт ``"str:'hi'"`` —
кавычки добавляет ``repr``. Для fallback кавычек нет: ``render(3.14)`` ->
``"?3.14"``, ``render(None)`` -> ``"?None"``.

``bool`` — подкласс ``int``, поэтому ``render(True)`` -> ``"int:True"``
(приведение к ``int`` не нужно, f-строка печатает значение как есть).
"""

from __future__ import annotations

from functools import singledispatchmethod


class Formatter:
    """Форматирует значения по-разному в зависимости от типа."""

    @singledispatchmethod
    def render(self, value: object) -> str:
        """Fallback для неизвестных типов.

        ``Formatter().render(3.14)`` -> ``"?3.14"``;
        ``Formatter().render(None)`` -> ``"?None"``;
        ``Formatter().render(True)`` сюда не попадёт — ``bool`` уйдёт в ``int``.

        Подсказка: ``return f"?{value}"`` — без ``!r``.
        """
        return f"?{value}"
    @render.register
    def _(self, value: int) -> str:
        return f"int:{value}"


    @render.register
    def _(self, value: str) -> str:
        return f"str:{value!r}"
