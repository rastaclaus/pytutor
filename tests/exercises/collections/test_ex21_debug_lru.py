"""Тесты упражнения 21: найди баг — LRU-кэш.

Тесты описывают правильное поведение LRU. Класс ``BuggyLRUCache`` в заготовке
содержит три бага; после исправлений все тесты должны стать зелёными.
"""

from __future__ import annotations

import pytest

from pytutor.exercises.collections import ex21_debug_lru as ex


def test_get_refreshes_key() -> None:
    cache = ex.BuggyLRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    assert cache.get("a") == 1  # "a" теперь самый свежий
    cache.put("c", 3)  # вытесняется "b", не "a"
    assert cache.get("b") is None
    assert cache.get("a") == 1


def test_get_missing_returns_none_without_error() -> None:
    cache = ex.BuggyLRUCache(2)
    assert cache.get("nope") is None
    assert len(cache) == 0


def test_evicts_oldest_not_freshest() -> None:
    cache = ex.BuggyLRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)  # вытесняется "a" — самый старый
    assert cache.get("a") is None
    assert cache.get("b") == 2
    assert cache.get("c") == 3


def test_put_existing_key_refreshes() -> None:
    cache = ex.BuggyLRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("a", 10)
    cache.put("c", 3)  # вытесняется "b"
    assert cache.get("a") == 10
    assert cache.get("b") is None


def test_len_never_exceeds_capacity() -> None:
    cache = ex.BuggyLRUCache(3)
    for i in range(5):
        cache.put(f"k{i}", i)
    assert len(cache) == 3


def test_zero_or_negative_capacity_rejected() -> None:
    with pytest.raises(ValueError, match="capacity"):
        ex.BuggyLRUCache(0)
    with pytest.raises(ValueError, match="capacity"):
        ex.BuggyLRUCache(-1)
