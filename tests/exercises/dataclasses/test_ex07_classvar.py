"""Тесты упражнения 7: переменные класса."""

from __future__ import annotations

from pytutor.exercises.dataclasses import ex07_classvar as ex


def test_fields_exclude_classvar() -> None:
    assert ex.field_names() == ["number", "status"]


def test_init_does_not_take_prefix() -> None:
    ticket_cls = ex.declare_ticket()
    ticket = ticket_cls(1)
    assert ticket.prefix == "TCK"


def test_ticket_id() -> None:
    ticket = ex.make_ticket(42)
    assert ex.ticket_id(ticket) == "TCK-42"


def test_counter_is_shared() -> None:
    ticket_cls = ex.declare_ticket()
    ticket_cls(1)
    ticket_cls(2)
    ticket_cls(3)
    assert ticket_cls.counter == 3
    assert "counter" not in ticket_cls(4).__dict__


def test_classvar_does_not_affect_equality() -> None:
    ticket_cls = ex.declare_ticket()
    assert ticket_cls(1) == ticket_cls(1)
