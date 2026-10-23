"""Упражнение 13. Тонкая настройка полей: ``repr``, ``compare``, ``hash``. Уровень 5.

``field()`` умеет исключать поле из отдельных сгенерированных методов:

* ``repr=False`` — поля нет в ``__repr__`` (удобно для больших/секретных данных);
* ``compare=False`` — поле не участвует в ``__eq__`` и (при ``order=True``) в
  сравнениях;
* ``hash=False`` — поле не идёт в ``__hash__``, но остаётся в ``__eq__``.

Полезный приём: поле-«кэш» с ``compare=False, repr=False``, чтобы не ломать
равенство. И наоборот: ``compare=False, hash=False`` для поля, которое вообще не
должно влиять на идентичность.

``unsafe_hash=True`` заставляет сгенерировать ``__hash__`` даже для изменяемого
класса — на свой риск, потому что мутация после вставки в ``set`` ломает поиск.
"""

from __future__ import annotations

from dataclasses import dataclass, field


def declare_cache_entry() -> type:
    """Создать dataclass ``CacheEntry``.

    Поля:

    * ``key: str``;
    * ``payload: str``;
    * ``hits: int = 0`` — исключить из ``repr`` и из сравнения.

    Два объекта с разными ``hits`` должны быть равны.
    """
    raise NotImplementedError


def make_entry(key: str, payload: str, hits: int = 0) -> object:
    """Создать ``CacheEntry``."""
    raise NotImplementedError


def repr_excludes_hits() -> bool:
    """Вернуть ``True``, если ``repr`` не содержит слова ``hits``."""
    raise NotImplementedError


def equality_ignores_hits() -> bool:
    """Вернуть ``True``, если объекты с разными ``hits`` равны."""
    raise NotImplementedError


def declare_unsafe_hashable() -> type:
    """Создать изменяемый dataclass ``Raw`` с ``value: int`` и ``unsafe_hash=True``."""
    raise NotImplementedError


def unsafe_hash_is_generated() -> bool:
    """Вернуть ``True``, если экземпляр ``Raw`` хешируется."""
    raise NotImplementedError
