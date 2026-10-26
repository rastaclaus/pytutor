"""Упражнение 6. ``collections.ChainMap`` — слои конфигурации. Уровень 3.

``ChainMap`` объединяет несколько словарей в один «вид» без их копирования.
Поиск ключа идёт слева направо: значение берётся из первого словаря, где ключ
встретился. Это классика для конфигурации: дефолты < пользовательские настройки
< переменные окружения.

Три правила, которые проверяют тесты:

* порядок аргументов — это порядок приоритета: ``ChainMap(user, defaults)``
  означает «``user`` важнее»;
* мутации (``cm[key] = value``, ``del cm[key]``) меняют **только первый**
  словарь, и это видно снаружи, потому что слои не копируются;
* ``new_child(m)`` возвращает **новый** ``ChainMap`` со слоем ``m`` сверху,
  ``parents`` — вид без верхнего слоя. Исходный объект не меняется.

Термины, на которые ссылаются условия:

* **верхний (приоритетный) слой** — ``cm.maps[0]``;
* **плоский словарь** — обычный ``dict`` со всеми ключами, где конфликт решён
  в пользу верхнего слоя.
"""

from __future__ import annotations

from collections import ChainMap


def make_chain(defaults: dict[str, int], user: dict[str, int]) -> ChainMap[str, int]:
    """Создать ``ChainMap``, где ``user`` имеет приоритет над ``defaults``.

    ``make_chain({"a": 1}, {"a": 2, "b": 3})["a"]`` -> ``2``;
    ``make_chain({"a": 1}, {})["a"]`` -> ``1`` — пользовательских настроек нет,
    работает дефолт;
    ``isinstance(make_chain({}, {}), ChainMap)`` -> ``True``.

    Подсказка: ``ChainMap(user, defaults)`` — именно в этом порядке. Если
    перепутать, приоритет станет обратным, и тест это поймает.
    """
    raise NotImplementedError


def lookup_priority(cm: ChainMap[str, int], key: str) -> int | None:
    """Вернуть значение ключа с учётом приоритета слоёв.

    ``cm = make_chain({"a": 1, "b": 2}, {"b": 3})``:
    ``lookup_priority(cm, "a")`` -> ``1`` (только в дефолтах);
    ``lookup_priority(cm, "b")`` -> ``3`` (пользовательский слой важнее);
    ``lookup_priority(cm, "c")`` -> ``None`` — ключа нет ни в одном слое.

    Важно: отсутствующий ключ не должен добавляться в словари, поэтому
    ``cm[key]`` с ``try/except`` хуже, чем ``get``.

    Подсказка: ``cm.get(key)`` уже реализует поиск по слоям и не мутирует
    ничего.
    """
    raise NotImplementedError


def flatten_layers(cm: ChainMap[str, int]) -> dict[str, int]:
    """Слить все слои в один словарь.

    Ключи, которые есть в нескольких слоях, берутся из более приоритетного
    (первого) слоя.

    ``flatten_layers(ChainMap({"a": 1}, {"a": 2, "b": 3}))`` ->
    ``{"a": 1, "b": 3}``;
    ``flatten_layers(ChainMap())`` -> ``{}``;
    ``flatten_layers(ChainMap({"x": 0}, {"y": 1}))`` ->
    ``{"x": 0, "y": 1}``.

    Результат — обычный ``dict``, а не ``ChainMap``, и он не связан со слоями:
    его изменение не затронет исходные словари.

    Подсказка: ``dict(cm)``. ``ChainMap`` сам является ``Mapping``, поэтому
    конструктор ``dict`` обойдёт ключи с учётом приоритета.
    """
    raise NotImplementedError


def insert_layer(cm: ChainMap[str, int], updates: dict[str, int]) -> ChainMap[str, int]:
    """Вернуть новый ``ChainMap`` со слоем ``updates`` поверх ``cm``.

    ``cm = make_chain({"a": 1}, {"b": 2})``:
    ``insert_layer(cm, {"a": 10})["a"]`` -> ``10``;
    ``cm["a"]`` по-прежнему ``1`` — исходный ``ChainMap`` не изменился;
    ``isinstance(insert_layer(cm, {}), ChainMap)`` -> ``True``.

    Подсказка: ``cm.new_child(updates)``. ``updates`` становится первым
    элементом ``maps`` и разделяет хранилище с результатом — копирования нет.
    """
    raise NotImplementedError


def drop_first_layer(cm: ChainMap[str, int]) -> ChainMap[str, int]:
    """Вернуть ``ChainMap`` без верхнего слоя.

    ``cm = ChainMap({"a": 1}, {"a": 2, "b": 3})``:
    ``parents = drop_first_layer(cm)``: ``parents["a"]`` -> ``2``;
    ``"b" in parents`` -> ``True``;
    ``parents["b"]`` -> ``3`` — второй слой стал первым.

    Если слой один, результат — пустой ``ChainMap``.

    Подсказка: ``cm.parents``. Это не копия, а новый ``ChainMap`` над теми же
    нижележащими словарями.
    """
    raise NotImplementedError


def write_through(cm: ChainMap[str, int], key: str, value: int) -> ChainMap[str, int]:
    """Записать ``key=value`` в первый (самый приоритетный) слой ``cm``.

    Мутация должна затронуть верхний словарь, а не нижележащие. Вернуть ``cm``.

    ``user = {"a": 1}``, ``defaults = {"a": 2, "b": 3}``,
    ``cm = ChainMap(user, defaults)``: после ``write_through(cm, "a", 99)``
    результат ``is cm``, ``cm["a"] == 99``, ``user["a"] == 99``, а
    ``defaults["a"]`` остаётся ``2``.

    Если ключа не было ни в одном слое, он появится в верхнем.

    Подсказка: ``cm[key] = value`` и ``return cm``. ``ChainMap`` не даёт
    записывать «во все слои» — это отдельная задача в упражнении 14.
    """
    raise NotImplementedError
