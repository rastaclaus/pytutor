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
    """
    raise NotImplementedError


def make_config(host: str, port: int) -> object:
    """Создать ``Config`` со значениями по умолчанию."""
    raise NotImplementedError


def positional_args() -> tuple[str, ...]:
    """Вернуть ``__match_args__`` класса ``Config``."""
    raise NotImplementedError


def can_set_timeout_positionally() -> bool:
    """Вернуть ``True``, если третий аргумент можно передать позиционно."""
    raise NotImplementedError
