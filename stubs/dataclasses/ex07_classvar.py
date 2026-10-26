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
Поэтому счётчик увеличивают через ``type(self).counter += 1`` — так изменение
попадает в класс, а не в экземпляр.
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

    Поведение:

    * ``[item.name for item in fields(cls)] == ["number", "status"]`` —
      ``prefix`` и ``counter`` не поля;
    * ``cls(1).prefix == "TCK"`` и ``cls(1) == cls(1)`` (``prefix`` в
      ``__eq__`` не участвует);
    * после трёх созданий ``cls.counter == 3``;
    * ``"counter" not in cls(4).__dict__`` — счётчик остался классовым.

    Подсказка: ``type(self).counter += 1`` (не ``self.counter += 1``).
    """
    raise NotImplementedError


def make_ticket(number: int) -> object:
    """Создать ``Ticket``.

    ``make_ticket(42)`` даёт ``number == 42`` и ``status == "open"``.

    Подсказка: переиспользуйте ``declare_ticket()``.
    """
    raise NotImplementedError


def field_names() -> list[str]:
    """Вернуть имена полей ``Ticket`` — без ``prefix`` и ``counter``.

    Ожидаемый результат — ``["number", "status"]``.

    Подсказка: ``fields(cls)`` уже отфильтровал ``ClassVar`` за вас.
    """
    raise NotImplementedError


def ticket_id(ticket: object) -> str:
    """Вернуть идентификатор вида ``TCK-42`` для ``ticket.number == 42``.

    ``ticket_id(make_ticket(42))`` -> ``"TCK-42"``;
    ``ticket_id(make_ticket(0))`` -> ``"TCK-0"``.

    Подсказка: префикс берите у класса (``type(ticket).prefix``), а не
    строкой-константой: тест проверяет связь с ``ClassVar``.
    """
    raise NotImplementedError
