"""Упражнение 3. ``collections.defaultdict`` — группировка. Уровень 2.

``defaultdict`` — словарь, который для отсутствующего ключа сам вызывает фабрику
и создаёт значение по умолчанию. Это убирает типичный шаблон
``if key not in d: d[key] = []``.

Две детали, которые ловят на практике:

* фабрика вызывается и при **чтении** отсутствующего ключа, поэтому
  ``d[missing]`` не бросает ``KeyError``, а создаёт запись;
* у ``defaultdict`` есть ``__missing__``, и простое приведение ``dict(d)``
  сохраняет уже созданные ключи. Проверять наличие лучше через ``in``, а не
  через ``d[key]``.

Самый частый сценарий — группировка: ``defaultdict(list)`` собирает элементы по
ключам, ``defaultdict(set)`` — уникальные значения.

Все функции возвращают обычный ``dict`` (или ``defaultdict``, но тесты
сравнивают с литералом словаря): результат не должен вести себя как
``defaultdict`` после возврата.

Термины, на которые ссылаются условия:

* **порядок появления** — порядок первого вхождения ключа при обходе входа;
* **порядок внутри группы** — порядок исходных элементов.
"""

from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def group_by_key(pairs: Iterable[tuple[str, int]]) -> dict[str, list[int]]:
    """Сгруппировать пары ``(ключ, значение)`` по ключу.

    ``group_by_key([("a", 1), ("b", 2), ("a", 3)])`` ->
    ``{"a": [1, 3], "b": [2]}``;
    ``group_by_key([])`` -> ``{}``;
    ``group_by_key([("z", 0)])`` -> ``{"z": [0]}`` — ноль не отбрасывается.

    Порядок ключей — по первому появлению, порядок значений внутри группы —
    исходный.

    Подсказка: ``defaultdict(list)`` + ``result[key].append(value)``; в конце
    ``dict(result)``, иначе вернётся ``defaultdict``.
    """
    raise NotImplementedError


def group_unique(pairs: Iterable[tuple[str, int]]) -> dict[str, set[int]]:
    """Сгруппировать пары по ключу, сохраняя уникальные значения.

    ``group_unique([("a", 1), ("a", 1), ("a", 2)])`` -> ``{"a": {1, 2}}`` —
    повтор ``1`` не создаёт дубликат;
    ``group_unique([("a", 1), ("b", 1)])`` -> ``{"a": {1}, "b": {1}}``;
    ``group_unique([])`` -> ``{}``.

    Подсказка: ``defaultdict(set)`` + ``add``. Порядок внутри множества не
    определён, но тест сравнивает множества, а не списки.
    """
    raise NotImplementedError


def index_by_field(records: Iterable[tuple[str, str]], field: int) -> dict[str, list[tuple[str, str]]]:
    """Сгруппировать записи по значению поля с индексом ``field``.

    ``index_by_field([("a", "x"), ("b", "y"), ("c", "x")], 1)`` ->
    ``{"x": [("a", "x"), ("c", "x")], "y": [("b", "y")]}`` — ключом стал второй
    элемент, а в группе лежат целые записи;
    ``index_by_field(records, 0)`` -> ключи ``"a"``, ``"b"``, ``"c"``, у каждого
    одна запись;
    ``index_by_field([], 0)`` -> ``{}``.

    ``field`` — индекс в кортеже, а не имя. Выход за границы кортежа даст
    ``IndexError`` от самого Python — перехватывать не нужно.

    Подсказка: ``record[field]`` как ключ, ``record`` целиком — в список.
    """
    raise NotImplementedError


def invert_mapping(mapping: dict[str, int]) -> dict[int, list[str]]:
    """Инвертировать словарь: значения -> список ключей.

    ``invert_mapping({"a": 1, "b": 2, "c": 1})`` ->
    ``{1: ["a", "c"], 2: ["b"]}``;
    ``invert_mapping({})`` -> ``{}``;
    ``invert_mapping({"x": 0})`` -> ``{0: ["x"]}`` — ноль остаётся значением
    ключа.

    Порядок ключей в списках — как в исходном словаре. Одинаковые значения не
    теряются: именно для этого нужен список, а не обратный ``dict``.

    Подсказка: ``defaultdict(list)`` по ``mapping.items()``.
    """
    raise NotImplementedError


def group_by_first_letter(words: Iterable[str]) -> dict[str, list[str]]:
    """Сгруппировать слова по первой букве.

    ``group_by_first_letter(["apple", "avocado", "banana"])`` ->
    ``{"a": ["apple", "avocado"], "b": ["banana"]}``;
    ``group_by_first_letter(["", "x"])`` -> ``{"x": ["x"]}`` — пустое слово
    пропускается, иначе ``word[0]`` бросил бы ``IndexError``;
    ``group_by_first_letter([])`` -> ``{}``.

    Порядок групп и элементов внутри — порядок появления; сортировать ничего
    не нужно.

    Регистр не нормализуется: ``"Apple"`` и ``"apple"`` попадут в разные группы
    (``"A"`` и ``"a"``).

    Подсказка: проверка ``if word:`` до обращения к ``word[0]``.
    """
    raise NotImplementedError
