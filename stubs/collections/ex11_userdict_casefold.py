"""Упражнение 11. ``UserDict`` — свой словарь с другой семантикой. Уровень 5.

``UserDict`` — класс-обёртка над обычным словарём. В отличие от наследования от
``dict``, он не переопределяет внутренний ``dict`` и потому безопаснее для
создания «своих» словарей: вы контролируете ``__getitem__``/``__setitem__``/
``__delitem__``, а всё остальное (``in``, ``len``, ``get``, ``items``) строится
поверх них.

Классический пример — словарь с регистронезависимыми ключами: все ключи
нормализуются через ``str.casefold()``.
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
        """Вернуть значение по ключу без учёта регистра."""
        raise NotImplementedError

    def __setitem__(self, key: str, value: int) -> None:
        """Записать значение, нормализовав ключ."""
        raise NotImplementedError

    def __delitem__(self, key: str) -> None:
        """Удалить ключ без учёта регистра."""
        raise NotImplementedError

    def __contains__(self, key: object) -> bool:
        """Проверить наличие ключа без учёта регистра."""
        raise NotImplementedError


def count_case_insensitive(words: Iterable[str]) -> dict[str, int]:
    """Посчитать слова без учёта регистра, вернув обычный словарь.

    Используйте ``CaseInsensitiveDict`` внутри. Ключи в результате — в исходном
    регистре первого вхождения.
    """
    raise NotImplementedError
