"""Эталон упражнения 20: капстоун — модель домена."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field, replace
from typing import Any, ClassVar, Literal


class IntField:
    """Дескриптор целочисленного поля с границами."""

    def __init__(self, low: int = 1, high: int = 5) -> None:
        self.low = low
        self.high = high
        self.name = ""

    def __set_name__(self, owner: type, name: str) -> None:
        self.name = f"_{name}"

    def __get__(self, obj: Any, objtype: type | None = None) -> int:
        if obj is None:
            return self.low
        return getattr(obj, self.name, self.low)

    def __set__(self, obj: Any, value: Any) -> None:
        number = int(value)
        if not self.low <= number <= self.high:
            msg = f"значение вне диапазона [{self.low}, {self.high}]: {number}"
            raise ValueError(msg)
        object.__setattr__(obj, self.name, number)


Status = Literal["new", "in_progress", "done"]

OPEN_STATUSES: frozenset[str] = frozenset({"new", "in_progress"})
ALL_STATUSES: frozenset[str] = frozenset({"new", "in_progress", "done"})


@dataclass(frozen=True)
class Ticket:
    """Заявка: неизменяемая сущность с общим журналом переходов."""

    history: ClassVar[list[str]] = []

    ticket_id: str
    title: str
    priority: int = IntField(1, 5)  # type: ignore[assignment]
    status: Status = "new"
    tags: tuple[str, ...] = ()
    previous_status: Status | None = field(default=None, init=False, compare=False, repr=False)

    def __post_init__(self) -> None:
        """Проверить статус и записать переход в журнал."""
        if self.status not in ALL_STATUSES:
            msg = f"неизвестный статус: {self.status}"
            raise ValueError(msg)
        type(self).history.append(f"{self.ticket_id}:{self.status}")


def reset_history() -> None:
    Ticket.history.clear()


def history() -> list[str]:
    return list(Ticket.history)


def new_ticket(ticket_id: str, title: str, priority: object = 1) -> object:
    return Ticket(ticket_id=ticket_id, title=title, priority=priority)


def transition(ticket: object, status: Status) -> object:
    if ticket.status == "done" and status != "done":  # type: ignore[attr-defined]
        raise ValueError("заявка уже завершена, менять статус нельзя")
    updated = replace(ticket, status=status)  # type: ignore[type-var]
    object.__setattr__(updated, "previous_status", ticket.status)  # type: ignore[attr-defined]
    return updated


def declare_project() -> type:
    @dataclass
    class Project:
        """Агрегат заявок."""

        name: str
        tickets: list = field(default_factory=list)

        def add(self, ticket: object) -> Project:
            self.tickets.append(ticket)
            return self

        def open_tickets(self) -> list:
            return [ticket for ticket in self.tickets if ticket.status in OPEN_STATUSES]

        def by_priority(self) -> dict:
            counts: dict = {}
            for ticket in self.tickets:
                counts[ticket.priority] = counts.get(ticket.priority, 0) + 1
            return counts

    return Project


def project_report(project: object) -> dict:  # type: ignore[type-arg]
    return {
        "name": project.name,  # type: ignore[attr-defined]
        "total": len(project.tickets),  # type: ignore[attr-defined]
        "open": len(project.open_tickets()),  # type: ignore[attr-defined]
        "by_priority": project.by_priority(),  # type: ignore[attr-defined]
    }


def demo_project() -> object:
    project = declare_project()("demo")
    project.add(new_ticket("T1", "первая", 3))
    project.add(transition(new_ticket("T2", "вторая", 5), "in_progress"))
    third = transition(new_ticket("T3", "третья", 5), "in_progress")
    project.add(transition(third, "done"))
    return project


def ticket_snapshot(ticket: object) -> dict:  # type: ignore[type-arg]
    return asdict(ticket)  # type: ignore[type-var]
