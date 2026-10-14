"""Эталон упражнения 4: ``compose``/``pipeline`` и ``partialmethod``."""

from __future__ import annotations

from collections.abc import Callable
from functools import partial, partialmethod, reduce
from typing import Any


def compose(*funcs: Callable[[Any], Any]) -> Callable[[Any], Any]:
    def composed(value: Any) -> Any:
        return reduce(lambda acc, func: func(acc), reversed(funcs), value)

    return composed


def pipeline(*funcs: Callable[[Any], Any]) -> Callable[[Any], Any]:
    def piped(value: Any) -> Any:
        return reduce(lambda acc, func: func(acc), funcs, value)

    return piped


def _check_length(text: str, min_len: int, max_len: int | None) -> bool:
    if len(text) < min_len:
        return False
    if max_len is not None and len(text) > max_len:
        return False
    return True


def make_validator(
    min_len: int = 0, max_len: int | None = None
) -> Callable[[str], bool]:
    return partial(_check_length, min_len=min_len, max_len=max_len)


class Logger:
    def __init__(self, prefix: str) -> None:
        self.prefix = prefix
        self.messages: list[str] = []

    def log(self, message: str, *, level: str = "INFO") -> str:
        line = f"{level}: {self.prefix} {message}"
        self.messages.append(line)
        return line

    warn = partialmethod(log, level="WARN")
    debug = partialmethod(log, level="DEBUG")
