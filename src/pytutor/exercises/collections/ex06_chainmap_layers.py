"""Упражнение 6. ``collections.ChainMap`` — слои конфигурации. Уровень 3.

``ChainMap`` объединяет несколько словарей в один «вид» без их копирования.
Поиск ключа идёт слева направо: значение берётся из первого словаря, где ключ
встретился. Это классика для конфигурации: дефолты < пользовательские настройки
< переменные окружения.

Важная деталь: мутации (``__setitem__`` и др.) всегда меняют **только первый**
словарь. ``new_child`` создаёт новый слой поверх, ``parents`` скидывает верхний.
"""

from __future__ import annotations

from collections import ChainMap


def make_chain(defaults: dict[str, int], user: dict[str, int]) -> ChainMap[str, int]:
    """Создать ``ChainMap``, где ``user`` имеет приоритет над ``defaults``."""
    raise NotImplementedError


def lookup_priority(cm: ChainMap[str, int], key: str) -> int | None:
    """Вернуть значение ключа с учётом приоритета слоёв.

    Если ключа нет ни в одном слое — ``None``.
    """
    raise NotImplementedError


def flatten_layers(cm: ChainMap[str, int]) -> dict[str, int]:
    """Слить все слои в один словарь.

    Ключи, которые есть в нескольких слоях, берутся из более приоритетного
    (первого) слоя. ``flatten_layers(ChainMap({"a": 1}, {"a": 2, "b": 3}))`` ->
    ``{"a": 1, "b": 3}``.
    """
    raise NotImplementedError


def insert_layer(cm: ChainMap[str, int], updates: dict[str, int]) -> ChainMap[str, int]:
    """Вернуть новый ``ChainMap`` со слоем ``updates`` поверх ``cm``.

    Используйте ``new_child``.
    """
    raise NotImplementedError


def drop_first_layer(cm: ChainMap[str, int]) -> ChainMap[str, int]:
    """Вернуть ``ChainMap`` без верхнего слоя.

    Используйте ``parents``.
    """
    raise NotImplementedError


def write_through(cm: ChainMap[str, int], key: str, value: int) -> ChainMap[str, int]:
    """Записать ``key=value`` в первый (самый приоритетный) слой ``cm``.

    Мутация должна затронуть верхний словарь, а не нижележащие. Вернуть ``cm``.
    """
    raise NotImplementedError
