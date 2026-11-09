"""Тесты упражнения 21 (dataclasses): найди баг — неизменяемая модель.

Тесты описывают правильное поведение. В заготовке ``ex21_debug_immutable``
три бага; после исправлений все тесты должны стать зелёными.
"""

from __future__ import annotations

import pytest

from pytutor.exercises.dataclasses import ex21_debug_immutable as ex


def test_default_settings() -> None:
    settings = ex.default_settings()
    assert settings.channel == "email"
    assert settings.retries == 3
    assert settings.tags == ()


def test_with_channel_returns_new_object() -> None:
    settings = ex.default_settings()
    changed = ex.with_channel(settings, "sms")
    assert changed.channel == "sms"
    assert settings.channel == "email"  # исходный не тронут
    assert changed is not settings


def test_with_channel_keeps_other_fields() -> None:
    settings = ex.NotificationSettings("email", retries=5, tags=("a",))
    changed = ex.with_channel(settings, "push")
    assert changed.retries == 5
    assert changed.tags == ("a",)


def test_add_tag_appends() -> None:
    settings = ex.default_settings()
    tagged = ex.add_tag(settings, "vip")
    assert tagged.tags == ("vip",)
    tagged_twice = ex.add_tag(tagged, "urgent")
    assert tagged_twice.tags == ("vip", "urgent")


def test_add_tag_does_not_touch_original() -> None:
    settings = ex.default_settings()
    ex.add_tag(settings, "vip")
    assert settings.tags == ()


def test_audit_log_returns_list() -> None:
    events = [("init", "email")]
    result = ex.audit_log(events, "channel=sms")
    assert result == [("init", "email"), ("change", "channel=sms")]
    assert result is not None


def test_settings_are_frozen() -> None:
    settings = ex.default_settings()
    with pytest.raises(Exception, match="cannot assign to field"):
        settings.channel = "sms"  # type: ignore[misc]
