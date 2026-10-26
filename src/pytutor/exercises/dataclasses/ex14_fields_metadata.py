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

Ловушка заданий: поле ``name`` имеет ``metadata``, но **не** имеет дефолта —
``field(metadata=...)`` дефолт не создаёт. Поэтому ``fields_without_default()``
вернёт именно ``["name"]``.
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

    ``cls("id")`` даёт ``name == "id"``, ``kind == "text"``, ``size == 0``.
    ``field(metadata=...)`` без ``default`` оставляет поле обязательным.

    Подсказка: не добавляйте ``name`` дефолт — иначе тест на
    ``fields_without_default`` не пройдёт.
    """
    raise NotImplementedError


def field_names() -> list[str]:
    """Вернуть имена полей ``Column``.

    Ожидаемый результат — ``["name", "kind", "size"]``.

    Подсказка: ``[item.name for item in fields(cls)]``.
    """
    raise NotImplementedError


def primary_key_names() -> list[str]:
    """Вернуть имена полей, у которых ``metadata["primary_key"]`` истинно.

    Ожидаемый результат — ``["name"]``.

    Подсказка: ``item.metadata.get("primary_key")`` — ``.get``, а не
    ``[...]``, потому что у большинства полей такого ключа нет.

    Обратите внимание: ``metadata["primary_key"]`` есть только у ``name``;
    у ``kind`` ключ другой (``nullable``), у ``size`` метаданных нет вовсе.
    """
    raise NotImplementedError


def fields_without_default() -> list[str]:
    """Вернуть имена полей без значения по умолчанию и без фабрики.

    Ожидаемый результат — ``["name"]``: у ``kind`` есть ``default="text"``, у
    ``size`` — ``0``.

    Подсказка: отсутствие и дефолта, и фабрики — это
    ``item.default is MISSING and item.default_factory is MISSING``; проверять
    только ``default`` недостаточно (поле с фабрикой тоже «без дефолта»).
    """
    raise NotImplementedError


def metadata_is_read_only() -> bool:
    """Вернуть ``True``, если ``metadata`` поля нельзя изменить.

    Ожидаемое значение — ``True``: ``metadata`` — это
    ``types.MappingProxyType``, запись в него бросает ``TypeError``.

    Подсказка: возьмите ``fields(cls)[0].metadata`` и попробуйте присвоить
    ``metadata["primary_key"] = False`` внутри ``try/except TypeError``.
    """
    raise NotImplementedError
