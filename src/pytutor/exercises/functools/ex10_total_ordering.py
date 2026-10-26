"""Упражнение 10. ``functools.total_ordering``. Уровень 5.

Если класс задаёт ``__eq__`` и ``__lt__``, ``total_ordering`` достроит остальные
четыре операции сравнения (``<=``, ``>``, ``>=`` и отражённые) автоматически.

Реализуйте ``__eq__``, ``__lt__`` и ``__repr__`` для версии из кортежа чисел.
Сравнение с объектом другого типа должно возвращать ``NotImplemented``.

Что это значит на практике: ``__eq__`` при чужом типе возвращает
``NotImplemented``, и Python превращает результат в ``False`` (``Version(1) != 5``),
а ``__lt__`` при чужом типе даёт ``NotImplemented``, и Python бросает
``TypeError`` — именно это и проверяет тест.
"""

from __future__ import annotations

from functools import total_ordering


@total_ordering
class Version:
    """Версия, представленная кортежем чисел: ``Version(1, 2, 0)``."""

    def __init__(self, *parts: int) -> None:
        """Сохранить числа версии как кортеж."""
        self.parts = tuple(parts)

    def __eq__(self, other: object) -> bool:
        """Сравнение на равенство по ``parts``; иначе ``NotImplemented``.

        ``Version(1, 2) == Version(1, 2)`` -> ``True``;
        ``Version(1, 2) != Version(1, 3)`` -> ``True``;
        ``Version(1, 2) == (1, 2)`` -> ``False`` — сравнение с кортежем не
        поддерживается, возвращается ``NotImplemented``.

        Подсказка: сравнение кортежей ``parts`` уже умеет всё, что нужно, но
        сначала проверьте ``isinstance(other, Version)``.
        """
        raise NotImplementedError

    def __lt__(self, other: object) -> bool:
        """Сравнение «меньше» по ``parts``; иначе ``NotImplemented``.

        ``Version(1, 2) < Version(1, 10)`` -> ``True`` — кортежи сравниваются
        покомпонентно, ``2 < 10``;
        ``Version(1, 2) < Version(1, 2, 0)`` -> ``True`` — более короткий
        кортеж меньше при совпадающем префиксе;
        ``Version(1) < 5`` -> ``TypeError``.

        Подсказка: ``return self.parts < other.parts`` после проверки типа.
        """
        raise NotImplementedError

    def __repr__(self) -> str:
        """Вернуть строку вида ``"Version(1, 2, 0)"``.

        ``repr(Version(1, 2, 0))`` -> ``"Version(1, 2, 0)"``;
        ``repr(Version())`` -> ``"Version()"`` — без лишней запятой.

        Подсказка: ``", ".join(map(str, self.parts))`` внутри ``f"Version(...)"``.
        """
        raise NotImplementedError
