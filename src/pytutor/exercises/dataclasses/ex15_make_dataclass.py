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

Порядок аргументов в ``fields`` — это порядок параметров ``__init__``, он же
порядок в ``fields(cls)``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable, Sequence


def build_point() -> type:
    """Создать ``make_dataclass("DynPoint", [("x", int), ("y", int)])``.

    ``cls.__name__ == "DynPoint"``;
    ``cls(1, 2)`` даёт ``(x, y) == (1, 2)``.

    Подсказка: одной строки ``make_dataclass(...)`` достаточно — возвращать
    нужно сам класс, а не экземпляр.
    """
    raise NotImplementedError


def build_record(names: Sequence[str]) -> type:
    """Создать dataclass ``DynRecord``, где каждое имя из ``names`` — поле ``Any``.

    Пустой ``names`` допустим: получится dataclass без полей.

    ``build_record(["a", "b"])(10, "x")`` даёт ``a == 10``, ``b == "x"``;
    ``[item.name for item in fields(cls)] == ["a", "b"]`` — порядок как в
    ``names``;
    ``fields(build_record([])) == ()`` и ``cls() == cls()``.

    Подсказка: ``[(name, Any) for name in names]``; ``Any`` импортируйте из
    ``typing``.
    """
    raise NotImplementedError


def build_row(values: Iterable[tuple[str, type]]) -> type:
    """Создать dataclass ``DynRow`` из пар ``(имя, тип)``.

    ``build_row([("age", int), ("name", str)])(30, "alice")`` даёт
    ``age == 30`` и ``name == "alice"``.

    Подсказка: ``make_dataclass`` принимает список пар как есть; ``Iterable``
    сначала материализуйте (``list(values)``).
    """
    raise NotImplementedError


def add_method(instance: object) -> object:
    """Проверить, что через ``namespace`` можно добавить метод.

    Создайте dataclass с полем ``value: int`` и методом ``doubled()``,
    возвращающим ``value * 2``, и верните экземпляр этого класса со значением 21.

    Ожидаемо: ``instance.value == 21`` и ``instance.doubled() == 42``.

    Аргумент ``instance`` не используется — он остался в сигнатуре ради
    единообразия; это нормально.

    Подсказка: ``namespace={"doubled": lambda self: self.value * 2}``. Метод
    должен принимать ``self`` первым аргументом, иначе он станет обычной
    функцией и ``instance.doubled()`` упадёт.
    """
    raise NotImplementedError
