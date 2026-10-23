"""Упражнение 19. Неизменяемое дерево: ``frozen`` + ``slots`` + ``kw_only``. Уровень 7.

Комбинация опций даёт «значимые» неизменяемые объекты:

* ``frozen=True`` — нельзя переприсвоить поле;
* ``slots=True`` — нет ``__dict__``, меньше памяти;
* ``kw_only=True`` — вызовы читаются как именованные аргументы;
* ``eq=True`` (по умолчанию) + ``frozen=True`` порождает ``__hash__``, поэтому
  узлы можно хранить в ``set`` и использовать как ключи.

Для дерева обычно нужны:

* ``parent: Node | None = field(default=None, repr=False, compare=False)`` —
  ссылка вверх не влияет на равенство и не печатается (иначе цикл/repr-взрыв);
* ``children: tuple[Node, ...]`` вместо списка — иначе ``frozen`` защищает лишь
  от переприсваивания, а содержимое списка остаётся изменяемым;
* «изменение» делается через ``dataclasses.replace``: возвращается новый узел.

Обратите внимание: ``replace`` не пересоберёт связи потомков — это ваша задача.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Self

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator


def declare_node() -> type:
    """Создать ``@dataclass(frozen=True, slots=True, kw_only=True)`` класс ``Node``.

    Поля:

    * ``name: str``;
    * ``children: tuple[Node, ...] = ()``;
    * ``parent: Node | None = field(default=None, repr=False, compare=False)``.

    Методы:

    * ``is_leaf()`` — нет потомков;
    * ``walk()`` — обход в глубину (сам узел, затем потомки), возвращает итератор имён;
    * ``with_child(child)`` — вернуть новый узел с добавленным потомком;
    * ``depth()`` — глубина поддерева (лист = 1).
    """
    raise NotImplementedError


def make_tree(structure: dict[str, object]) -> object:
    """Построить дерево из вложенного словаря ``{имя: {поддерево}}``.

    Например, ``{"root": {"a": {}, "b": {"c": {}}}}`` даёт дерево из 4 узлов.
    """
    raise NotImplementedError


def names_in_order(node: object) -> list[str]:
    """Вернуть имена узлов в порядке обхода ``walk()``."""
    raise NotImplementedError


def depth(node: object) -> int:
    """Вернуть глубину поддерева."""
    raise NotImplementedError


def add_child(node: object, name: str) -> object:
    """Вернуть новый узел с добавленным листом ``name``."""
    raise NotImplementedError
