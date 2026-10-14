"""Эталон упражнения 15: капстоун-конвейер на ``functools``."""

from __future__ import annotations

from collections.abc import Callable
from functools import cache, partial, reduce, wraps
from typing import Any, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def retry(
    times: int, exceptions: tuple[type[BaseException], ...] = (Exception,)
) -> Callable[[F], F]:
    if times < 1:
        raise ValueError("times должно быть >= 1")

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last: BaseException | None = None
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    last = exc
            assert last is not None
            raise last

        return wrapper  # type: ignore[return-value]

    return decorator


def pipeline(*funcs: Callable[[Any], Any]) -> Callable[[Any], Any]:
    def piped(value: Any) -> Any:
        return reduce(lambda acc, func: func(acc), funcs, value)

    return piped


@cache
def parse_measurement(raw: str) -> int:
    return int(raw.strip())


def _scaled(value: int, *, factor: int, offset: int) -> int:
    return value * factor + offset


def make_scaler(factor: int, offset: int = 0) -> Callable[[int], int]:
    return partial(_scaled, factor=factor, offset=offset)


def scale_value(row: dict[str, Any], scaler: Callable[[int], int]) -> dict[str, Any]:
    return {**row, "value": scaler(row["value"])}


def aggregate_by_category(rows: list[dict[str, Any]]) -> dict[str, int]:
    def step(acc: dict[str, int], row: dict[str, Any]) -> dict[str, int]:
        category = row["cat"]
        acc[category] = acc.get(category, 0) + row["value"]
        return acc

    return reduce(step, rows, {})
