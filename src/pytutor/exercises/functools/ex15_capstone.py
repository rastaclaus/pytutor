"""Упражнение 15. Капстоун: конвейер на ``functools``. Уровень 8.

Соберите мини-ETL, где вместе работают ``retry``, ``cache``, ``partial``,
``reduce`` и композиция функций. Реализуйте:

* ``retry(times, exceptions)`` — декоратор с повторами (как в упражнении 6);
* ``pipeline(*funcs)`` — композиция слева направо (как в упражнении 4);
* ``parse_measurement(raw)`` — ``int(raw.strip())``, **замемоизированная**;
* ``make_scaler(factor, offset=0)`` — функция ``value -> value * factor + offset``
  через ``functools.partial`` от готовой ``_scaled``;
* ``scale_value(row, scaler)`` — вернуть копию строки-словаря с полем ``"value"``,
  пропущенным через ``scaler``;
* ``aggregate_by_category(rows)`` — просуммировать ``row["value"]`` по
  ``row["cat"]`` через ``functools.reduce``.

Общее правило: функции не мутируют вход. ``scale_value`` возвращает новый словарь,
``aggregate_by_category`` не меняет ``rows``.
"""

from __future__ import annotations

from collections.abc import Callable
from functools import cache, partial, reduce, wraps
from typing import Any, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def retry(times: int, exceptions: tuple[type[BaseException], ...] = (Exception,)) -> Callable[[F], F]:
    """Декоратор: до ``times`` попыток при исключениях из ``exceptions``.

    ``@retry(3)`` над функцией, падающей один раз, вернёт результат со второй
    попытки;
    ``@retry(2, exceptions=(ValueError,))`` над всегда падающей ``ValueError``
    сделает 2 вызова и пробросит последнюю ошибку;
    ``retry(0)`` -> ``ValueError`` (в сообщении есть ``times``).

    Подсказка: тело можно позаимствовать из упражнения 6 — логика та же.
    """
    if times < 1:
        msg = "times must be => 1"
        raise ValueError(msg)
    def decorator(func: F) -> Callable[[F], F]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last: BaseException
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    last = err
            raise last
        return wrapper
    return decorator


def pipeline(*funcs: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """Композиция слева направо: ``pipeline(f, g)(x) == g(f(x))``.

    ``pipeline(lambda x: x + 1, lambda x: x * 2)(3)`` -> ``8``;
    ``pipeline()(5)`` -> ``5``;
    ``pipeline(lambda x: x + 1)(3)`` -> ``4``.

    Подсказка: ``reduce`` с ``initial`` равным входу — как в упражнении 4.
    """
    def piped(value: Any) -> Callable[[Any], Any]:
        return reduce(lambda acc, func: func(acc), funcs, value)
    return piped



@cache
def parse_measurement(raw: str) -> int:
    """Преобразовать строку в целое (``int(raw.strip())``) и закэшировать результат.

    ``parse_measurement("  10 ")`` -> ``10`` — пробелы по краям снимаются;
    ``parse_measurement("-3")`` -> ``-3``;
    повторный вызов с той же строкой даёт ``cache_info().hits == 1``;
    ``parse_measurement("abc")`` -> ``ValueError``.

    Кэширование нужно именно на уровне функции (декоратор), а не ручным
    словарём: тест обращается к ``cache_info()`` и ``cache_clear()``.

    Подсказка: ``@cache`` над функцией, внутри — ``int(raw.strip())``.
    """
    return pipeline(str.strip, int)(raw)


def _scaled(value: int, *, factor: int, offset: int) -> int:
    """Масштабирование значения: ``value * factor + offset``."""
    return value * factor + offset


def make_scaler(factor: int, offset: int = 0) -> Callable[[int], int]:
    """Вернуть ``value -> value * factor + offset`` через ``functools.partial``.

    ``make_scaler(2, 1)(5)`` -> ``11``;
    ``make_scaler(3)(4)`` -> ``12`` — ``offset`` по умолчанию 0;
    ``make_scaler(-1, 10)(0)`` -> ``10``.

    Подсказка: ``factor`` и ``offset`` у ``_scaled`` — именованные аргументы,
    поэтому ``partial(_scaled, factor=factor, offset=offset)``.
    """
    return partial(_scaled, factor=factor, offset=offset)


def scale_value(row: dict[str, Any], scaler: Callable[[int], int]) -> dict[str, Any]:
    """Вернуть копию ``row``, где ``value`` пропущено через ``scaler``.

    ``scale_value({"cat": "a", "value": 5}, make_scaler(2, 1))`` ->
    ``{"cat": "a", "value": 11}``;
    исходный ``row`` остаётся неизменным;
    остальные ключи копируются как есть, включая не связанные с ``value``
    (например, ``"raw"``).

    Подсказка: ``{**row, "value": scaler(row["value"])}`` — новый словарь без
    мутации входа.
    """
    return {**row, "value": scaler(row["value"])}


def aggregate_by_category(rows: list[dict[str, Any]]) -> dict[str, int]:
    """Сумма ``row["value"]`` по категориям ``row["cat"]`` (через ``reduce``).

    ``aggregate_by_category([{"cat": "a", "value": 1}, {"cat": "b", "value": 2},
    {"cat": "a", "value": 3}])`` -> ``{"a": 4, "b": 2}``;
    ``aggregate_by_category([])`` -> ``{}``.

    Порядок ключей — как при первом появлении категории.

    Подсказка: ``reduce`` с ``initial={}`` и функцией, которая мутирует
    аккумулятор и возвращает его.
    """
    def group_by(acc: dict[str, int], row: dict[str, Any]) -> dict[str, int]:
        cat, value = row["cat"], row["value"]
        acc[cat] = acc.get(cat, 0) + value
        return acc

    return reduce(group_by, rows, {})
