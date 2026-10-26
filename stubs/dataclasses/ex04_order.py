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

Практическое следствие: ``Version(1, 2) < 5`` — это ``TypeError``, а не
``False``. Тест ждёт именно исключение.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def declare_version() -> type:
    """Создать ``@dataclass(order=True)`` класс ``Version`` с ``major: int``, ``minor: int``.

    ``cls(1, 2) < cls(1, 3)`` -> ``True``;
    ``cls(2, 0) > cls(1, 99)`` -> ``True`` — первое поле важнее второго;
    ``cls(1, 2) <= cls(1, 2)`` -> ``True``;
    ``cls(1, 2) < 5`` -> ``TypeError``.

    Подсказка: ``@dataclass(order=True)``; поля объявляйте в том порядке, в
    котором они должны сравниваться.
    """
    raise NotImplementedError


def sorted_versions(versions: Iterable[object]) -> list[object]:
    """Отсортировать версии по возрастанию и вернуть список.

    ``sorted_versions([Version(2, 1), Version(1, 4), Version(1, 0)])`` ->
    ``[Version(1, 0), Version(1, 4), Version(2, 1)]``;
    ``sorted_versions([])`` -> ``[]``.

    Подсказка: ``sorted(versions)`` — ``order=True`` уже дал все операторы.
    """
    raise NotImplementedError


def max_version(versions: Iterable[object]) -> object | None:
    """Вернуть максимальную версию (или ``None`` для пустого входа).

    ``max_version([Version(1, 2), Version(3, 0)])`` -> ``Version(3, 0)``;
    ``max_version([])`` -> ``None`` — пустой вход не ошибка;
    ``max_version([Version(1, 2)])`` -> эта же версия.

    Подсказка: ``max`` на пустой последовательности бросает ``ValueError``,
    поэтому сначала материализуйте вход в список и проверьте пустоту.
    """
    raise NotImplementedError


def order_without_eq_is_rejected() -> bool:
    """Проверить, что ``order=True, eq=False`` невозможен.

    Объявите такой класс. Если при объявлении брошен ``ValueError`` — вернуть
    ``True``, иначе ``False``.

    Ошибка возникает в момент применения декоратора, а не при создании
    экземпляра.

    Подсказка: ``try: @dataclass(order=True, eq=False) class Bad: ...`` и
    ``except ValueError: return True``.
    """
    raise NotImplementedError
