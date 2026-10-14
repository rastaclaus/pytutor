"""Упражнение 14. Свой ``memoize`` на ``wraps`` + ``dict``. Уровень 7.

``functools.lru_cache`` умеет много, но полезно уметь написать мемоизацию самому.
Тонкость: ключ должен быть одинаковым для вызовов, записанных по-разному одной и
той же подписью, то есть ``f(1, b=2)``, ``f(b=2, a=1)`` и ``f(1, 2)`` должны
попадать в один и тот же кэш, даже если у параметров есть значения по умолчанию.

Реализуйте ``memoize``:

* используйте ``functools.wraps``, чтобы сохранить метаданные;
* нормализуйте аргументы через ``inspect.signature(func).bind(*args, **kwargs)``,
  затем ``bound.apply_defaults()`` и превратите ``bound.arguments`` в
  хэшируемый ключ (например, ``tuple(sorted(...))``);
* храните кэш в обычном ``dict`` и отдавайте его наружу как ``wrapper.cache``;
  добавьте ``wrapper.cache_clear`` (обёртка над ``dict.clear``).
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def memoize(func: F) -> F:
    """Кэширующий декоратор с нормализацией аргументов по подписи ``func``."""
    raise NotImplementedError
