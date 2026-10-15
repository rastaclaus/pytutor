"""Упражнение 8. Тонкости ``lru_cache``. Уровень 5.

Разные параметры ``lru_cache`` меняют поведение кэша:

* ``maxsize`` ограничивает размер; при переполнении вытесняется давно не
  использованный элемент, а повторный вызов пересчитывает значение;
* ``typed=False`` (по умолчанию) считает ``1`` и ``1.0`` одним ключом, а
  ``typed=True`` — разными;
* ``cache_info()`` отдаёт статистику (``hits``, ``misses``, ``maxsize``,
  ``currsize``), ``cache_clear()`` сбрасывает кэш.

Навесьте на функции декораторы с нужными параметрами и реализуйте тела.
"""

from __future__ import annotations


def add_typed(a: int, b: int) -> int:
    """Сумма двух чисел; кэш должен различать ``1`` и ``1.0``."""
    raise NotImplementedError


def add_untyped(a: int, b: int) -> int:
    """Сумма двух чисел; кэш не должен различать ``1`` и ``1.0``."""
    raise NotImplementedError


def limited(x: int) -> int:
    """Вернуть ``x * x`` с кэшем ровно на 2 элемента."""
    raise NotImplementedError
