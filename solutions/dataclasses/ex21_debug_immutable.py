"""Эталон упражнения 21 (dataclasses): найди баг — неизменяемая модель.

Три бага исходной версии:

1. ``with_channel`` присваивал поле замороженному объекту —
   ``FrozenInstanceError``; нужно ``dataclasses.replace``;
2. ``add_tag`` вызывал ``tuple.append`` — у кортежа нет ``append``; нужна
   конкатенация ``(*tags, tag)``;
3. ``audit_log`` возвращала результат ``list.append`` (``None``), теряя журнал;
   дописать нужно на копию или в исходный список, вернув сам список.
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace


@dataclass(frozen=True)
class NotificationSettings:
    """Неизменяемые настройки уведомлений."""

    channel: str
    retries: int = 3
    tags: tuple[str, ...] = field(default_factory=tuple)


def default_settings() -> NotificationSettings:
    """Настройки по умолчанию: канал ``email``."""
    return NotificationSettings("email")


def with_channel(settings: NotificationSettings, channel: str) -> NotificationSettings:
    """Копия настроек с другим каналом (исходный не меняется)."""
    return replace(settings, channel=channel)


def add_tag(settings: NotificationSettings, tag: str) -> NotificationSettings:
    """Копия настроек с дописанным тегом в конец (исходный не меняется)."""
    return replace(settings, tags=(*settings.tags, tag))


def audit_log(events: list[tuple[str, str]], change: str) -> list[tuple[str, str]]:
    """Дописать изменение в журнал и вернуть журнал."""
    events.append(("change", change))
    return events
