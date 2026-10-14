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
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def retry(
    times: int, exceptions: tuple[type[BaseException], ...] = (Exception,)
) -> Callable[[F], F]:
    """Декоратор: до ``times`` попыток при исключениях из ``exceptions``."""
    raise NotImplementedError


def pipeline(*funcs: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """Композиция слева направо: ``pipeline(f, g)(x) == g(f(x))``."""
    raise NotImplementedError


def parse_measurement(raw: str) -> int:
    """Преобразовать строку в целое (``int(raw.strip())``) и закэшировать результат."""
    raise NotImplementedError


def _scaled(value: int, *, factor: int, offset: int) -> int:
    """Масштабирование значения: ``value * factor + offset``."""
    return value * factor + offset


def make_scaler(factor: int, offset: int = 0) -> Callable[[int], int]:
    """Вернуть ``value -> value * factor + offset`` через ``functools.partial``."""
    raise NotImplementedError


def scale_value(row: dict[str, Any], scaler: Callable[[int], int]) -> dict[str, Any]:
    """Вернуть копию ``row``, где ``value`` пропущено через ``scaler``."""
    raise NotImplementedError


def aggregate_by_category(rows: list[dict[str, Any]]) -> dict[str, int]:
    """Сумма ``row["value"]`` по категориям ``row["cat"]`` (через ``reduce``)."""
    raise NotImplementedError
