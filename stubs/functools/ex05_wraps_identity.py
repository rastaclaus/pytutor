"""Упражнение 5. Зачем нужен ``functools.wraps``. Уровень 3.

Декоратор обычно подменяет функцию на ``wrapper``. Если не скопировать метаданные,
у обёрнутой функции «пропадут» имя и докстринг, а ``inspect`` перестанет видеть
исходную сигнатуру. Это и исправляет ``functools.wraps``.

Реализуйте два декоратора:

* ``identity_decorator`` — возвращает результат обёрнутой функции, но **без**
  ``wraps`` (метаданные теряются);
* ``preserving_decorator`` — то же самое, но с ``functools.wraps`` (метаданные
  и ``__wrapped__`` сохраняются).
"""

from __future__ import annotations

from functools import wraps
from typing import TYPE_CHECKING, Any, ParamSpec, TypeVar

if TYPE_CHECKING:
    from collections.abc import Callable

P = ParamSpec("P")
R = TypeVar("R")

def identity_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    """Обернуть ``func``, возвращая её результат, но не копируя метаданные."""
    raise NotImplementedError

def preserving_decorator[**P, R](func: Callable[P, R]) -> Callable[P, R]:
    """Обернуть ``func``, сохранив метаданные через ``functools.wraps``."""
    raise NotImplementedError
