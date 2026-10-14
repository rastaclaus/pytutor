"""Тесты упражнения 13: ``singledispatchmethod``."""

from __future__ import annotations

from pytutor.exercises.functools import ex13_singledispatchmethod as ex


def test_int_method() -> None:
    assert ex.Formatter().render(5) == "int:5"


def test_str_method() -> None:
    assert ex.Formatter().render("hi") == "str:'hi'"


def test_fallback_method() -> None:
    assert ex.Formatter().render(3.14) == "?3.14"
    assert ex.Formatter().render(None) == "?None"


def test_bool_dispatches_to_int() -> None:
    assert ex.Formatter().render(True) == "int:True"


def test_method_works_on_instances() -> None:
    fmt = ex.Formatter()
    assert fmt.render(1) == "int:1"
    assert fmt.render("x") == "str:'x'"
