"""Упражнение 7. Переменные класса: ``ClassVar``. Уровень 3.

Аннотация ``ClassVar[T]`` говорит dataclass: «это не поле экземпляра». Такие
атрибуты:

* не попадают в ``__init__``;
* не возвращаются ``fields()``;
* не участвуют в ``__eq__``/``__repr__``;
* общие для всех экземпляров — менять их через экземпляр обычно ошибка.

Типичное применение — счётчик созданных объектов, константы конфигурации,
реестр подклассов.

Замечание: ``self.<name> = ...`` для ``ClassVar`` создаст атрибут экземпляра,
который перекроет классовый. Это разрешено, но почти всегда не то, что нужно.
"""

from __future__ import annotations

from dataclasses import dataclass


def declare_ticket() -> type:
    """Создать dataclass ``Ticket``.

    Поля:

    * ``prefix: ClassVar[str] = "TCK"``;
    * ``number: int``;
    * ``status: str = "open"``.

    В ``__post_init__`` увеличивайте ``Ticket.counter`` (``ClassVar[int] = 0``),
    чтобы считать созданные билеты.
    """
    raise NotImplementedError


def make_ticket(number: int) -> object:
    """Создать ``Ticket``."""
    raise NotImplementedError


def field_names() -> list[str]:
    """Вернуть имена полей ``Ticket`` — без ``prefix`` и ``counter``."""
    raise NotImplementedError


def ticket_id(ticket: object) -> str:
    """Вернуть идентификатор вида ``TCK-42`` для ``ticket.number == 42``."""
    raise NotImplementedError
