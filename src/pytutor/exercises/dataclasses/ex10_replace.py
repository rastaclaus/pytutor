"""Упражнение 10. Копирование с изменениями: ``dataclasses.replace``. Уровень 4.

``replace(obj, **changes)`` создаёт **новый** объект того же класса, вызывая
``__init__`` с изменёнными полями. Следствия:

* ``__post_init__`` выполняется заново — вычисляемые поля пересчитываются;
* ``changes`` принимает только поля, у которых ``init=True``; иначе
  ``ValueError``;
* неизвестное имя поля → ``TypeError``;
* ``InitVar`` без дефолта нужно передавать явно;
* для замороженных объектов ``replace`` — основной способ «изменить» значение.

Тексты ошибок принадлежат stdlib: ``TypeError`` для неизвестного имени поля
(``unexpected keyword argument``) и ``ValueError`` для поля с ``init=False``.
Переупаковывать их не нужно.
"""

from __future__ import annotations

from dataclasses import dataclass


def declare_settings() -> type:
    """Создать ``@dataclass(frozen=True)`` класс ``Settings``.

    Поля:

    * ``host: str``;
    * ``port: int``;
    * ``debug: bool = False``.

    ``cls("localhost", 80)`` даёт ``debug == False``;
    присваивание ``settings.debug = True`` -> ``FrozenInstanceError``
    (в сообщении есть ``cannot assign to field``).

    Подсказка: ``frozen=True`` нужен, чтобы «изменение» шло только через
    ``replace``.
    """
    raise NotImplementedError


def with_debug(settings: object, debug: bool) -> object:  # noqa: FBT001
    """Вернуть копию ``settings`` с другим ``debug`` (исходный не менять).

    ``changed = with_debug(cls("localhost", 80), True)``:
    ``changed is not original``, ``changed.debug is True``,
    ``original.debug is False``;
    ``type(changed) is type(original)`` — ``replace`` сохраняет класс;
    остальные поля (``host``, ``port``) копируются без изменений.

    Подсказка: ``replace(settings, debug=debug)``.
    """
    raise NotImplementedError


def changed_fields() -> list[str]:
    """Вернуть имена полей ``Settings``, которые можно менять через ``replace``.

    Ожидаемый результат — ``["host", "port", "debug"]`` в порядке объявления.

    Подсказка: отфильтруйте ``fields(cls)`` по ``item.init``; это важно, если
    позже появится поле с ``init=False`` — оно в список не попадёт.
    """
    raise NotImplementedError


def replace_unknown_field_fails() -> bool:
    """Проверить, что ``replace`` с несуществующим полем бросает ``TypeError``.

    Создайте ``Settings("localhost", 80)`` и вызовите
    ``replace(settings, unknown=1)``. Поймали ``TypeError`` — вернуть ``True``.

    Важно: ``TypeError``, а не ``ValueError`` — ``replace`` просто передаёт
    лишний именованный аргумент в ``__init__``.

    Подсказка: ``try/except TypeError``.
    """
    raise NotImplementedError
