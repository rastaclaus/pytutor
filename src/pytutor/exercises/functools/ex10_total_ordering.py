"""Упражнение 10. ``functools.total_ordering``. Уровень 5.

Если класс задаёт ``__eq__`` и ``__lt__``, ``total_ordering`` достроит остальные
четыре операции сравнения (``<=``, ``>``, ``>=`` и отражённые) автоматически.

Реализуйте ``__eq__``, ``__lt__`` и ``__repr__`` для версии из кортежа чисел.
Сравнение с объектом другого типа должно возвращать ``NotImplemented``.
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
        """Сравнение на равенство по ``parts``; иначе ``NotImplemented``."""
        raise NotImplementedError

    def __lt__(self, other: object) -> bool:
        """Сравнение «меньше» по ``parts``; иначе ``NotImplemented``."""
        raise NotImplementedError

    def __repr__(self) -> str:
        """Вернуть строку вида ``"Version(1, 2, 0)"``."""
        raise NotImplementedError
