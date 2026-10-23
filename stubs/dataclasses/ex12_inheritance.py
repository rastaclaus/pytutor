"""Упражнение 12. Наследование. Уровень 5.

Dataclass-наследник собирает поля всех базовых классов: сначала в порядке MRO
(от ``object`` к потомку), затем свои. Поле, объявленное в наследнике, перекрывает
одноимённое поле базы (и его тип, и позицию — позиция остаётся от базы).

Правила и ловушки:

* генератор ``__init__`` общий: порядок параметров — порядок накопленных полей;
* дефолт у базового поля + поле без дефолта у наследника → ``TypeError``;
* ``super().__post_init__()`` нужно звать руками, если база тоже его определяет;
* ``slots=True`` в наследнике с полем, уже занятым в базе, → ``TypeError``.
"""

from __future__ import annotations

from dataclasses import dataclass


def declare_hierarchy() -> tuple[type, type]:
    """Создать два dataclass и вернуть ``(Base, Child)``.

    * ``Base``: ``name: str``; ``__post_init__`` ставит ``self.name`` в нижний
      регистр.
    * ``Child(Base)``: ``age: int = 0``; в ``__post_init__`` вызывает
      ``super().__post_init__()``, а затем увеличивает ``age`` на 1.
    """
    raise NotImplementedError


def make_child(name: str, age: int) -> object:
    """Создать ``Child``."""
    raise NotImplementedError


def inherited_field_order() -> list[str]:
    """Вернуть порядок полей ``Child``."""
    raise NotImplementedError


def default_before_non_default_is_rejected() -> bool:
    """Проверить, что поле без дефолта после поля с дефолтом запрещено."""
    raise NotImplementedError
