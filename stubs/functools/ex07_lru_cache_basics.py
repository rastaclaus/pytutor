"""Упражнение 7. Основы ``functools.lru_cache`` / ``functools.cache``. Уровень 4.

Мемоизация превращает экспоненциальную рекурсию в линейную. Декораторы
``functools.lru_cache(maxsize=None)`` и ``functools.cache`` кэшируют результаты по
аргументам вызова.

Ваша задача — дописать тела функций **и навесить подходящий кэширующий
декоратор**, чтобы повторные и вложенные вызовы не пересчитывались.

Подсказка: ``functools.cache`` — это просто ``lru_cache(maxsize=None)``.
"""

from __future__ import annotations


def fib(n: int) -> int:
    """Число Фибоначчи: ``fib(0) == 0``, ``fib(1) == 1``.

    Должно быть мемоизировано, чтобы ``fib(100)`` считался мгновенно.
    """
    raise NotImplementedError


def catalan(n: int) -> int:
    """Число Каталана: ``C(0) == 1``, ``C(n) == sum(C(i) * C(n - 1 - i))``.

    Рекурсивная реализация с мемоизацией.
    """
    raise NotImplementedError
