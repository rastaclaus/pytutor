"""Упражнение 15. Крайние случаи ``Counter``: мультимножество. Уровень 6.

``Counter`` — это мультимножество, и его крайние случаи часто ловят в реальном
коде:

* счётчики могут стать **отрицательными** после ``subtract``;
* ``elements()`` игнорирует ключи со счётчиком ``<= 0``;
* ``+`` отбрасывает неположительные итоги, а ``|`` — нет;
* после ``&``/``|`` нулевые ключи могут остаться.

Нужно уметь фильтровать и сравнивать мультимножества.

Базовое правило для всех функций набора: **положительный счётчик** — это
участие элемента, ноль и отрицательное значение — не участие. В отличие от
``Counter.__eq__``, которое сравнивает словари целиком и потому считает
``Counter(a=0)`` и ``Counter()`` разными, эти функции смотрят только на
положительные значения.

Термины, на которые ссылаются условия:

* **нормализованный счётчик** — без нулевых и отрицательных значений;
* **под-мультимножество** — каждый элемент ``left`` встречается в ``right`` не
  меньше раз;
* **симметрическая разность** — элементы, которых «не поровну», с модулем
  разности.
"""

from __future__ import annotations

from collections import Counter


def nonzero_items(counter: Counter[str]) -> Counter[str]:
    """Оставить только ключи с положительным счётчиком.

    ``nonzero_items(Counter(a=2, b=0, c=-1, d=3))`` -> ``Counter(a=2, d=3)``;
    ``nonzero_items(Counter())`` -> ``Counter()``;
    ``nonzero_items(Counter(x=-1))`` -> ``Counter()``.

    Порядок ключей сохраняется.

    Подсказка: словарное включение по ``counter.items()`` с условием
    ``count > 0`` внутри ``Counter(...)``. Фильтрация списка ключей и повторный
    подсчёт дали бы неверные значения — счётчики нужно переносить как есть.
    """
    raise NotImplementedError


def keys_with_positive_count(counter: Counter[str]) -> list[str]:
    """Список ключей со счётчиком больше нуля (порядок — как в ``counter``).

    ``keys_with_positive_count(Counter(a=2, b=0, c=-1, d=3))`` ->
    ``["a", "d"]``;
    ``keys_with_positive_count(Counter())`` -> ``[]``;
    ``keys_with_positive_count(Counter(x=-1, y=1))`` -> ``["y"]``.

    Подсказка: ``[key for key, count in counter.items() if count > 0]``. Это
    ровно ключи из ``nonzero_items``, но без счётчиков.
    """
    raise NotImplementedError


def is_submultiset(left: Counter[str], right: Counter[str]) -> bool:
    """Проверить, что ``left`` — под-мультимножество ``right``.

    Каждый ключ из ``left`` должен иметь счётчик не больше, чем в ``right``
    (отрицательные счётчики в ``left`` игнорируются).

    ``is_submultiset(Counter(a=2), Counter(a=3, b=1))`` -> ``True``;
    ``is_submultiset(Counter(a=4), Counter(a=3))`` -> ``False``;
    ``is_submultiset(Counter(a=-1), Counter(a=3))`` -> ``True`` — отрицательный
    счётчик не требует ничего;
    ``is_submultiset(Counter(), Counter())`` -> ``True``;
    ``is_submultiset(Counter(x=1), Counter())`` -> ``False`` — в ``right`` ключа
    нет, а у ``Counter`` отсутствующий ключ читается как ``0``.

    Подсказка: ``all(left[key] <= right[key] for key in left if left[key] > 0)``.
    Именно ``right[key]``, а не ``right.get(key, 0)``: у ``Counter`` отсутствующий
    ключ и так даёт ``0``, причём без создания записи.
    """
    raise NotImplementedError


def symmetric_difference(left: Counter[str], right: Counter[str]) -> Counter[str]:
    """Симметрическая разность: ключи, где счётчики различаются.

    Для каждого ключа — модуль разности счётчиков, отбрасывая нули.

    ``symmetric_difference(Counter(a=4, b=1), Counter(a=1, b=1, c=2))`` ->
    ``Counter(a=3, c=2)`` — ``b`` совпал и ушёл, ``c`` был только справа;
    ``symmetric_difference(Counter(a=2), Counter(a=2))`` -> ``Counter()``;
    ``symmetric_difference(Counter(), Counter(x=3))`` -> ``Counter(x=3)``;
    ``symmetric_difference(Counter(a=1), Counter(a=-2))`` -> ``Counter(a=3)`` —
    модуль разности ``|1 - (-2)|``.

    Подсказка: обойдите ``set(left) | set(right)``, берите
    ``abs(left[key] - right[key])`` и добавляйте, только если разность больше
    нуля. Порядок ключей в результате не определён множеством — тест сравнивает
    ``Counter``, для которого порядок не важен.
    """
    raise NotImplementedError


def normalize(counter: Counter[str]) -> Counter[str]:
    """Вернуть счётчик без отрицательных и нулевых значений.

    Оставшиеся элементы отсортированы по ключу.

    ``normalize(Counter(b=1, a=2, c=0, d=-1))`` -> ``Counter(a=2, b=1)``;
    ``normalize(Counter())`` -> ``Counter()``;
    ``normalize(Counter(x=-5))`` -> ``Counter()``.

    Функция семантически совпадает с ``nonzero_items``, но дополнительно
    упорядочивает ключи — тест сравнивает ``Counter`` с литералом, поэтому
    порядок не важен, однако он полезен для воспроизводимого вывода.

    Подсказка: отсортируйте пары с положительным счётчиком
    (``sorted(..., key=lambda item: item[0])``) и передайте их в ``Counter``.
    """
    raise NotImplementedError
