"""Упражнение 21. Найди баг: работа с неизменяемой моделью. Уровень 5.

Модуль «сервис уведомлений» ниже выглядит рабочим: он строит настройки,
делает копии и ведёт аудит изменений. В нём **три бага**, из-за которых модель
либо мутирует там, где не должна, либо теряет данные. Исправьте их минимальными
правками.

Как искать: прогоните тесты (``uv run pytest -k ex21_debug``). Особое внимание —
на то, что происходит с исходным объектом после каждой операции.

Из упражнения 10: ``dataclasses.replace`` создаёт новый объект, не трогая
исходный; у неизменяемой модели это единственный способ «изменения».
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class NotificationSettings:
    """Неизменяемые настройки уведомлений."""

    channel: str
    retries: int = 3
    tags: tuple[str, ...] = field(default_factory=tuple)


def default_settings() -> NotificationSettings:
    """Настройки по умолчанию: канал ``email``, остальное из класса."""
    return NotificationSettings("email")


def with_channel(settings: NotificationSettings, channel: str) -> NotificationSettings:
    """Копия настроек с другим каналом (исходный не меняется)."""
    settings.channel = channel
    return settings


def add_tag(settings: NotificationSettings, tag: str) -> NotificationSettings:
    """Копия настроек с дописанным тегом в конец (исходный не меняется)."""
    return NotificationSettings(
        channel=settings.channel,
        retries=settings.retries,
        tags=settings.tags.append(tag),
    )


def audit_log(events: list[tuple[str, str]], change: str) -> list[tuple[str, str]]:
    """Дописать изменение в журнал и вернуть журнал.

    ``audit_log([("init", "email")], "channel=sms")`` ->
    ``[("init", "email"), ("change", "channel=sms")]``.
    """
    return events.append(("change", change))
