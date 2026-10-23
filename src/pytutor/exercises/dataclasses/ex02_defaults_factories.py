"""Упражнение 2. Значения по умолчанию и ``default_factory``. Уровень 1.

Значение по умолчанию задаётся обычным присваиванием::

    quantity: int = 0

Для изменяемых значений так делать нельзя: ``@dataclass`` бросает
``ValueError``, если значение по умолчанию нехешируемо (список, словарь,
множество). Причина — такой объект был бы общим для всех экземпляров.
Вместо этого используют фабрику::

    tags: list[str] = field(default_factory=list)

Фабрика вызывается при создании каждого экземпляра, поэтому списки получаются
независимыми.
"""

from __future__ import annotations

from dataclasses import dataclass, field


def declare_inventory_item() -> type:
    """Создать dataclass ``InventoryItem``.

    Поля по порядку:

    * ``name: str`` — без значения по умолчанию;
    * ``quantity: int = 0``;
    * ``tags: list[str]`` — по умолчанию пустой список через ``default_factory``.
    """
    raise NotImplementedError


def add_tag(item: object, tag: str) -> object:
    """Добавить ``tag`` в ``item.tags`` и вернуть тот же объект."""
    raise NotImplementedError


def independent_defaults() -> bool:
    """Вернуть ``True``, если два экземпляра по умолчанию не делят один список.

    Создайте два экземпляра ``InventoryItem`` без аргументов и проверьте, что
    ``a.tags`` и ``b.tags`` — разные объекты.
    """
    raise NotImplementedError


def mutable_default_is_rejected() -> bool:
    """Проверить, что изменяемый дефолт запрещён.

    Попробуйте объявить dataclass с полем ``items: list[int] = []``. Если
    ``@dataclass`` бросил ``ValueError`` — вернуть ``True``, иначе ``False``.
    """
    raise NotImplementedError
