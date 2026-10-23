"""Эталон упражнения 9: ``kw_only``."""

from __future__ import annotations

from dataclasses import KW_ONLY, dataclass


def declare_config() -> type:
    @dataclass
    class Config:
        """Настройки подключения."""

        host: str
        port: int
        _: KW_ONLY
        timeout: float = 5.0
        retries: int = 3

    return Config


def make_config(host: str, port: int) -> object:
    return declare_config()(host, port)


def positional_args() -> tuple[str, ...]:
    return tuple(declare_config().__match_args__)


def can_set_timeout_positionally() -> bool:
    config_cls = declare_config()
    try:
        config_cls("localhost", 80, 1.0)  # type: ignore[misc]
    except TypeError:
        return False
    return True
