"""Тесты упражнения 9: ``kw_only``."""

from __future__ import annotations

from pytutor.exercises.dataclasses import ex09_kw_only as ex


def test_positional_fields_work() -> None:
    config = ex.make_config("localhost", 80)
    assert config.host == "localhost"
    assert config.port == 80
    assert config.timeout == 5.0
    assert config.retries == 3


def test_kw_only_fields_can_be_overridden() -> None:
    config_cls = ex.declare_config()
    config = config_cls("localhost", 80, timeout=1.5, retries=0)
    assert config.timeout == 1.5
    assert config.retries == 0


def test_kw_only_fields_cannot_be_positional() -> None:
    config_cls = ex.declare_config()
    try:
        config_cls("localhost", 80, 1.5)  # type: ignore[misc]
    except TypeError:
        pass
    else:  # pragma: no cover - должно падать
        raise AssertionError("timeout не должен передаваться позиционно")


def test_match_args_exclude_kw_only() -> None:
    assert ex.positional_args() == ("host", "port")


def test_can_set_timeout_positionally_is_false() -> None:
    assert ex.can_set_timeout_positionally() is False
