"""Упражнение 12. Наследование. Уровень 5.

Dataclass-наследник собирает поля всех базовых классов: сначала в порядке MRO
(от ``object`` к потомку), затем свои. Поле, объявленное в наследнике, перекрывает
одноимённое поле базы (и его тип, и позицию — позиция остаётся от базы).

Правила и ловушки:

* генератор ``__init__`` общий: порядок параметров — порядок накопленных полей;
* дефолт у базового поля + поле без дефолта у наследника → ``TypeError``;
* ``super().__post_init__()`` нужно звать руками, если база тоже его определяет;
* ``slots=True`` в наследнике с полем, уже занятым в базе, → ``TypeError``.

Порядок полей в наследнике: сначала ``name`` (из ``Base``), затем ``age``
(из ``Child``) — позиции наследуются от базы.
"""

from __future__ import annotations

from dataclasses import dataclass


def declare_hierarchy() -> tuple[type, type]:
    """Создать два dataclass и вернуть ``(Base, Child)``.

    * ``Base``: ``name: str``; ``__post_init__`` ставит ``self.name`` в нижний
      регистр.
    * ``Child(Base)``: ``age: int = 0``; в ``__post_init__`` вызывает
      ``super().__post_init__()``, а затем увеличивает ``age`` на 1.

    Поведение:

    * ``Child("Bob", 5)`` даёт ``name == "bob"`` и ``age == 6``;
    * ``Child("Bob")`` даёт ``age == 1``;
    * порядок полей ``Child`` — ``["name", "age"]``;
    * ``__post_init__`` у наследника обязателен: без него база не выполнится
      и ``name`` останется как есть.

    Подсказка: ``super().__post_init__()`` — первая строка, затем
    ``self.age += 1``.
    """
    raise NotImplementedError


def make_child(name: str, age: int) -> object:
    """Создать ``Child``.

    ``make_child("Bob", 5)`` даёт ``name == "bob"`` и ``age == 6``.

    Подсказка: ``declare_hierarchy()`` возвращает ``(Base, Child)`` — нужен
    второй элемент.
    """
    raise NotImplementedError


def inherited_field_order() -> list[str]:
    """Вернуть порядок полей ``Child``.

    Ожидаемый результат — ``["name", "age"]``.

    Подсказка: ``[item.name for item in fields(child_cls)]``.
    """
    raise NotImplementedError


def default_before_non_default_is_rejected() -> bool:
    """Проверить, что поле без дефолта после поля с дефолтом запрещено.

    Объявите базу с полем ``value: int = 0`` и наследника с полем
    ``extra: int`` без дефолта. Ожидается ``TypeError`` при объявлении
    наследника — вернуть ``True``.

    Исключение возникает в момент применения ``@dataclass`` к наследнику, а не
    при создании экземпляра.

    Подсказка: оба класса объявляйте внутри ``try``; ловите ``TypeError``.
    """
    raise NotImplementedError
