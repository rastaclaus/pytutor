"""Упражнение 4. Сравнения и ``order=True``. Уровень 2.

По умолчанию dataclass генерирует только ``__eq__``. Параметр
``@dataclass(order=True)`` добавляет ``__lt__``, ``__le__``, ``__gt__``, ``__ge__``.
Сравнение идёт как у кортежа полей в порядке объявления: сначала первое поле,
при равенстве — второе и так далее.

Ограничения:

* ``order=True`` вместе с ``eq=False`` — ошибка ``ValueError`` при создании класса;
* сравнение с объектом другого типа возвращает ``NotImplemented``, а операторы
  ``<``/``>`` на нём бросают ``TypeError``;
* если класс уже определяет ``__lt__`` и подобные, ``order=True`` бросает
  ``TypeError``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def declare_version() -> type:
    """Создать ``@dataclass(order=True)`` класс ``Version`` с ``major: int``, ``minor: int``."""
    raise NotImplementedError


def sorted_versions(versions: Iterable[object]) -> list[object]:
    """Отсортировать версии по возрастанию и вернуть список."""
    raise NotImplementedError


def max_version(versions: Iterable[object]) -> object | None:
    """Вернуть максимальную версию (или ``None`` для пустого входа)."""
    raise NotImplementedError


def order_without_eq_is_rejected() -> bool:
    """Проверить, что ``order=True, eq=False`` невозможен.

    Объявите такой класс. Если при объявлении брошен ``ValueError`` — вернуть
    ``True``, иначе ``False``.
    """
    raise NotImplementedError
