"""Тесты упражнения 6: поля только для инициализации."""

from __future__ import annotations

import pytest

from pytutor.exercises.dataclasses import ex06_initvar as ex


def test_user_is_built() -> None:
    user = ex.make_user("alice", "secret")
    assert user.username == "alice"
    assert user.password_hash == "hash-secret"


def test_password_is_not_stored() -> None:
    user = ex.make_user("alice", "secret")
    assert ex.has_password_attribute(user) is False


def test_initvar_is_not_a_field() -> None:
    assert ex.initvar_field_names() == ["username", "password_hash"]


def test_password_is_required() -> None:
    user_cls = ex.declare_user()
    with pytest.raises(TypeError):
        user_cls("alice")  # type: ignore[call-arg]
