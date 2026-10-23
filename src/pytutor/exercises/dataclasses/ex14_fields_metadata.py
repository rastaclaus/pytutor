"""Упражнение 14. Интроспекция: ``fields()``, ``Field``, ``metadata``. Уровень 6.

``dataclasses.fields(cls_or_obj)`` возвращает кортеж ``Field``. У каждого поля
есть:

* ``name``, ``type`` — имя и аннотация;
* ``default``, ``default_factory`` — значения по умолчанию (``MISSING``, если нет);
* ``init``, ``repr``, ``compare``, ``hash``, ``kw_only`` — флаги;
* ``metadata`` — **только для чтения** ``MappingProxyType``, свободное место для
  сторонних расширений;
* ``doc`` — необязательный докстринг поля (Python 3.14+).

``metadata`` dataclass сам не использует: это крючок для валидаторов и схем.
"""

from __future__ import annotations

from dataclasses import MISSING, dataclass, field


def declare_column() -> type:
    """Создать dataclass ``Column``.

    Поля:

    * ``name: str = field(metadata={"primary_key": True})``;
    * ``kind: str = field(default="text", metadata={"nullable": True})``;
    * ``size: int = 0``.

    Метаданные dataclass не интерпретирует — это просто ваш словарь.
    """
    raise NotImplementedError


def field_names() -> list[str]:
    """Вернуть имена полей ``Column``."""
    raise NotImplementedError


def primary_key_names() -> list[str]:
    """Вернуть имена полей, у которых ``metadata["primary_key"]`` истинно."""
    raise NotImplementedError


def fields_without_default() -> list[str]:
    """Вернуть имена полей без значения по умолчанию и без фабрики."""
    raise NotImplementedError


def metadata_is_read_only() -> bool:
    """Вернуть ``True``, если ``metadata`` поля нельзя изменить."""
    raise NotImplementedError
