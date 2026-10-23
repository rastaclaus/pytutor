"""Эталон упражнения 10: ``dataclasses.replace``."""

from __future__ import annotations

from dataclasses import dataclass, fields, replace


def declare_settings() -> type:
    @dataclass(frozen=True)
    class Settings:
        """Настройки приложения."""

        host: str
        port: int
        debug: bool = False

    return Settings


def with_debug(settings: object, debug: bool) -> object:  # noqa: FBT001
    """Вернуть копию ``settings`` с другим ``debug`` (исходный не менять)."""
    return replace(settings, debug=debug)  # type: ignore[type-var]


def changed_fields() -> list[str]:
    return [item.name for item in fields(declare_settings()) if item.init]


def replace_unknown_field_fails() -> bool:
    settings = declare_settings()("localhost", 80)
    try:
        replace(settings, unknown=1)  # type: ignore[call-arg]
    except TypeError:
        return True
    return False
