"""Упражнение 11. ``UserDict`` — свой словарь с другой семантикой. Уровень 5.

``UserDict`` — класс-обёртка над обычным словарём. В отличие от наследования от
``dict``, он хранит данные не в самом объекте, а в атрибуте ``self.data`` и не
переопределяет внутренние быстрые пути ``dict``. Поэтому безопаснее создавать
«свои» словари через ``UserDict``: вы контролируете
``__getitem__``/``__setitem__``/``__delitem__``, а всё остальное (``in``,
``len``, ``get``, ``items``, ``update``) строится поверх них.

Классический пример — словарь с регистронезависимыми ключами: все ключи
нормализуются через ``str.casefold()``.

Почему ``casefold``, а не ``lower``: ``casefold`` агрессивнее и корректнее
сворачивает регистр, например ``"ß".casefold() == "ss"``. Для кириллицы
результат тот же, что у ``lower``.

Ловушки:

* ``__contains__`` получает **любой** объект, не только строку. Вызов
  ``key.casefold()`` на ``None`` бросит ``AttributeError``, поэтому тин нужно
  проверить. Тест проверяет ``None not in d``;
* ``UserDict`` ищет ключи через ваш ``__getitem__``, но в ``self.data`` лежат
  **нормализованные** ключи. Смешивать их нельзя.

Термины, на которые ссылаются условия:

* **нормализованный ключ** — результат ``casefold()``;
* **исходный регистр** — то написание, с которым слово встретилось первым.
"""

from __future__ import annotations

from collections import UserDict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


class CaseInsensitiveDict(UserDict[str, int]):
    """Словарь, где поиск/вставка/удаление не зависят от регистра ключа.

    Все ключи нормализуются через ``str.casefold()``. Реализуйте
    ``__getitem__``, ``__setitem__``, ``__delitem__``, ``__contains__`` —
    остальное возьмёт ``UserDict``.
    """

    def __getitem__(self, key: str) -> int:
        """Вернуть значение по ключу без учёта регистра.

        ``d["Hello"] = 1``: ``d["hello"]`` -> ``1`` и ``d["HELLO"]`` -> ``1``;
        ``d["ну"]`` -> ``KeyError`` — отсутствующий ключ ведёт себя как в
        обычном словаре.

        Подсказка: обратитесь к ``self.data`` напрямую с
        нормализованным ключом: ``self.data[key.casefold()]``. Вызов
        ``super().__getitem__`` снова попадёт в ваш же метод.
        """
        raise NotImplementedError

    def __setitem__(self, key: str, value: int) -> None:
        """Записать значение, нормализовав ключ.

        после ``d["Hello"] = 1`` и ``d["HELLO"] = 2`` ``len(d) == 1`` и
        ``d["hello"] == 2`` — разные написания одного ключа;
        ``d[123]`` -> ``AttributeError`` — не-строка не приводится к нижнему
        регистру, и это ожидаемо.

        Подсказка: ``self.data[key.casefold()] = value``.
        """
        raise NotImplementedError

    def __delitem__(self, key: str) -> None:
        """Удалить ключ без учёта регистра.

        ``d["Привет"] = 1``: после ``del d["ПРИВЕТ"]`` ключа нет ни в каком
        написании, ``len(d) == 0``;
        ``del d["нет такого"]`` -> ``KeyError``.

        Подсказка: ``del self.data[key.casefold()]`` — «сырой» ``del d[key]``
        ушёл бы в ``UserDict``, который для удаления тоже зовёт ваш метод.
        """
        raise NotImplementedError

    def __contains__(self, key: object) -> bool:
        """Проверить наличие ключа без учёта регистра.

        ``d["Привет"] = 1``: ``"привет" in d`` и ``"ПРИВЕТ" in d`` -> ``True``;
        ``None not in d`` -> ``True`` (то есть ``False`` для ``in``) —
        не-строка не роняет проверку;
        ``123 in d`` -> ``False``.

        Подсказка: ``isinstance(key, str) and key.casefold() in self.data``.
        Проверка типа обязательна: ``None.casefold()`` бросает
        ``AttributeError``, а не возвращает ``False``.
        """
        raise NotImplementedError


def count_case_insensitive(words: Iterable[str]) -> dict[str, int]:
    """Посчитать слова без учёта регистра, вернув обычный словарь.

    Используйте ``CaseInsensitiveDict`` внутри. Ключи в результате — в исходном
    регистре первого вхождения.

    ``count_case_insensitive(["Кот", "кот", "КОТ", "пёс"])`` ->
    ``{"Кот": 3, "пёс": 1}`` — ключом стало первое написание;
    ``count_case_insensitive([])`` -> ``{}``;
    ``count_case_insensitive(["a", "B", "b"])`` -> ``{"a": 1, "B": 2}``.

    Порядок ключей — по первому появлению.

    Подсказка: заведите ещё ``dict`` «нормализованный ключ -> исходное
    написание» и заполняйте его при первом появлении. Иначе возвращать
    придётся ``casefold``-версии, и тест не пройдёт.
    """
    raise NotImplementedError
