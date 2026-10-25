"""Упражнение 4. Сборка функций: ``partial``, ``reduce``, ``partialmethod``. Уровень 3.

Тема упражнения — как из готовых функций собирать новые. Три инструмента делят
работу так:

* ``functools.partial`` — **подгоняет сигнатуру**: из функции с несколькими
  аргументами делает функцию с одним (``make_validator``);
* ``functools.reduce`` — **соединяет** такие функции в цепочку
  (``compose``/``pipeline``): значение течёт от шага к шагу, поэтому каждый шаг
  обязан принимать ровно один аргумент — ровно то, что даёт ``partial``;
* ``functools.partialmethod`` — то же, что ``partial``, но для методов:
  фиксирует часть аргументов прямо в теле класса (``Logger``).

Именно поэтому тема собрана в одном упражнении: сначала функция «готовится»,
потом встраивается в конвейер, а для методов используется родственный приём.
"""

from __future__ import annotations

from functools import partial, partialmethod, reduce
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable


def _check_length(text: str, min_len: int, max_len: int | None) -> bool:
    """Проверить, что ``min_len <= len(text)`` и (при заданном) ``len(text) <= max_len``."""
    if len(text) < min_len:
        return False
    return not (max_len is not None and len(text) > max_len)


def make_validator(min_len: int = 0, max_len: int | None = None) -> Callable[[str], bool]:
    """Вернуть валидатор строки с зафиксированными границами длины.

    Функция ``_check_length`` принимает три аргумента, а в конвейер (см.
    ``pipeline`` ниже) годится только функция от одного аргумента. Используйте
    ``functools.partial``, чтобы зафиксировать ``min_len`` и ``max_len``
    по имени и оставить свободным только ``text``.
    """
    raise NotImplementedError


def compose(*funcs: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """Скомпоновать функции справа налево.

    ``compose(f, g)(x)`` равно ``f(g(x))``. Без аргументов верните
    функцию-тождество (``lambda x: x``).

    Каждая функция цепочки получает результат предыдущей, поэтому все они
    должны принимать ровно один аргумент. Подсказка: соберите через ``reduce``,
    применяя функции в обратном порядке.
    """
    raise NotImplementedError


def pipeline(*funcs: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """Скомпоновать функции слева направо.

    ``pipeline(f, g)(x)`` равно ``g(f(x))``. Без аргументов — тождество.

    Подсказка: это тот же ``reduce``, что и в ``compose``, но без разворота
    последовательности.
    """
    raise NotImplementedError


def make_trimmed_validator(min_len: int = 0, max_len: int | None = None) -> Callable[[str], bool]:
    """Вернуть валидатор, который сначала обрезает пробелы, затем проверяет длину.

    Соберите оба шага через ``pipeline``: ``str.strip`` приводит строку в
    порядок, а результат ``make_validator`` — уже готовая функция от одного
    аргумента — выносит вердикт. Здесь ``partial`` и ``reduce`` встречаются:
    подготовленная функция становится шагом конвейера.
    """
    raise NotImplementedError


class Logger:
    """Простой логгер, записывающий строки в ``self.messages``.

    Реализуйте ``log``, а методы ``warn`` и ``debug`` добавьте как
    ``functools.partialmethod`` от ``log`` с соответствующим ``level``.
    """

    def __init__(self, prefix: str) -> None:
        """Запомнить префикс и завести список записанных сообщений."""
        self.prefix = prefix
        self.messages: list[str] = []

    def log(self, message: str, *, level: str = "INFO") -> str:
        """Записать ``"{level}: {prefix} {message}"`` в ``messages`` и вернуть строку."""
        raise NotImplementedError

    warn = partialmethod(log, level="WARN")
    debug = partialmethod(log, level="DEBUG")
