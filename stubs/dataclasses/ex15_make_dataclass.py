"""Упражнение 15. Динамические классы: ``make_dataclass``. Уровень 6.

``make_dataclass(name, fields, *, namespace=None, bases=(), **options)`` создаёт
dataclass во время выполнения. Элемент ``fields`` — одно из:

* ``"x"`` — имя без типа (тип станет ``typing.Any``);
* ``("x", int)`` — имя и тип;
* ``("x", int, field(default=5))`` — имя, тип и ``field()``.

Через ``namespace`` можно добавить методы. Опции (``frozen``, ``slots``,
``order``, ...) те же, что у ``@dataclass``.

Это удобно для схем «из данных»: форматы ответа API, таблицы из конфигурации,
тестовые фабрики.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable, Sequence


def build_point() -> type:
    """Создать ``make_dataclass("DynPoint", [("x", int), ("y", int)])``."""
    raise NotImplementedError


def build_record(names: Sequence[str]) -> type:
    """Создать dataclass ``DynRecord``, где каждое имя из ``names`` — поле ``Any``.

    Пустой ``names`` допустим: получится dataclass без полей.
    """
    raise NotImplementedError


def build_row(values: Iterable[tuple[str, type]]) -> type:
    """Создать dataclass ``DynRow`` из пар ``(имя, тип)``."""
    raise NotImplementedError


def add_method(instance: object) -> object:
    """Проверить, что через ``namespace`` можно добавить метод.

    Создайте dataclass с полем ``value: int`` и методом ``doubled()``,
    возвращающим ``value * 2``, и верните экземпляр этого класса со значением 21.
    """
    raise NotImplementedError
