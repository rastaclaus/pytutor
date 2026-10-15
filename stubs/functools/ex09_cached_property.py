"""Упражнение 9. ``functools.cached_property``. Уровень 5.

``cached_property`` — это свойство, значение которого вычисляется **один раз** и
затем сохраняется в ``__dict__`` экземпляра. Повторные обращения не пересчитывают
значение. Удаление атрибута (``del obj.value``) сбрасывает кэш.

Допишите класс ``HeavyValue``: сделайте ``value`` ленивым кэширующим свойством,
которое увеличивает ``self.computations`` ровно один раз на одно вычисление.
"""

from __future__ import annotations


class HeavyValue:
    """Хранит ``base`` и (лениво) его квадрат в ``value``."""

    def __init__(self, base: int) -> None:
        self.base = base
        self.computations = 0

    def value(self) -> int:
        """Вернуть ``base ** 2``, посчитав его лишь однажды.

        TODO: превратите это в ``functools.cached_property`` и увеличивайте
        ``self.computations`` при каждом реальном вычислении.
        """
        raise NotImplementedError
