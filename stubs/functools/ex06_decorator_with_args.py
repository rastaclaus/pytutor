"""Упражнение 6. Декораторы с аргументами. Уровень 4.

Декоратор с аргументами — это функция, которая возвращает декоратор
(«фабрика декораторов»). Не забудьте про ``functools.wraps``, чтобы сохранить
метаданные обёрнутой функции.

Реализуйте:

* ``repeat(times)`` — вызывает функцию ``times`` раз и возвращает список
  результатов;
* ``retry(times, exceptions)`` — делает до ``times`` попыток вызова; повторяет
  только при исключениях из ``exceptions``; если все попытки неудачны —
  пробрасывает последнее исключение.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def repeat(times: int) -> Callable[[F], F]:
    """Вернуть декоратор, вызывающий функцию ``times`` раз.

    Результат — список из ``times`` результатов. При ``times == 0`` список пуст.
    """
    raise NotImplementedError


def retry(
    times: int, exceptions: tuple[type[BaseException], ...] = (Exception,)
) -> Callable[[F], F]:
    """Вернуть декоратор с повторами при ошибках.

    Максимум ``times`` попыток (``times >= 1``). Если поймано исключение из
    ``exceptions`` — попытка повторяется. Если все попытки провалились,
    пробрасывается последнее исключение. Исключения не из ``exceptions``
    пробрасываются сразу.
    """
    raise NotImplementedError
