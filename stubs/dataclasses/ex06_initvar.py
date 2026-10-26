"""Упражнение 6. Поля только для инициализации: ``InitVar``. Уровень 3.

Иногда конструктору нужен параметр, который не становится полем. Пример: пароль
для вычисления хеша — хранить его нельзя.

``InitVar[T]`` делает поле псевдо-полем:

* оно попадает в ``__init__``;
* оно передаётся в ``__post_init__`` (в порядке объявления);
* в ``fields()`` его нет, и атрибута ``self.<имя>`` после инициализации тоже нет.

Если у ``InitVar`` нет значения по умолчанию, аргумент обязателен при создании.

Практическое следствие: ``cls("alice")`` без пароля — это ``TypeError``, а не
``ValueError``: сигнатуру проверяет сам Python.
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

    Поведение:

    * ``cls("alice", "secret")`` -> ``username == "alice"`` и
      ``password_hash == "hash-secret"``;
    * ``hasattr(user, "password")`` -> ``False``;
    * ``[f.name for f in fields(cls)] == ["username", "password_hash"]``;
    * ``cls("alice")`` -> ``TypeError``.

    Подсказка: параметр ``__post_init__`` должен называться так же, как
    ``InitVar``, и идти в том же порядке объявления.
    """
    raise NotImplementedError


def make_user(username: str, password: str) -> object:
    """Создать ``User``.

    ``make_user("alice", "secret").password_hash == "hash-secret"``.

    Подсказка: переиспользуйте ``declare_user()``.
    """
    raise NotImplementedError


def initvar_field_names() -> list[str]:
    """Вернуть имена настоящих полей ``User`` (``fields()``), без ``InitVar``.

    Ожидаемый результат — ``["username", "password_hash"]``: ``password``
    в ``fields()`` не попадает.

    Подсказка: ``[item.name for item in fields(cls)]``.
    """
    raise NotImplementedError


def has_password_attribute(user: object) -> bool:
    """Вернуть ``True``, если у экземпляра остался атрибут ``password``.

    ``make_user("alice", "secret")`` -> ``False``: ``InitVar`` не превращается
    в атрибут.

    Подсказка: ``hasattr(user, "password")``.
    """
    raise NotImplementedError
