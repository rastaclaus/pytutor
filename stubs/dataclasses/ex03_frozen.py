"""Упражнение 3. Замороженные экземпляры: ``frozen=True``. Уровень 2.

``@dataclass(frozen=True)`` добавляет ``__setattr__`` и ``__delattr__``, которые
бросают ``dataclasses.FrozenInstanceError`` — подкласс ``AttributeError``.
Экземпляр становится неизменяемым после создания.

Побочный эффект: при ``frozen=True`` и ``eq=True`` (по умолчанию) dataclass
генерирует ``__hash__``, поэтому объекты можно класть в ``set`` и использовать
ключами словаря. У изменяемого dataclass ``__hash__`` равен ``None``.

Важно: «заморожен» только сам объект. Если поле — список, менять его содержимое
никто не мешает; ``frozen`` защищает от переприсваивания поля.

Тексты ошибок: ``FrozenInstanceError`` формируется stdlib и содержит
``cannot assign to field`` (``field`` — имя поля, например ``cannot assign to
field 'x'``). Своё исключение с другим текстом тест не примет.
"""

from __future__ import annotations

from dataclasses import dataclass, field


def declare_frozen_point() -> type:
    """Создать ``@dataclass(frozen=True)`` класс ``FrozenPoint`` с ``x: int``, ``y: int``.

    ``cls(1, 2)`` даёт объект с ``(x, y) == (1, 2)``;
    ``hash(cls(1, 2))`` работает, и ``len({cls(1, 2), cls(1, 2), cls(3, 4)})``
    равно 2.

    Подсказка: ``@dataclass(frozen=True)`` — без ``eq=False``, иначе
    ``__hash__`` не сгенерируется.
    """
    raise NotImplementedError


def declare_mutable_point() -> type:
    """Создать обычный (изменяемый) dataclass ``MutPoint`` с ``x: int``, ``y: int``.

    ``point.x = 10`` работает;
    ``hash(cls(1, 2))`` -> ``TypeError`` — у изменяемого dataclass
    ``__hash__ is None``.

    Подсказка: просто ``@dataclass`` без аргументов.
    """
    raise NotImplementedError


def try_to_mutate() -> bool:
    """Вернуть ``True``, если присваивание поля замороженному экземпляру падает.

    Создайте ``FrozenPoint(1, 2)`` и попробуйте присвоить ``point.x = 10``.
    Если поймали ``FrozenInstanceError`` — ``True``, иначе ``False``.

    Ловить надо именно ``FrozenInstanceError`` (или его предка
    ``AttributeError``), а не любое исключение: иначе тест прошёл бы и при
    случайной синтаксической ошибке.

    Подсказка: импортируйте ``FrozenInstanceError`` из ``dataclasses``.
    """
    raise NotImplementedError


def is_hashable(obj: object) -> bool:
    """Вернуть ``True``, если объект можно положить в ``set`` (``hash`` работает).

    ``is_hashable(FrozenPoint(1, 2))`` -> ``True``;
    ``is_hashable(MutPoint(1, 2))`` -> ``False``;
    ``is_hashable([1])`` -> ``False`` — список тоже нехешируем.

    Создавать объекты не нужно: функция работает с тем, что передали.

    Подсказка: ``try: hash(obj) except TypeError: return False``, иначе
    ``return True``.
    """
    raise NotImplementedError
