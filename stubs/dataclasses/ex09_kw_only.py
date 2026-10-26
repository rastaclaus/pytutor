"""Упражнение 9. Только именованные аргументы: ``kw_only``. Уровень 4.

``@dataclass(kw_only=True)`` делает все поля доступными только по имени.
Альтернатива — псевдо-поле ``_: KW_ONLY``: все поля после него становятся
keyword-only. Это позволяет обойти правило «поле с дефолтом не может идти перед
полем без дефолта»:

::

    @dataclass
    class Point:
        x: float
        y: float
        _: KW_ONLY
        label: str = ""

Здесь ``label`` — kw-only, поэтому стоит после ``x``/``y``, хотя у него есть
дефолт, а у соседей его нет.

Keyword-only поля не попадают в ``__match_args__`` (значит, не участвуют в
позиционном ``match``).

Практическое следствие: ``Config("localhost", 80, 1.0)`` — ``TypeError``,
потому что третий позиционный аргумент принять некому.
"""

from __future__ import annotations


def declare_config() -> type:
    """Создать dataclass ``Config``.

    Поля:

    * ``host: str`` — позиционный;
    * ``port: int`` — позиционный;
    * ``timeout: float = 5.0`` — kw-only (через ``KW_ONLY`` или
      ``field(kw_only=True)``);
    * ``retries: int = 3`` — kw-only.

    ``Config("localhost", 80)`` должен работать, а
    ``Config("localhost", 80, 1.0)`` — нет.

    Поведение:

    * ``cls("localhost", 80)`` даёт ``timeout == 5.0`` и ``retries == 3``;
    * ``cls("localhost", 80, timeout=1.5, retries=0)`` переопределяет оба;
    * ``cls("localhost", 80, 1.5)`` -> ``TypeError``.

    Подсказка: ``_: KW_ONLY`` ставится как аннотированное поле между
    позиционными и kw-only полями.
    """
    raise NotImplementedError


def make_config(host: str, port: int) -> object:
    """Создать ``Config`` со значениями по умолчанию.

    ``make_config("localhost", 80)`` даёт ``timeout == 5.0`` и
    ``retries == 3``.

    Подсказка: переиспользуйте ``declare_config()``.
    """
    raise NotImplementedError


def positional_args() -> tuple[str, ...]:
    """Вернуть ``__match_args__`` класса ``Config``.

    Ожидаемый результат — ``("host", "port")``: kw-only поля в
    ``__match_args__`` не попадают.

    Подсказка: ``tuple(cls.__match_args__)``; вернуть нужно кортеж, а не
    список (тест сравнивает с кортежем).
    """
    raise NotImplementedError


def can_set_timeout_positionally() -> bool:
    """Вернуть ``True``, если третий аргумент можно передать позиционно.

    Ожидаемое значение — ``False``: ``timeout`` kw-only. Проверяйте это
    попыткой создать ``cls("localhost", 80, 1.0)`` и ловите ``TypeError``.

    Подсказка: не проверяйте сигнатуру вручную — создайте объект в ``try``;
    при успехе верните ``True``.
    """
    raise NotImplementedError
