"""Упражнение 4. ``compose``/``pipeline`` и ``partialmethod``. Уровень 3.

Композиция функций — классический повод совместить ``reduce`` и ``partial``:
``compose`` собирает функции справа налево, ``pipeline`` — слева направо.

Отдельная тема — ``functools.partialmethod``: это ``partial`` для методов,
он позволяет зафиксировать часть аргументов метода прямо в теле класса.
"""

from __future__ import annotations

from collections.abc import Callable
from functools import partial, partialmethod, reduce
from typing import Any


def compose(*funcs: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """Скомпоновать функции справа налево.

    ``compose(f, g)(x)`` равно ``f(g(x))``. Без аргументов верните
    функцию-тождество (``lambda x: x``).

    Подсказка: соберите через ``reduce``, применяя функции в обратном порядке.
    """
    raise NotImplementedError


def pipeline(*funcs: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """Скомпоновать функции слева направо.

    ``pipeline(f, g)(x)`` равно ``g(f(x))``. Без аргументов — тождество.
    """
    raise NotImplementedError


def _check_length(text: str, min_len: int, max_len: int | None) -> bool:
    """Проверить, что ``min_len <= len(text)`` и (при заданном) ``len(text) <= max_len``."""
    if len(text) < min_len:
        return False
    return not (max_len is not None and len(text) > max_len)


def make_validator(
    min_len: int = 0, max_len: int | None = None
) -> Callable[[str], bool]:
    """Вернуть валидатор строки с зафиксированными границами длины.

    Используйте ``functools.partial`` от ``_check_length``.
    """
    raise NotImplementedError


class Logger:
    """Простой логгер, записывающий строки в ``self.messages``.

    Реализуйте ``log``, а методы ``warn`` и ``debug`` добавьте как
    ``functools.partialmethod`` от ``log`` с соответствующим ``level``.
    """

    def __init__(self, prefix: str) -> None:
        self.prefix = prefix
        self.messages: list[str] = []

    def log(self, message: str, *, level: str = "INFO") -> str:
        """Записать ``"{level}: {prefix} {message}"`` в ``messages`` и вернуть строку."""
        raise NotImplementedError

    warn = partialmethod(log, level="WARN")
    debug = partialmethod(log, level="DEBUG")
