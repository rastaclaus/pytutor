"""Эталон упражнения 6: поля только для инициализации."""

from __future__ import annotations

from dataclasses import InitVar, dataclass, field, fields


def declare_user() -> type:
    @dataclass
    class User:
        """Пользователь, который не хранит пароль."""

        username: str
        password: InitVar[str]
        password_hash: str = field(init=False)

        def __post_init__(self, password: str) -> None:
            self.password_hash = f"hash-{password}"

    return User


def make_user(username: str, password: str) -> object:
    return declare_user()(username, password)


def initvar_field_names() -> list[str]:
    return [item.name for item in fields(declare_user())]


def has_password_attribute(user: object) -> bool:
    return hasattr(user, "password")
