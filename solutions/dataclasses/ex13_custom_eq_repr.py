"""Эталон упражнения 13: тонкая настройка полей."""

from __future__ import annotations

from dataclasses import dataclass, field


def declare_cache_entry() -> type:
    @dataclass
    class CacheEntry:
        """Запись кэша; счётчик попаданий не влияет на идентичность."""

        key: str
        payload: str
        hits: int = field(default=0, repr=False, compare=False)

    return CacheEntry


def make_entry(key: str, payload: str, hits: int = 0) -> object:
    return declare_cache_entry()(key, payload, hits)


def repr_excludes_hits() -> bool:
    entry = make_entry("k", "v", 7)
    return "hits" not in repr(entry)


def equality_ignores_hits() -> bool:
    entry_cls = declare_cache_entry()
    return entry_cls("k", "v", 1) == entry_cls("k", "v", 99)


def declare_unsafe_hashable() -> type:
    @dataclass(unsafe_hash=True)
    class Raw:
        """Изменяемый, но намеренно хешируемый класс."""

        value: int

    return Raw


def unsafe_hash_is_generated() -> bool:
    raw_cls = declare_unsafe_hashable()
    try:
        hash(raw_cls(1))
    except TypeError:
        return False
    return True
