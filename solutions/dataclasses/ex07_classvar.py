"""Эталон упражнения 7: переменные класса."""

from __future__ import annotations

from dataclasses import dataclass, fields
from typing import ClassVar


def declare_ticket() -> type:
    @dataclass
    class Ticket:
        """Билет с общим счётчиком и префиксом."""

        prefix: ClassVar[str] = "TCK"
        counter: ClassVar[int] = 0

        number: int
        status: str = "open"

        def __post_init__(self) -> None:
            type(self).counter += 1

    return Ticket


def make_ticket(number: int) -> object:
    return declare_ticket()(number)


def field_names() -> list[str]:
    return [item.name for item in fields(declare_ticket())]


def ticket_id(ticket: object) -> str:
    ticket_cls = type(ticket)
    return f"{ticket_cls.prefix}-{ticket.number}"  # type: ignore[attr-defined]
