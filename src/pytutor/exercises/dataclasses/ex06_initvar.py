"""Упражнение 6. Поля только для инициализации: ``InitVar``. Уровень 3.

Иногда конструктору нужен параметр, который не становится полем. Пример: пароль
для вычисления хеша — хранить его нельзя.

``InitVar[T]`` делает поле псевдо-полем:

* оно попадает в ``__init__``;
* оно передаётся в ``__post_init__`` (в порядке объявления);
* в ``fields()`` его нет, и атрибута ``self.<имя>`` после инициализации тоже нет.

Если у ``InitVar`` нет значения по умолчанию, аргумент обязателен при создании.
"""

from __future__ import annotations

from dataclasses import InitVar, dataclass, field


def declare_user() -> type:
    """Создать dataclass ``User``.

    Поля:

    * ``username: str``;
    * ``password: InitVar[str]`` — не хранится как поле;
    * ``password_hash: str = field(init=False)`` — в ``__post_init__``
      присвойте ``password_hash = f"hash-{password}"``.

    Метод ``__post_init__(self, password: str)`` принимает ``InitVar``.
    """
    raise NotImplementedError


def make_user(username: str, password: str) -> object:
    """Создать ``User``."""
    raise NotImplementedError


def initvar_field_names() -> list[str]:
    """Вернуть имена настоящих полей ``User`` (``fields()``), без ``InitVar``."""
    raise NotImplementedError


def has_password_attribute(user: object) -> bool:
    """Вернуть ``True``, если у экземпляра остался атрибут ``password``."""
    raise NotImplementedError
