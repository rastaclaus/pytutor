"""Эталон упражнения 6: декораторы с аргументами."""

from __future__ import annotations

from collections.abc import Callable
from functools import wraps
from typing import Any, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def repeat(times: int) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return [func(*args, **kwargs) for _ in range(times)]

        return wrapper  # type: ignore[return-value]

    return decorator


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
