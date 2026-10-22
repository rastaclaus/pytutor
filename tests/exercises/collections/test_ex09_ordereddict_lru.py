"""Тесты упражнения 9: ``OrderedDict`` и LRU-кэш."""

from __future__ import annotations

from collections import OrderedDict

import pytest

from pytutor.exercises.collections import ex09_ordereddict_lru as ex


def test_lru_cache_basic() -> None:
    cache = ex.LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    assert cache.get("a") == 1
    cache.put("c", 3)  # вытеснит "b" (наименее недавно использованный)
    assert cache.get("b") is None
    assert cache.get("a") == 1
    assert cache.get("c") == 3


def test_lru_cache_update_refreshes() -> None:
    cache = ex.LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("a", 10)  # обновление освежает ключ
    cache.put("c", 3)  # вытеснит "b", не "a"
    assert cache.get("a") == 10
    assert cache.get("b") is None


def test_lru_cache_len() -> None:
    cache = ex.LRUCache(3)
    assert len(cache) == 0
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)
    cache.put("d", 4)
    assert len(cache) == 3


def test_lru_cache_rejects_bad_capacity() -> None:
    with pytest.raises(ValueError, match="capacity"):
        ex.LRUCache(0)


def test_fifo_cache() -> None:
    items = [("a", 1), ("b", 2), ("c", 3), ("d", 4)]
    assert ex.fifo_cache(items, 2) == [("a", 1), ("b", 2)]


def test_touch() -> None:
    cache = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
    result = ex.touch(cache, "a")
    assert result is cache
    assert list(cache) == ["b", "c", "a"]
    ex.touch(cache, "zzz")
    assert "zzz" not in cache


def test_oldest_key() -> None:
    cache = OrderedDict([("a", 1), ("b", 2)])
    assert ex.oldest_key(cache) == "a"
    assert ex.oldest_key(OrderedDict()) is None
