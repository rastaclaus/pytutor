"""Упражнение 8. ``slots=True``: компактные экземпляры. Уровень 4.

``@dataclass(slots=True)`` создаёт новый класс с ``__slots__``, поэтому у
экземпляров нет ``__dict__``: меньше памяти, быстрее доступ. Но:

* нельзя добавлять новые атрибуты, которых нет среди полей —
  ``AttributeError``;
* ``slots=True`` и явно заданный ``__slots__`` в классе → ``TypeError``;
* ``frozen=True`` с ``slots=True`` работает, а вот ``weakref`` без
  ``weakref_slot=True`` недоступен;
* ``weakref_slot=True`` допустим только вместе с ``slots=True``.

Проверить наличие ``__dict__``: ``hasattr(obj, "__dict__")``.
"""

from __future__ import annotations


def declare_slotted_point() -> type:
    """Создать ``@dataclass(slots=True)`` класс ``SlottedPoint`` с ``x: int``, ``y: int``."""
    raise NotImplementedError


def declare_weakref_point() -> type:
    """Создать ``@dataclass(slots=True, weakref_slot=True)`` класс ``WeakPoint``.

    Поля: ``x: int``, ``y: int``.
    """
    raise NotImplementedError


def has_instance_dict(obj: object) -> bool:
    """Вернуть ``True``, если у экземпляра есть ``__dict__``."""
    raise NotImplementedError


def foreign_attribute_fails() -> bool:
    """Проверить, что новому атрибуту в slotted-классе места нет.

    Создайте ``SlottedPoint(1, 2)`` и попробуйте присвоить ``point.z = 3``.
    Если поймали ``AttributeError`` — ``True``, иначе ``False``.
    """
    raise NotImplementedError


def weakref_is_supported() -> bool:
    """Вернуть ``True``, если на ``WeakPoint`` можно сделать ``weakref.ref``."""
    raise NotImplementedError
