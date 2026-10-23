"""Упражнение 5. ``__post_init__`` и вычисляемые поля. Уровень 3.

Сгенерированный ``__init__`` в конце вызывает ``self.__post_init__()``, если метод
определён. Это место для нормализации и проверки полей, а также для вычисления
значений, которых нет в аргументах ``__init__``.

Чтобы поле не попадало в ``__init__``, объявите его с ``field(init=False)``: у
него может быть ``default``/``default_factory``, но его всё равно нужно
пересчитать в ``__post_init__``, если значение зависит от других полей.

Если метод ``__init__`` не генерируется (``init=False`` у декоратора или свой
``__init__``), ``__post_init__`` автоматически не вызывается.
"""

from __future__ import annotations

from dataclasses import dataclass, field


def declare_rectangle() -> type:
    """Создать dataclass ``Rectangle``.

    Поля:

    * ``width: float``;
    * ``height: float``;
    * ``area: float = field(init=False)`` — считается в ``__post_init__``
      как ``width * height``.

    В ``__post_init__`` также проверяйте, что ``width`` и ``height``
    положительны, иначе бросайте ``ValueError`` с текстом про "положительн".
    """
    raise NotImplementedError


def make_rectangle(width: float, height: float) -> object:
    """Создать ``Rectangle`` с заданными сторонами."""
    raise NotImplementedError


def has_area_argument() -> bool:
    """Вернуть ``True``, если ``area`` НЕ является параметром ``__init__``."""
    raise NotImplementedError
