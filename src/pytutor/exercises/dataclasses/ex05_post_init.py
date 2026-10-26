"""Упражнение 5. ``__post_init__`` и вычисляемые поля. Уровень 3.

Сгенерированный ``__init__`` в конце вызывает ``self.__post_init__()``, если метод
определён. Это место для нормализации и проверки полей, а также для вычисления
значений, которых нет в аргументах ``__init__``.

Чтобы поле не попадало в ``__init__``, объявите его с ``field(init=False)``: у
него может быть ``default``/``default_factory``, но его всё равно нужно
пересчитать в ``__post_init__``, если значение зависит от других полей.

Если метод ``__init__`` не генерируется (``init=False`` у декоратора или свой
``__init__``), ``__post_init__`` автоматически не вызывается.

Текст ошибки: при неположительных сторонах нужно ``ValueError``, в сообщении
которого есть подстрока ``положительн`` (например, «стороны должны быть
положительными»). Тест ищет именно её.
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

    Поведение:

    * ``cls(3, 4).area == 12``;
    * ``cls(2.5, 2).area == 5.0``;
    * ``cls(0, 1)``, ``cls(1, 0)``, ``cls(-1, 2)`` -> ``ValueError``
      (ноль тоже не положительное число);
    * ``cls(2, 3) == cls(2, 3)`` — ``area`` одинаково вычислен, поэтому равенство
      работает без доработок.

    Подсказка: внутри ``__post_init__`` сначала проверка, затем
    ``self.area = self.width * self.height``. Порядок важен: при ошибке
    ``area`` не должно остаться неинициализированным «наполовину».
    """
    raise NotImplementedError


def make_rectangle(width: float, height: float) -> object:
    """Создать ``Rectangle`` с заданными сторонами.

    ``make_rectangle(3, 4).area == 12``;
    ``make_rectangle(0, 1)`` -> ``ValueError`` (в сообщении есть
    ``положительн``).

    Подсказка: переиспользуйте ``declare_rectangle()``.
    """
    raise NotImplementedError


def has_area_argument() -> bool:
    """Вернуть ``True``, если ``area`` НЕ является параметром ``__init__``.

    Ожидаемое значение — ``True``: ``field(init=False)`` убирает ``area`` из
    параметров, но оставляет поле в ``fields()``.

    Подсказка: ``inspect.signature(cls.__init__).parameters`` и проверка
    ``"area" not in params``. Не путайте с ``fields(cls)`` — там ``area`` есть.
    """
    raise NotImplementedError
