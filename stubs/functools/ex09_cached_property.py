"""Упражнение 9. ``functools.cached_property``. Уровень 5.

``cached_property`` — это свойство, значение которого вычисляется **один раз** и
затем сохраняется в ``__dict__`` экземпляра. Повторные обращения не пересчитывают
значение. Удаление атрибута (``del obj.value``) сбрасывает кэш.

Допишите класс ``HeavyValue``: сделайте ``value`` ленивым кэширующим свойством,
которое увеличивает ``self.computations`` ровно один раз на одно вычисление.

Ключевое отличие от ``property``: у ``cached_property`` нет сеттера, но
присваивание всё равно работает — значение просто кладётся в ``__dict__``
экземпляра и перекрывает вычисляемое.
"""

from __future__ import annotations


class HeavyValue:
    """Хранит ``base`` и (лениво) его квадрат в ``value``."""

    def __init__(self, base: int) -> None:
        """Запомнить ``base`` и обнулить счётчик вычислений."""
        self.base = base
        self.computations = 0

    def value(self) -> int:
        """Вернуть ``base ** 2``, посчитав его лишь однажды.

        ``HeavyValue(3).value`` -> ``9`` и ``computations == 1``;
        повторное обращение -> ``9`` и ``computations`` по-прежнему ``1``;
        ``del obj.value``, затем ``obj.value`` -> ``9`` и ``computations == 2``;
        ``obj.value = 100`` после первого вычисления -> дальше возвращается
        ``100``, а ``computations`` не растёт.

        TODO: превратите это в ``functools.cached_property`` и увеличивайте
        ``self.computations`` при каждом реальном вычислении.

        Подсказка: снимите скобки у ``def value(self)`` (``cached_property``
        заменяет метод дескриптором) и добавьте ``@cached_property``.
        """
        raise NotImplementedError
