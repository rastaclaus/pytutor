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

Порядок полей важен: поле без дефолта не может идти после поля с дефолтом.
Поэтому ``name`` объявляется первым.
"""

from __future__ import annotations

from dataclasses import dataclass, field


def declare_inventory_item() -> type:
    """Создать dataclass ``InventoryItem``.

    Поля по порядку:

    * ``name: str`` — без значения по умолчанию;
    * ``quantity: int = 0``;
    * ``tags: list[str]`` — по умолчанию пустой список через ``default_factory``.

    ``item_cls("widget")`` даёт ``quantity == 0`` и ``tags == []``;
    ``item_cls("widget", quantity=3, tags=["new"])`` даёт ``quantity == 3`` и
    ``tags == ["new"]``;
    ``item_cls("a").tags is not item_cls("b").tags`` — списки независимы.

    Подсказка: ``tags: list[str] = field(default_factory=list)``. Запись
    ``tags: list[str] = []`` приведёт к ``ValueError`` уже при объявлении.
    """
    raise NotImplementedError


def add_tag(item: object, tag: str) -> object:
    """Добавить ``tag`` в ``item.tags`` и вернуть тот же объект.

    ``add_tag(item, "sale") is item`` -> ``True``;
    после вызова ``item.tags`` содержит ``"sale"`` последним элементом;
    повторный вызов с тем же тегом добавляет его ещё раз (список, без
    дедупликации).

    Подсказка: мутируйте ``item.tags`` на месте через ``append`` — не
    переприсваивайте поле новым списком, иначе ``is item`` останется ``True``,
    но исходный список не изменится.
    """
    raise NotImplementedError


def independent_defaults() -> bool:
    """Вернуть ``True``, если два экземпляра по умолчанию не делят один список.

    Создайте два экземпляра ``InventoryItem`` (разными именами) и верните
    ``first.tags is not second.tags``.

    Ожидаемо ``True``: ``default_factory`` вызывается на каждый экземпляр.
    Если вернуть ``False``, значит где-то использован общий список.

    Подсказка: ``is not``, а не ``!=`` — пустые списки равны по значению, но
    должны быть разными объектами.
    """
    raise NotImplementedError


def mutable_default_is_rejected() -> bool:
    """Проверить, что изменяемый дефолт запрещён.

    Попробуйте объявить dataclass с полем ``items: list[int] = []``. Если
    ``@dataclass`` бросил ``ValueError`` — вернуть ``True``, иначе ``False``.

    Важно: класс нужно объявлять внутри ``try`` — ошибка возникает в момент
    применения декоратора, а не при создании экземпляра.

    Подсказка: ``try: @dataclass class Bad: ... except ValueError: return True``
    и ``return False`` после блока.
    """
    raise NotImplementedError
