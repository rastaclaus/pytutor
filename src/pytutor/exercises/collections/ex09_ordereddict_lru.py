"""Упражнение 9. ``OrderedDict`` и LRU-кэш. Уровень 4.

``OrderedDict`` — словарь, который помнит порядок вставки ключей и даёт два
метода, которых нет у обычного ``dict``:

* ``move_to_end(key, last=True)`` — переместить ключ в конец (или в начало при
  ``last=False``);
* ``popitem(last=True)`` — забрать крайний элемент: последний или (при
  ``last=False``) первый.

Этого достаточно, чтобы собрать классический LRU-кэш (Least Recently Used):
при каждом обращении ключ «освежается» в конце, а при переполнении вытесняется
ключ из начала.

Обратите внимание: с Python 3.7 обычный ``dict`` тоже сохраняет порядок
вставки, но ``OrderedDict`` даёт ``move_to_end`` и ``popitem(last=)``.

Три политики, которые легко перепутать:

* **LRU** — ``get`` освежает ключ (переставляет в конец);
* **FIFO** — ``get`` порядок **не** меняет, вытесняется самый старый по
  вставке;
* **обновление существующего ключа** в LRU тоже считается обращением и
  освежает ключ.

Тексты ошибок: для неположительной ёмкости нужно ``ValueError`` со словом
``capacity`` (например, ``"capacity должно быть >= 1"``).
"""

from __future__ import annotations

from collections import OrderedDict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


class LRUCache:
    """Кэш ограниченного размера: вытесняет наименее недавно использованный ключ.

    Реализуйте через ``OrderedDict`` и ``move_to_end``.
    """

    def __init__(self, capacity: int) -> None:
        """Создать кэш на ``capacity`` элементов (``capacity >= 1``).

        ``LRUCache(0)`` и ``LRUCache(-1)`` -> ``ValueError`` (в сообщении есть
        ``capacity``);
        ``len(LRUCache(3)) == 0`` — новый кэш пуст.

        Подсказка: проверку делайте **до** создания хранилища, иначе получится
        объект, который сразу же не сможет ничего принять.
        """
        raise NotImplementedError

    def get(self, key: str) -> int | None:
        """Вернуть значение по ключу, освежив его (или ``None``).

        после ``put("a", 1)``: ``get("a")`` -> ``1``, и ключ ``"a"`` теперь
        последний в порядке вытеснения;
        ``get("missing")`` -> ``None`` — отсутствие ключа не ошибка и не меняет
        порядок;
        повторный ``get`` не меняет значение, только порядок.

        Подсказка: сначала проверьте наличие (``key in self._data``), затем
        ``move_to_end(key)`` и верните значение. Если сначала взять
        ``self._data[key]``, промах даст ``KeyError``.
        """
        raise NotImplementedError

    def put(self, key: str, value: int) -> None:
        """Записать пару; при переполнении вытеснить самого старого.

        ``cache = LRUCache(2)``: после ``put("a", 1)``, ``put("b", 2)``,
        ``get("a")`` и ``put("c", 3)`` вытесняется ``b``, а ``a`` остаётся;
        ``put`` для существующего ключа обновляет значение и освежает ключ;
        после переполнения ``len(cache) == capacity``.

        Подсказка: для существующего ключа сделайте ``move_to_end``, затем
        присвойте значение и, если ``len(self._data) > self.capacity``,
        вызовите ``popitem(last=False)``.
        """
        raise NotImplementedError

    def __len__(self) -> int:
        """Число записей в кэше.

        ``len(LRUCache(3))`` -> ``0``;
        после трёх ``put`` при ёмкости 3 -> ``3``;
        после четырёх ``put`` при ёмкости 3 -> ``3`` — ёмкость не превышается.

        Подсказка: ``len(self._data)``.
        """
        raise NotImplementedError


def fifo_cache(items: Iterable[tuple[str, int]], capacity: int) -> list[tuple[str, int]]:
    """Пропустить ``items`` через FIFO-кэш и вернуть вытесненные пары.

    Вытеснение идёт в порядке вставки (первый пришёл — первый ушёл). Вернуть
    список вытесненных пар по мере их вытеснения.

    ``fifo_cache([("a", 1), ("b", 2), ("c", 3), ("d", 4)], 2)`` ->
    ``[("a", 1), ("b", 2)]``;
    ``fifo_cache([("a", 1)], 5)`` -> ``[]`` — кэш не переполнялся;
    ``fifo_cache([], 2)`` -> ``[]``;
    повторная пара с тем же ключом не вытесняет ничего, а обновляет значение;
    ``fifo_cache([], 0)`` -> ``ValueError`` (в сообщении есть ``capacity``).

    Подсказка: OrderedDict + ``popitem(last=False)``, когда ``len(cache) >=
    capacity`` и ключа ещё нет. Порядок вытеснения — это порядок появления в
    возвращаемом списке.
    """
    raise NotImplementedError


def touch(cache: OrderedDict[str, int], key: str) -> OrderedDict[str, int]:
    """Переместить ``key`` в конец ``cache`` (освежить).

    ``cache = OrderedDict([("a", 1), ("b", 2), ("c", 3)])``: после
    ``touch(cache, "a")`` результат ``is cache`` и ``list(cache) == ["b", "c",
    "a"]``;
    ``touch(cache, "zzz")`` не добавляет ключ и не бросает исключение;
    пустой кэш остаётся пустым.

    Подсказка: ``if key in cache: cache.move_to_end(key)`` + ``return cache``.
    ``move_to_end`` на отсутствующем ключе бросил бы ``KeyError``.
    """
    raise NotImplementedError


def oldest_key(cache: OrderedDict[str, int]) -> str | None:
    """Вернуть ключ, вставленный раньше всех (или ``None`` для пустого).

    ``oldest_key(OrderedDict([("a", 1), ("b", 2)]))`` -> ``"a"``;
    ``oldest_key(OrderedDict())`` -> ``None``;
    после ``touch(cache, "a")`` самый старый — уже ``"b"``.

    Подсказка: ``next(iter(cache), None)`` — итерация по ``OrderedDict`` идёт в
    порядке вставки. ``cache.popitem`` использовать нельзя: функция не должна
    менять кэш.
    """
    raise NotImplementedError
