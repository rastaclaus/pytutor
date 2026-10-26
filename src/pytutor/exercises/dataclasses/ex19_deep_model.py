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
Конкретно: ``with_child`` обязан проставить новому потомку ``parent``, указывающий
на **новый** узел (не на старый). Так как класс заморожен, поле ``parent``
ставится через ``object.__setattr__(child, "parent", grown)``.
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

    Поведение:

    * ``cls(name="leaf").is_leaf() is True`` и ``depth() == 1``;
    * узлы хешируются: ``len({cls(name="a"), cls(name="a")}) == 1``;
    * ``cls(name="a") == cls(name="a", parent=cls(name="p"))`` — ``parent`` не
      влияет на равенство;
    * ``not hasattr(cls(name="a"), "__dict__")``;
    * ``node.name = "b"`` -> ``FrozenInstanceError`` (в сообщении есть
      ``cannot assign to field``);
    * ``with_child`` возвращает **новый** узел; новый потомок получает
      ``parent``, ссылающийся на этот новый узел.

    Подсказка: ``walk`` — генератор с ``yield self.name`` и
    ``yield from child.walk()``; ``depth`` — ``1 + max(...)`` по потомкам
    (для листа просто ``1``). В ``with_child`` создайте узел, затем
    ``object.__setattr__(child, "parent", grown)`` и верните ``grown``.
    """
    raise NotImplementedError


def make_tree(structure: dict[str, object]) -> object:
    """Построить дерево из вложенного словаря ``{имя: {поддерево}}``.

    Например, ``{"root": {"a": {}, "b": {"c": {}}}}`` даёт дерево из 4 узлов.
    ``names_in_order(tree)`` -> ``["root", "a", "b", "c"]``;
    ``depth(tree)`` -> ``3``;
    ``tree.children[0].parent is tree`` — ``make_tree`` сам расставляет
    обратные ссылки.

    Порядок потомков — порядок ключей словаря (в Python 3.7+ он гарантирован).

    Подсказка: рекурсивный помощник, который сначала строит потомков, затем
    создаёт узел и проставляет ``object.__setattr__(child, "parent", node)``.
    Верхний уровень — ровно одна пара ``имя: поддерево``.
    """
    raise NotImplementedError


def names_in_order(node: object) -> list[str]:
    """Вернуть имена узлов в порядке обхода ``walk()``.

    ``names_in_order(make_tree({"root": {"a": {}, "b": {"c": {}}}}))`` ->
    ``["root", "a", "b", "c"]`` — родитель раньше потомков, потомки в порядке
    объявления.

    Подсказка: ``list(node.walk())``.
    """
    raise NotImplementedError


def depth(node: object) -> int:
    """Вернуть глубину поддерева.

    ``depth(make_tree({"root": {}}))`` -> ``1``;
    ``depth(make_tree({"root": {"a": {}, "b": {"c": {}}}}))`` -> ``3``.

    Подсказка: делегируйте в ``node.depth()``.
    """
    raise NotImplementedError


def add_child(node: object, name: str) -> object:
    """Вернуть новый узел с добавленным листом ``name``.

    ``tree = make_tree({"root": {}})``; ``grown = add_child(tree, "x")``:
    ``grown is not tree``, ``tree.children == ()``,
    ``[child.name for child in grown.children] == ["x"]`` и
    ``grown.children[0].parent is grown`` — новый потомок связан с новым узлом,
    а не со старым.

    Подсказка: создайте лист ``type(node)(name=name)`` и вызовите
    ``node.with_child(child)`` — связь ``parent`` ставит сам ``with_child``.
    """
    raise NotImplementedError
