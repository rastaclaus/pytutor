"""Упражнение 3. Замороженные экземпляры: ``frozen=True``. Уровень 2.

``@dataclass(frozen=True)`` добавляет ``__setattr__`` и ``__delattr__``, которые
бросают ``dataclasses.FrozenInstanceError`` — подкласс ``AttributeError``.
Экземпляр становится неизменяемым после создания.

Побочный эффект: при ``frozen=True`` и ``eq=True`` (по умолчанию) dataclass
генерирует ``__hash__``, поэтому объекты можно класть в ``set`` и использовать
ключами словаря. У изменяемого dataclass ``__hash__`` равен ``None``.

Важно: «заморожен» только сам объект. Если поле — список, менять его содержимое
никто не мешает; ``frozen`` защищает от переприсваивания поля.
"""

from __future__ import annotations

from dataclasses import dataclass, field


def declare_frozen_point() -> type:
    """Создать ``@dataclass(frozen=True)`` класс ``FrozenPoint`` с ``x: int``, ``y: int``."""
    raise NotImplementedError


def declare_mutable_point() -> type:
    """Создать обычный (изменяемый) dataclass ``MutPoint`` с ``x: int``, ``y: int``."""
    raise NotImplementedError


def try_to_mutate() -> bool:
    """Вернуть ``True``, если присваивание поля замороженному экземпляру падает.

    Создайте ``FrozenPoint(1, 2)`` и попробуйте присвоить ``point.x = 10``.
    Если поймали ``FrozenInstanceError`` — ``True``, иначе ``False``.
    """
    raise NotImplementedError


def is_hashable(obj: object) -> bool:
    """Вернуть ``True``, если объект можно положить в ``set`` (``hash`` работает)."""
    raise NotImplementedError
