"""Упражнение 20. Капстоун: модель домена. Уровень 8.

Соберите вместе всё, что даёт ``dataclasses``, на задаче учёта заявок.

Идея: заявка — «значимый» неизменяемый объект, поэтому любое изменение — это
новый объект через ``replace``. Журнал переходов — ``ClassVar``, то есть общий
для всех экземпляров класса.

Класс ``Ticket`` уже объявлен ниже — это «данные» упражнения. Изучите, как в нём
соединены ``frozen=True``, дескриптор ``IntField``, ``ClassVar`` и
``field(init=False, compare=False, repr=False)``. Ваша задача — реализовать
функции и класс ``Project``.

Тексты ошибок, которые проверяются:

* приоритет вне диапазона — от дескриптора, в сообщении есть ``диапазон``;
* переход из ``done`` — ``ValueError`` со словом ``завершена``;
* неизвестный статус — ``ValueError`` со словом ``статус``;
* присваивание полю заявки — stdlib ``FrozenInstanceError`` с
  ``cannot assign to field``.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field, replace
from typing import Any, ClassVar, Literal


class IntField:
    """Дескриптор целочисленного поля с границами (уже реализован)."""

    def __init__(self, low: int = 1, high: int = 5) -> None:
        """Запомнить границы."""
        self.low = low
        self.high = high
        self.name = ""

    def __set_name__(self, owner: type, name: str) -> None:
        """Запомнить имя поля."""
        self.name = f"_{name}"

    def __get__(self, obj: Any, objtype: type | None = None) -> int:
        """Вернуть значение поля или нижнюю границу при доступе через класс."""
        if obj is None:
            return self.low
        return getattr(obj, self.name, self.low)

    def __set__(self, obj: Any, value: Any) -> None:
        """Привести к ``int`` и проверить границы."""
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
    """Очистить журнал ``Ticket.history``.

    После вызова ``history() == []``.

    Подсказка: ``Ticket.history.clear()`` — мутация на месте, а не
    переприсваивание: иначе ``ClassVar`` класса не изменится.
    """
    raise NotImplementedError


def history() -> list[str]:
    """Вернуть копию журнала ``Ticket.history`` (не сам список).

    ``new_ticket("T1", "x")`` -> ``history() == ["T1:new"]``;
    мутация возвращённого списка не меняет журнал: после
    ``history().append("garbage")`` следующий ``history()`` по-прежнему
    ``["T1:new"]``.

    Подсказка: ``list(Ticket.history)`` — именно копия, поэтому ``copy``
    тоже подойдёт, а вот ``return Ticket.history`` нет.
    """
    raise NotImplementedError


def new_ticket(ticket_id: str, title: str, priority: object = 1) -> object:
    """Создать заявку в статусе ``new``.

    ``new_ticket("T1", "заголовок", 3)`` даёт ``status == "new"``,
    ``priority == 3``, ``tags == ()``;
    ``new_ticket("T1", "x", "4").priority == 4`` — строка приводится к ``int``
    дескриптором;
    ``new_ticket("T1", "x", 6)`` -> ``ValueError`` (в сообщении есть
    ``диапазон``) — допустимы только 1..5;
    создание записывает ``"T1:new"`` в журнал.

    Подсказка: ``Ticket(ticket_id=..., title=..., priority=priority)``.
    Поля класса заморожены, поэтому все аргументы — именованные.
    """
    raise NotImplementedError


def transition(ticket: object, status: Status) -> object:
    """Вернуть новую заявку с другим статусом.

    * заявка в ``done`` не может перейти в другой статус — ``ValueError``
      с текстом "завершена";
    * результат — ``replace(ticket, status=status)``, после чего
      ``previous_status`` результата должен равняться прежнему статусу
      (поставьте его через ``object.__setattr__``: класс заморожен).

    Поведение:

    * ``moved = transition(new_ticket("T1", "x", 2), "in_progress")``:
      ``moved is not ticket``, ``moved.status == "in_progress"``,
      ``ticket.status == "new"``, ``moved.previous_status == "new"``;
    * цепочка ``new -> in_progress -> done`` даёт ``previous_status ==
      "in_progress"`` у финальной заявки;
    * ``transition(done_ticket, "new")`` -> ``ValueError`` (``завершена``);
    * ``transition(ticket, "archived")`` -> ``ValueError`` (``статус``) — его
      поднимает ``__post_init__`` нового объекта.

    Обратите внимание: ``replace`` вызывает ``__init__``, а значит
    ``__post_init__`` сработает заново и допишет строку
    ``"T1:in_progress"`` в журнал.

    Подсказка: проверку «уже завершена» делайте **до** ``replace``, иначе
    новый объект успеет записаться в журнал.
    """
    raise NotImplementedError


def declare_project() -> type:
    """Создать dataclass ``Project``.

    Поля:

    * ``name: str``;
    * ``tickets: list = field(default_factory=list)``.

    Методы:

    * ``add(ticket)`` — добавить заявку, вернуть ``self``;
    * ``open_tickets()`` — заявки в статусах из ``OPEN_STATUSES``;
    * ``by_priority()`` — ``{priority: count}`` по всем заявкам.

    Поведение:

    * ``project.add(ticket) is project``;
    * ``[t.ticket_id for t in demo_project().open_tickets()] == ["T1", "T2"]``
      — ``done`` в открытые не попадает;
    * ``by_priority()`` у демо-проекта -> ``{3: 1, 5: 2}``.

    Подсказка: ``add`` возвращает ``self`` (не ``None``), ``open_tickets``
    фильтрует по ``ticket.status in OPEN_STATUSES``.
    """
    raise NotImplementedError


def project_report(project: object) -> dict:  # type: ignore[type-arg]
    """Собрать сводку ``{"name", "total", "open", "by_priority"}``.

    У ``demo_project()``: ``name == "demo"``, ``total == 3``, ``open == 2``,
    ``by_priority == {3: 1, 5: 2}`` — ровно четыре ключа.

    Подсказка: ``total`` — ``len(project.tickets)``, ``open`` —
    ``len(project.open_tickets())``, остальное делегируйте методам.
    """
    raise NotImplementedError


def demo_project() -> object:
    """Собрать проект ``"demo"`` из трёх заявок.

    * ``T1`` — приоритет 3, остаётся ``new``;
    * ``T2`` — приоритет 5, переводится в ``in_progress``;
    * ``T3`` — приоритет 5, переводится в ``in_progress``, затем в ``done``.

    Ожидаемо: статусы в порядке добавления — ``["new", "in_progress", "done"]``.

    Подсказка: ``transition`` возвращает новую заявку — в проект добавляйте
    результат, а не исходную.
    """
    raise NotImplementedError


def ticket_snapshot(ticket: object) -> dict:  # type: ignore[type-arg]
    """Вернуть ``asdict(ticket)`` — снимок без ``ClassVar``.

    У ``new_ticket("T1", "x", 2)``: ``snapshot["ticket_id"] == "T1"``,
    ``snapshot["priority"] == 2``, ``snapshot["previous_status"] is None``,
    ключа ``"history"`` нет — ``ClassVar`` в ``asdict`` не попадает.

    Подсказка: ``asdict(ticket)``. Дескриптор ``priority`` при этом вернёт
    обычное число, приведённое к ``int``.
    """
    raise NotImplementedError
