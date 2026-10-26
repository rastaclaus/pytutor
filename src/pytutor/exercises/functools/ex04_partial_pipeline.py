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

    ``make_validator(min_len=1)("ok")`` -> ``True``;
    ``make_validator(min_len=1)("")`` -> ``False``;
    ``make_validator(min_len=2, max_len=4)("ab")`` -> ``True`` и
    ``"abcde"`` -> ``False``;
    ``make_validator()("")`` -> ``True`` — обе границы по умолчанию не мешают.

    Границы включительные: строка ровно длины ``max_len`` проходит.

    Функция ``_check_length`` принимает три аргумента, а в конвейер (см.
    ``pipeline`` ниже) годится только функция от одного аргумента. Используйте
    ``functools.partial``, чтобы зафиксировать ``min_len`` и ``max_len``
    по имени и оставить свободным только ``text``.
    """
    raise NotImplementedError


def compose(*funcs: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """Скомпоновать функции справа налево.

    ``compose(_inc, _double)(3)`` -> ``7``, потому что ``_inc(_double(3))``;
    ``compose()(5)`` -> ``5`` — без аргументов функция-тождество;
    ``compose(_negate)(4)`` -> ``-4`` — одна функция, ничего не разворачивается.

    Каждая функция цепочки получает результат предыдущей, поэтому все они
    должны принимать ровно один аргумент.

    Подсказка: соберите через ``reduce``, применяя функции в обратном порядке
    (``reversed(funcs)``), с ``initial`` равным входному значению.
    """
    raise NotImplementedError


def pipeline(*funcs: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """Скомпоновать функции слева направо.

    ``pipeline(_inc, _double)(3)`` -> ``8``, потому что ``_double(_inc(3))``;
    ``pipeline()(5)`` -> ``5`` — тождество;
    ``pipeline(_negate)(4)`` -> ``-4``.

    Подсказка: это тот же ``reduce``, что и в ``compose``, но без разворота
    последовательности. Функцию-тождество писать не нужно: ``reduce`` без
    элементов вернёт ``initial``, то есть сам вход.
    """
    raise NotImplementedError


def make_trimmed_validator(min_len: int = 0, max_len: int | None = None) -> Callable[[str], bool]:
    """Вернуть валидатор, который сначала обрезает пробелы, затем проверяет длину.

    ``make_trimmed_validator(min_len=1)("  ok  ")`` -> ``True`` — пробелы не
    считаются;
    ``make_trimmed_validator(min_len=1)("   ")`` -> ``False`` — после обрезки
    строка пуста;
    ``make_trimmed_validator(min_len=2, max_len=4)("  abcde  ")`` -> ``False``.

    Обрезка идёт строго до проверки длины: ``str.strip`` снимает пробелы по
    краям, а не внутри строки.

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
        """Записать ``"{level}: {prefix} {message}"`` в ``messages`` и вернуть строку.

        ``Logger("app").log("started")`` -> ``"INFO: app started"``;
        ``log("careful", level="WARN")`` -> ``"WARN: app careful"``.

        Уровень — **именованный** аргумент (после ``*``), поэтому
        ``partialmethod`` должен фиксировать его по имени.
        """
        raise NotImplementedError

    warn = partialmethod(log, level="WARN")
    debug = partialmethod(log, level="DEBUG")
