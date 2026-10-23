"""Упражнение 18. Альтернативные конструкторы. Уровень 7.

У dataclass один сгенерированный ``__init__``. Дополнительные способы создания
объекта оформляют как ``@classmethod``:

* ``from_dict(data)`` — разбор словаря/JSON;
* ``from_row(row)`` — разбор кортежа или строки;
* ``parse(text)`` — разбор пользовательского ввода.

Внутри такого метода удобно вызывать ``cls(...)``, чтобы работали ``__post_init__``
и наследование (``cls``, а не жёсткое имя класса). ``InitVar`` помогает передать
в ``__post_init__`` данные, которые не нужно хранить.

Ошибки ввода: ``raise ValueError``/``KeyError`` — но лучше явная проверка и
``ValueError`` с внятным сообщением.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Mapping


def declare_measurement() -> type:
    """Создать dataclass ``Measurement``.

    Поля:

    * ``value: float``;
    * ``unit: str = "m"``;
    * ``source: str = field(default="unknown")``.

    Методы:

    * ``@classmethod from_dict(cls, data)`` — берёт ключи ``value`` (обязателен),
      ``unit``, ``source``; неизвестные ключи игнорирует; если нет ``value`` —
      ``ValueError`` с текстом "value";
    * ``@classmethod from_text(cls, text)`` — разбирает строку вида ``"12.5 m"``
      или ``"12.5"``; пустая строка → ``ValueError``.
    """
    raise NotImplementedError


def parse_measurement(text: str) -> object:
    """Разобрать строку через ``Measurement.from_text``."""
    raise NotImplementedError


def parse_measurement_dict(data: Mapping[str, Any]) -> object:
    """Создать через ``Measurement.from_dict``."""
    raise NotImplementedError


def serialize(measurement: object) -> dict:  # type: ignore[type-arg]
    """Вернуть словарь с ключами ``value``, ``unit``, ``source``."""
    raise NotImplementedError
