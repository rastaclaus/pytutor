"""Упражнение 17. Поля-дескрипторы. Уровень 7.

Если значение по умолчанию у поля — объект-дескриптор (у него есть ``__set__``
или ``__get__``), dataclass ведёт себя иначе:

* в ``__init__`` присваивание идёт через ``descriptor.__set__(obj, value)``;
* чтение поля тоже идёт через ``__get__``;
* чтобы понять, есть ли у поля дефолт, dataclass вызывает
  ``descriptor.__get__(None, cls)``; если тот бросит ``AttributeError`` — дефолта
  нет.

Это способ добавить валидацию или приведение типа прямо в поле, не переопределяя
``__setattr__``.

Реализуйте дескриптор, приводящий значение к ``int`` и проверяющий границы.

Важно про ``__set__``: значение нужно складывать не в ``obj.<name>``, а в
отдельный атрибут (например ``obj._quantity``). Иначе присваивание снова
попадёт в дескриптор и получится бесконечная рекурсия. Кроме того, при
``__get__`` с ``obj is None`` (доступ через класс) возвращается ``default`` —
именно так dataclass узнаёт значение по умолчанию.
"""

from __future__ import annotations

from typing import Any


class IntField:
    """Дескриптор целочисленного поля с проверкой диапазона.

    * ``__set_name__(owner, name)`` — запомните имя атрибута в экземпляре;
    * ``__get__(obj, objtype)`` — если ``obj is None``, верните ``default``
      (это нужно dataclass, чтобы найти дефолт); иначе верните значение;
    * ``__set__(obj, value)`` — приведите к ``int`` и проверьте границы
      ``0 <= value <= max_value``; иначе ``ValueError`` с текстом "диапазон".
    """

    def __init__(self, *, default: int = 0, max_value: int = 100) -> None:
        """Запомнить дефолт и верхнюю границу.

        ``IntField(default=1)`` -> ``default == 1``, ``max_value == 100``;
        ``IntField(max_value=5)`` -> ``default == 0``.

        Подсказка: заведите ещё и пустое ``self.name`` — его заполнит
        ``__set_name__``.
        """
        raise NotImplementedError

    def __set_name__(self, owner: type, name: str) -> None:
        """Запомнить имя поля.

        ``quantity`` -> сохраняется как ``"_quantity"``: под этим именем
        значение лежит в ``__dict__`` экземпляра.

        Подсказка: ``self.name = f"_{name}"`` — ведущее подчёркивание
        обязательно, иначе ``setattr`` снова вызовет ``__set__``.
        """
        raise NotImplementedError

    def __get__(self, obj: Any, objtype: type | None = None) -> int:
        """Вернуть значение или дефолт при доступе через класс.

        ``Item.quantity`` (через класс) -> ``1``, то есть ``default``;
        ``Item(quantity=5).quantity`` -> ``5``;
        у только что созданного объекта без значения — ``default``.

        Подсказка: ``if obj is None: return self.default``, иначе
        ``getattr(obj, self.name, self.default)``.
        """
        raise NotImplementedError

    def __set__(self, obj: Any, value: Any) -> None:
        """Привести к ``int`` и проверить диапазон.

        ``obj.quantity = "42"`` -> дальше читается ``42``;
        ``obj.quantity = 0`` и ``obj.quantity = 100`` допустимы (границы
        включительные);
        ``obj.quantity = 101`` и ``obj.quantity = -1`` -> ``ValueError``
        (в сообщении есть ``диапазон``);
        ``obj.quantity = "abc"`` -> ``ValueError`` от ``int()``.

        Подсказка: ``int(value)`` сам бросит ``ValueError`` на нечисловой
        строке — перехватывать не надо. Записывайте результат через
        ``setattr(obj, self.name, number)``.
        """
        raise NotImplementedError


def declare_item() -> type:
    """Создать dataclass ``Item`` с полем ``quantity: int = IntField(default=1)``.

    ``declare_item()()`` (без аргументов) даёт ``quantity == 1``;
    ``declare_item()(quantity="7").quantity == 7``.

    Подсказка: дескриптор — это значение по умолчанию поля; аннотация остаётся
    ``int`` (проверку типов можно заглушить ``# type: ignore[assignment]``).
    """
    raise NotImplementedError


def make_item(quantity: object) -> object:
    """Создать ``Item`` из произвольного значения (дескриптор приведёт к int).

    ``make_item("7").quantity == 7`` и это ``int``;
    ``make_item(0).quantity == 0`` и ``make_item(100).quantity == 100`` —
    границы включительные;
    ``make_item(-1)``, ``make_item(101)``, ``make_item("abc")`` -> ``ValueError``.

    Подсказка: передавайте значение по имени (``quantity=quantity``), чтобы не
    зависеть от позиционного порядка полей.
    """
    raise NotImplementedError
