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

Практическое следствие: ``point.z = 3`` у slotted-класса — ``AttributeError``,
а не «просто добавился атрибут».
"""

from __future__ import annotations


def declare_slotted_point() -> type:
    """Создать ``@dataclass(slots=True)`` класс ``SlottedPoint`` с ``x: int``, ``y: int``.

    ``cls(1, 2)`` даёт ``(x, y) == (1, 2)``;
    ``hasattr(cls(1, 2), "__dict__")`` -> ``False``;
    ``set(cls.__slots__) == {"x", "y"}``;
    ``cls(1, 2).z = 3`` -> ``AttributeError``.

    Подсказка: ``@dataclass(slots=True)`` — больше ничего не нужно.
    """
    raise NotImplementedError


def declare_weakref_point() -> type:
    """Создать ``@dataclass(slots=True, weakref_slot=True)`` класс ``WeakPoint``.

    Поля: ``x: int``, ``y: int``.

    ``weakref.ref(cls(1, 2))()`` возвращает тот же объект, а не ``None``:
    без ``weakref_slot=True`` слабая ссылка на slotted-объект невозможна.

    Подсказка: ``@dataclass(slots=True, weakref_slot=True)``.
    """
    raise NotImplementedError


def has_instance_dict(obj: object) -> bool:
    """Вернуть ``True``, если у экземпляра есть ``__dict__``.

    ``has_instance_dict(SlottedPoint(1, 2))`` -> ``False``;
    ``has_instance_dict(MutPoint(1, 2))`` (обычный dataclass) -> ``True``;
    ``has_instance_dict(object())`` -> ``False`` — у ``object`` тоже нет
    словаря.

    Обратите внимание: проверять нужно именно ``__dict__``, а не
    ``vars(obj)`` — ``vars`` бросает ``TypeError`` у объектов без словаря.

    Подсказка: ``hasattr(obj, "__dict__")``.
    """
    raise NotImplementedError


def foreign_attribute_fails() -> bool:
    """Проверить, что новому атрибуту в slotted-классе места нет.

    Создайте ``SlottedPoint(1, 2)`` и попробуйте присвоить ``point.z = 3``.
    Если поймали ``AttributeError`` — ``True``, иначе ``False``.

    Подсказка: ``try/except AttributeError``.
    """
    raise NotImplementedError


def weakref_is_supported() -> bool:
    """Вернуть ``True``, если на ``WeakPoint`` можно сделать ``weakref.ref``.

    Ожидаемое значение — ``True``; проверяйте, что разыменованная ссылка
    возвращает **тот же** объект (``weakref.ref(point)() is point``), а не
    просто что вызов не упал.

    Подсказка: импортируйте ``weakref`` из стандартной библиотеки.
    """
    raise NotImplementedError
