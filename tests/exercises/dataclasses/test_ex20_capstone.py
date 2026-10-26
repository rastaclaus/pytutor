"""Тесты упражнения 20: капстоун — модель домена."""

from __future__ import annotations

import pytest

from pytutor.exercises.dataclasses import ex20_capstone as ex


@pytest.fixture(autouse=True)
def _clean_history() -> None:
    """Очистить общий журнал между тестами (не зависит от решения)."""
    ex.Ticket.history.clear()


def test_new_ticket_defaults() -> None:
    ticket = ex.new_ticket("T1", "заголовок", 3)
    assert ticket.ticket_id == "T1"
    assert ticket.status == "new"
    assert ticket.priority == 3
    assert ticket.tags == ()


def test_priority_is_coerced_and_bounded() -> None:
    assert ex.new_ticket("T1", "x", "4").priority == 4
    with pytest.raises(ValueError, match="диапазон"):
        ex.new_ticket("T1", "x", 6)


def test_ticket_is_frozen() -> None:
    ticket = ex.new_ticket("T1", "x")
    with pytest.raises(Exception, match="cannot assign to field"):
        ticket.title = "y"  # type: ignore[misc]


def test_transition_returns_new_object() -> None:
    ticket = ex.new_ticket("T1", "x", 2)
    moved = ex.transition(ticket, "in_progress")
    assert moved is not ticket
    assert moved.status == "in_progress"
    assert ticket.status == "new"
    assert moved.previous_status == "new"


def test_transition_chain() -> None:
    ticket = ex.new_ticket("T1", "x")
    done = ex.transition(ex.transition(ticket, "in_progress"), "done")
    assert done.status == "done"
    assert done.previous_status == "in_progress"


def test_done_ticket_cannot_be_reopened() -> None:
    ticket = ex.transition(ex.new_ticket("T1", "x"), "done")
    with pytest.raises(ValueError, match="завершена"):
        ex.transition(ticket, "new")


def test_invalid_status_rejected() -> None:
    ticket = ex.new_ticket("T1", "x")
    with pytest.raises(ValueError, match="статус"):
        ex.transition(ticket, "archived")  # type: ignore[arg-type]


def test_history_is_recorded() -> None:
    ex.new_ticket("T1", "x")
    ex.transition(ex.new_ticket("T2", "y"), "in_progress")
    assert ex.history() == ["T1:new", "T2:new", "T2:in_progress"]


def test_history_is_a_copy() -> None:
    ex.new_ticket("T1", "x")
    snapshot = ex.history()
    snapshot.append("garbage")
    assert ex.history() == ["T1:new"]


def test_reset_history_clears_journal() -> None:
    ex.new_ticket("T1", "x")
    ex.reset_history()
    assert ex.history() == []


def test_project_report() -> None:
    project = ex.demo_project()
    report = ex.project_report(project)
    assert report["name"] == "demo"
    assert report["total"] == 3
    assert report["open"] == 2
    assert report["by_priority"] == {3: 1, 5: 2}


def test_open_tickets() -> None:
    project = ex.demo_project()
    assert [ticket.ticket_id for ticket in project.open_tickets()] == ["T1", "T2"]


def test_project_add_returns_self() -> None:
    project = ex.declare_project()("p")
    assert project.add(ex.new_ticket("T1", "x")) is project


def test_demo_project_statuses() -> None:
    project = ex.demo_project()
    assert [ticket.status for ticket in project.tickets] == ["new", "in_progress", "done"]


def test_snapshot_excludes_service_fields() -> None:
    ticket = ex.new_ticket("T1", "x", 2)
    snapshot = ex.ticket_snapshot(ticket)
    assert snapshot["ticket_id"] == "T1"
    assert snapshot["priority"] == 2
    assert "history" not in snapshot
    assert snapshot["previous_status"] is None
