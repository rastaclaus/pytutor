"""Упражнение 5. Зачем нужен ``functools.wraps``. Уровень 3.

Декоратор обычно подменяет функцию на ``wrapper``. Если не скопировать метаданные,
у обёрнутой функции «пропадут» имя и докстринг, а ``inspect`` перестанет видеть
исходную сигнатуру. Это и исправляет ``functools.wraps``.

Реализуйте два декоратора:

* ``identity_decorator`` — возвращает результат обёрнутой функции, но **без**
  ``wraps`` (метаданные теряются);
* ``preserving_decorator`` — то же самое, но с ``functools.wraps`` (метаданные
  и ``__wrapped__`` сохраняются).

Оба декоратора должны честно пробрасывать аргументы: ``identity_decorator``
принимает ``*args, **kwargs`` и вызывает ``func(*args, **kwargs)``.
"""

from __future__ import annotations

from functools import wraps
from typing import TYPE_CHECKING, Any, ParamSpec, TypeVar

if TYPE_CHECKING:
    from collections.abc import Callable

P = ParamSpec("P")
R = TypeVar("R")


def identity_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    """Обернуть ``func``, возвращая её результат, но не копируя метаданные.

    ``wrapped = identity_decorator(sample)``: ``wrapped(2, 3)`` -> ``5``;
    ``wrapped.__name__`` -> ``"wrapper"``, а не ``"sample"``;
    ``wrapped.__doc__`` -> ``None`` (или свой докстринг), а не докстринг
    ``sample``;
    ``hasattr(wrapped, "__wrapped__")`` -> ``False``.

    То есть поведение то же, а метаданные — от ``wrapper``. Именно это и
    показывает, зачем нужен ``wraps``.

    Подсказка: определите внутри ``wrapper(*args, **kwargs)`` и верните его,
    **не** вызывая ``wraps``.
    """
    raise NotImplementedError


def preserving_decorator[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    """Обернуть ``func``, сохранив метаданные через ``functools.wraps``.

    ``wrapped = preserving_decorator(sample)``: ``wrapped(2, 3)`` -> ``5``;
    ``wrapped.__name__`` -> ``"sample"``;
    ``wrapped.__doc__`` -> ``"Складывает два числа."``;
    ``wrapped.__wrapped__ is sample`` -> ``True``;
    ``inspect.signature(wrapped) == inspect.signature(sample)``.

    Подсказка: тот же ``wrapper``, но с ``@wraps(func)``. ``__wrapped__`` и
    подпись появляются автоматически — вручную их копировать не надо.
    """
    raise NotImplementedError
