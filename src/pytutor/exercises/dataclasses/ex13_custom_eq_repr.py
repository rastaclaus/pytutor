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

    Поведение:

    * ``repr(cls("k", "v", 7))`` не содержит слова ``hits``;
    * ``cls("k", "v", 1) == cls("k", "v", 99)`` -> ``True``.

    Подсказка: ``hits: int = field(default=0, repr=False, compare=False)``.
    """
    raise NotImplementedError


def make_entry(key: str, payload: str, hits: int = 0) -> object:
    """Создать ``CacheEntry``.

    ``make_entry("k", "v")`` даёт ``hits == 0``;
    ``make_entry("k", "v", 7)`` — ``hits == 7``.

    Подсказка: переиспользуйте ``declare_cache_entry()``.
    """
    raise NotImplementedError


def repr_excludes_hits() -> bool:
    """Вернуть ``True``, если ``repr`` не содержит слова ``hits``.

    Проверяйте на объекте с ненулевым ``hits`` (например, 7): если поле
    исключено корректно, слова в строке не будет вовсе.

    Подсказка: ``"hits" not in repr(entry)``. Проверка на нулевом ``hits``
    ничего не доказывает — значение могло просто совпасть с дефолтом.
    """
    raise NotImplementedError


def equality_ignores_hits() -> bool:
    """Вернуть ``True``, если объекты с разными ``hits`` равны.

    ``cls("k", "v", 1) == cls("k", "v", 99)`` -> ``True``;
    но ``cls("k", "v", 1) != cls("k", "other", 1)`` — остальные поля всё ещё
    сравниваются.

    Подсказка: создайте два объекта одного класса с одинаковыми ``key``/
    ``payload`` и разными ``hits``.
    """
    raise NotImplementedError


def declare_unsafe_hashable() -> type:
    """Создать изменяемый dataclass ``Raw`` с ``value: int`` и ``unsafe_hash=True``.

    ``hash(cls(1))`` работает, хотя класс не заморожен;
    ``cls(1).value = 2`` тоже работает — изменяемость сохранена.

    Подсказка: ``@dataclass(unsafe_hash=True)`` без ``frozen``.
    """
    raise NotImplementedError


def unsafe_hash_is_generated() -> bool:
    """Вернуть ``True``, если экземпляр ``Raw`` хешируется.

    Ожидаемое значение — ``True``.

    Подсказка: ``try: hash(raw_cls(1)) except TypeError: return False``.
    """
    raise NotImplementedError
