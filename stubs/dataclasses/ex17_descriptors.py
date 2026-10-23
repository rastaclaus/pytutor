"""Упражнение 17. Поля-дескрипторы. Уровень 7.

Если значение по умолчанию у поля — объект-дескриптор (у него есть ``__set__``
или ``__get__``), dataclass ведёт себя иначе:

* в ``__init__`` присваивание идёт через ``descriptor.__set__(obj, value)``;
* чтение поля тоже идёт через ``__get__``;
* чтобы понять, есть ли у поля дефолт, dataclass вызывает
  ``descriptor.__get__(None, cls)``; если тот бросит ``AttributeError`` — дефолта
  нет.

Это способ добавить валидацию или приведение типа прямо в поле, не переопределяя
``__setattr__``.

Реализуйте дескриптор, приводящий значение к ``int`` и проверяющий границы.
"""

from __future__ import annotations

from typing import Any


class IntField:
    """Дескриптор целочисленного поля с проверкой диапазона.

    * ``__set_name__(owner, name)`` — запомните имя атрибута в экземпляре;
    * ``__get__(obj, objtype)`` — если ``obj is None``, верните ``default``
      (это нужно dataclass, чтобы найти дефолт); иначе верните значение;
    * ``__set__(obj, value)`` — приведите к ``int`` и проверьте границы
      ``0 <= value <= max_value``; иначе ``ValueError`` с текстом "диапазон".
    """

    def __init__(self, *, default: int = 0, max_value: int = 100) -> None:
        """Запомнить дефолт и верхнюю границу."""
        raise NotImplementedError

    def __set_name__(self, owner: type, name: str) -> None:
        """Запомнить имя поля."""
        raise NotImplementedError

    def __get__(self, obj: Any, objtype: type | None = None) -> int:
        """Вернуть значение или дефолт при доступе через класс."""
        raise NotImplementedError

    def __set__(self, obj: Any, value: Any) -> None:
        """Привести к ``int`` и проверить диапазон."""
        raise NotImplementedError


def declare_item() -> type:
    """Создать dataclass ``Item`` с полем ``quantity: int = IntField(default=1)``."""
    raise NotImplementedError


def make_item(quantity: object) -> object:
    """Создать ``Item`` из произвольного значения (дескриптор приведёт к int)."""
    raise NotImplementedError
