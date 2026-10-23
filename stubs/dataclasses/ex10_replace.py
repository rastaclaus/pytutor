"""Упражнение 10. Копирование с изменениями: ``dataclasses.replace``. Уровень 4.

``replace(obj, **changes)`` создаёт **новый** объект того же класса, вызывая
``__init__`` с изменёнными полями. Следствия:

* ``__post_init__`` выполняется заново — вычисляемые поля пересчитываются;
* ``changes`` принимает только поля, у которых ``init=True``; иначе
  ``ValueError``;
* неизвестное имя поля → ``TypeError``;
* ``InitVar`` без дефолта нужно передавать явно;
* для замороженных объектов ``replace`` — основной способ «изменить» значение.
"""

from __future__ import annotations

from dataclasses import dataclass


def declare_settings() -> type:
    """Создать ``@dataclass(frozen=True)`` класс ``Settings``.

    Поля:

    * ``host: str``;
    * ``port: int``;
    * ``debug: bool = False``.
    """
    raise NotImplementedError


def with_debug(settings: object, debug: bool) -> object:  # noqa: FBT001
    """Вернуть копию ``settings`` с другим ``debug`` (исходный не менять)."""
    raise NotImplementedError


def changed_fields() -> list[str]:
    """Вернуть имена полей ``Settings``, которые можно менять через ``replace``."""
    raise NotImplementedError


def replace_unknown_field_fails() -> bool:
    """Проверить, что ``replace`` с несуществующим полем бросает ``TypeError``."""
    raise NotImplementedError
