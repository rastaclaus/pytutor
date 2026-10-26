"""Упражнение 8. Вложенные ``defaultdict`` — автосоздание уровней. Уровень 4.

``defaultdict`` можно вкладывать друг в друга: ``defaultdict(lambda:
defaultdict(list))`` создаёт двухуровневую структуру, где каждый отсутствующий
ключ первого уровня автоматически порождает ``defaultdict(list)`` второго.

Это удобно для деревьев каталогов, «толстых» таблиц и любых структур, где
пути/ключи заранее неизвестны.

Важно помнить: автосоздание — это палка о двух концах.

* Чтение ``tree[key]`` **создаёт** пустой узел, поэтому проверять наличие нужно
  через ``key in tree``, иначе «проверка» изменит дерево.
* Функция ``get_path`` обязана не создавать узлы — иначе она не сможет вернуть
  ``default``.
* Фабрика — ``lambda``, а не ``defaultdict``: фабрикой может быть любой
  вызываемый объект без аргументов, а сам класс ``defaultdict`` ждёт первый
  аргумент-фабрику.

Термины, на которые ссылаются условия:

* **путь** — список ключей от корня до листа, например ``["a", "x"]``;
* **лист** — узел, в котором лежит список значений, а не вложенный словарь.
"""

from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def nested_defaultdict() -> defaultdict:
    """Создать двухуровневый ``defaultdict``.

    ``tree = nested_defaultdict()``: ``tree["a"]["x"].append(1)`` не бросает
    ``KeyError``, а после этого ``tree["a"]["x"] == [1]``;
    ``isinstance(tree, defaultdict)`` -> ``True``;
    ``isinstance(tree["b"], defaultdict)`` -> ``True`` — второй уровень тоже
    ``defaultdict``.

    Подсказка: ``defaultdict(lambda: defaultdict(list))``. Именно ``lambda``:
    передать ``defaultdict(list)`` как фабрику нельзя — его вызовут без
    аргументов и он бросит ``TypeError``.
    """
    raise NotImplementedError


def add_path(tree: defaultdict, path: list[str], value: int) -> defaultdict:
    """Добавить ``value`` в дерево по пути ``path``.

    ``path`` — список ключей; по каждому ключу (кроме последнего) создаётся
    вложенный узел. Последний ключ получает ``value`` в свой список.

    ``tree = nested_defaultdict()``: ``add_path(tree, ["a", "x"], 1)`` даёт
    ``{"a": {"x": [1]}}``;
    повторный ``add_path(tree, ["a", "x"], 2)`` — ``[1, 2]``;
    одноэлементный путь ``add_path(tree, ["b"], 3)`` даёт ``{"b": [3]}`` —
    ``value`` лежит прямо у корня;
    дерево возвращается тем же объектом (``is tree``).

    Порядок ключей в результате — порядок первого появления пути.

    Подсказка: пройдите по ``path[:-1]``, спускаясь ``node = node[key]`` (это
    как раз автосоздание), затем ``node[path[-1]] = ...``. Внимание: на
    последнем шаге значение — список, а не ``defaultdict``; ``node[last]`` без
    подготовки создал бы вложенный ``defaultdict``.
    """
    raise NotImplementedError


def get_path(tree: defaultdict, path: list[str], default: int | None = None) -> list[int] | None:
    """Вернуть список значений по пути ``path``.

    Если какого-то ключа в пути нет — вернуть ``default``. Не создавать
    отсутствующие узлы.

    ``tree`` после ``add_path(tree, ["a", "x"], 1)``:
    ``get_path(tree, ["a", "x"])`` -> ``[1]``;
    ``get_path(tree, ["a", "y"])`` -> ``None`` — такого листа нет;
    ``get_path(tree, ["z"])`` -> ``None``;
    ``get_path(tree, ["a", "x"], [])`` -> ``[1]`` — ``default`` вернулся бы
    только при промахе;
    после всех вызовов ``"z" not in tree`` — чтение ничего не создало.

    Подсказка: на каждом шаге проверяйте ``if key not in node: return default``.
    ``node[key]`` использовать нельзя: ``defaultdict`` создаст узел вместо того,
    чтобы сообщить об отсутствии.
    """
    raise NotImplementedError


def build_counts(words: Iterable[str]) -> defaultdict:
    """Построить ``defaultdict``: длина слова -> ``Counter`` букв слова.

    ``build_counts(["ab", "abc"])`` -> ``{2: Counter(a=1, b=1), 3: Counter(a=1,
    b=1, c=1)}``;
    ``build_counts([])`` -> пустой ``defaultdict``;
    ``build_counts(["ab", "ab"])`` -> ``{2: Counter(a=2, b=2)}`` — счётчики
    накапливаются по всем словам одной длины.

    Второй уровень — ``Counter``, а не список и не ``dict``: тест сравнивает с
    ``Counter(a=1, b=1)``.

    Подсказка: ``defaultdict(Counter)`` (фабрика — сам класс ``Counter``,
    который без аргументов даёт пустой счётчик) и ``+= 1`` по каждой букве.
    Вложенный ``Counter`` можно получить и через ``Counter(word)``, но тогда
    повторное слово перезапишет счётчик, а не сложит.
    """
    raise NotImplementedError


def merge_trees(left: defaultdict, right: defaultdict) -> defaultdict:
    """Слить два вложенных ``defaultdict``.

    Для каждой длины слова списки значений объединяются (порядок: сначала все из
    ``left``, потом все из ``right``). Вернуть новое дерево.

    ``left`` с ``["a", "x"] -> [1]`` и ``right`` с ``["a", "x"] -> [2, 3]``:
    ``merge_trees(left, right)["a"]["x"]`` -> ``[1, 2, 3]``;
    ключ, который есть только в ``right``, попадает в результат как есть;
    ключ, который есть только в ``left``, тоже сохраняется;
    исходные деревья не меняются, результат — новый ``defaultdict``.

    Подсказка: обойдите объединение ключей (``set(left) | set(right)``) и для
    каждого решите: оба значения — словари (рекурсия) или списки (конкатенация).
    Осторожно с формой дерева: у корня значения бывают и ``dict``, и ``list``.
    Проверять надо именно ``isinstance(value, dict)``, а не ``defaultdict``:
    обычный ``dict`` тоже подходит.
    """
    raise NotImplementedError
