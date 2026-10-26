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

Тексты ошибок: у ``from_dict`` при отсутствии ``value`` нужно ``ValueError``, в
тексте которого есть ``value``; у ``from_text`` пустая (в том числе из одних
пробелов) строка — просто ``ValueError``, текст не проверяется.
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

    Поведение:

    * ``from_text("12.5 cm")`` -> ``value == 12.5``, ``unit == "cm"``;
    * ``from_text("7")`` -> ``value == 7.0``, ``unit == "m"`` (дефолт);
    * ``from_text("   ")`` -> ``ValueError``;
    * ``from_dict({"value": 3, "unit": "kg", "extra": 1})`` создаёт
      ``value == 3.0``, ``unit == "kg"``, ``source == "unknown"``; лишний ключ
      ``extra`` не мешает;
    * ``from_dict({"unit": "kg"})`` -> ``ValueError`` с ``value`` в тексте.

    Подсказка: ``value`` приводите к ``float`` (``7`` -> ``7.0``). Для строки
    ``text.split()`` уже отбрасывает пробелы, поэтому ``"   ".split() == []``.

    Обратите внимание: методы объявляются внутри класса, но возвращают объект
    через ``cls(...)``, а не через ``Measurement(...)``.
    """
    raise NotImplementedError


def parse_measurement(text: str) -> object:
    """Разобрать строку через ``Measurement.from_text``.

    ``parse_measurement("12.5 cm").unit == "cm"``;
    ``parse_measurement("7").value == 7.0``;
    ``parse_measurement("   ")`` -> ``ValueError``.

    Подсказка: ``declare_measurement().from_text(text)`` — методы у класса, а не
    у экземпляра, но вызов через экземпляр тоже работает.
    """
    raise NotImplementedError


def parse_measurement_dict(data: Mapping[str, Any]) -> object:
    """Создать через ``Measurement.from_dict``.

    ``parse_measurement_dict({"value": 1, "source": "sensor"})`` даёт
    ``source == "sensor"`` и ``unit == "m"``;
    ``parse_measurement_dict({"unit": "kg"})`` -> ``ValueError`` (в тексте есть
    ``value``).

    Подсказка: ``declare_measurement().from_dict(data)``.
    """
    raise NotImplementedError


def serialize(measurement: object) -> dict:  # type: ignore[type-arg]
    """Вернуть словарь с ключами ``value``, ``unit``, ``source``.

    ``serialize(parse_measurement_dict({"value": 1, "source": "sensor"}))`` ->
    ``{"value": 1.0, "unit": "m", "source": "sensor"}`` — ровно три ключа, без
    лишних.

    Подсказка: не используйте ``dataclasses.asdict`` «на всякий случай» —
    здесь нужен явный словарь из трёх полей; порядок ключей в сравнении не
    важен, но лишний ключ сломает тест.
    """
    raise NotImplementedError
