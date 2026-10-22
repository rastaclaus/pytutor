"""Упражнение 18. ``collections.abc.MutableMapping`` — свой словарь с нуля. Уровень 7.

Чтобы получить полноценный изменяемый словарь, достаточно реализовать пять
методов ``MutableMapping``: ``__getitem__``, ``__setitem__``, ``__delitem__``,
``__iter__`` и ``__len__``. Всё остальное (``get``, ``keys``, ``pop``, ``in``,
``items``) абстрактный класс построит сам поверх них.

Это самый честный способ сделать «свой» словарь: полный контроль над хранилищем.
Здесь мы делаем логгирующий словарь, который записывает все операции, и словарь,
который считает обращения по ключам.
"""

from __future__ import annotations

from collections.abc import Iterator, MutableMapping


class LoggingDict(MutableMapping[str, int]):
    """Словарь, который записывает все операции чтения и записи.

    Журнал хранится в атрибуте ``log`` (список строк вида ``"get:key"``,
    ``"set:key=value"``, ``"del:key"``).

    Реализуйте пять обязательных методов; остальное сделает ``MutableMapping``.
    """

    def __init__(self) -> None:
        """Создать пустой словарь с журналом."""
        raise NotImplementedError

    def __getitem__(self, key: str) -> int:
        """Вернуть значение, записав в журнал ``get:key``."""
        raise NotImplementedError

    def __setitem__(self, key: str, value: int) -> None:
        """Записать значение, записав в журнал ``set:key=value``."""
        raise NotImplementedError

    def __delitem__(self, key: str) -> None:
        """Удалить ключ, записав в журнал ``del:key``."""
        raise NotImplementedError

    def __iter__(self) -> Iterator[str]:
        """Итерация по ключам."""
        raise NotImplementedError

    def __len__(self) -> int:
        """Число записей."""
        raise NotImplementedError


class AccessCountingDict(MutableMapping[str, int]):
    """Словарь, который считает обращения к ключам.

    Счётчики обращений хранятся в ``AccessCountingDict.access`` (обычный словарь:
    ключ -> сколько раз к нему обратились через ``get``/``__getitem__``).
    """

    def __init__(self, initial: dict[str, int] | None = None) -> None:
        """Создать словарь, заполнив из ``initial`` (если дан)."""
        raise NotImplementedError

    def __getitem__(self, key: str) -> int:
        """Вернуть значение и увеличить счётчик обращений к ключу."""
        raise NotImplementedError

    def __setitem__(self, key: str, value: int) -> None:
        """Записать значение (обращения не считаются)."""
        raise NotImplementedError

    def __delitem__(self, key: str) -> None:
        """Удалить ключ (и его счётчик обращений)."""
        raise NotImplementedError

    def __iter__(self) -> Iterator[str]:
        """Итерация по ключам."""
        raise NotImplementedError

    def __len__(self) -> int:
        """Число записей."""
        raise NotImplementedError

    def most_accessed(self, n: int) -> list[tuple[str, int]]:
        """Вернуть ``n`` самых часто запрашиваемых ключей с числом обращений."""
        raise NotImplementedError
