"""Тесты упражнения 16: FIFO / LRU / LFU кэши."""

from __future__ import annotations

import pytest

from pytutor.exercises.collections import ex16_eviction_caches as ex


def test_fifo_cache_evicts_oldest_inserted() -> None:
    cache = ex.FIFOCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    assert cache.get("a") == 1  # то не освежает порядок
    cache.put("c", 3)
    assert cache.get("a") is None  # вытеснен "a" — старейший по вставке
    assert cache.get("b") == 2
    assert cache.get("c") == 3


def test_lru_cache_evicts_least_recently_used() -> None:
    cache = ex.LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    assert cache.get("a") == 1
    cache.put("c", 3)
    assert cache.get("b") is None
    assert cache.get("a") == 1


def test_fifo_len() -> None:
    cache = ex.FIFOCache(2)
    assert len(cache) == 0
    cache.put("a", 1)
    cache.put("b", 2)
    cache.put("c", 3)
    assert len(cache) == 2


def test_lfu_cache_evicts_least_frequently_used() -> None:
    cache = ex.LFUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    assert cache.get("a") == 1
    assert cache.get("a") == 1  # "a" теперь чаще
    cache.put("c", 3)  # вытеснит "b" (1 обращение) вместо "a"
    assert cache.get("b") is None
    assert cache.get("a") == 1
    assert cache.get("c") == 3


def test_caches_reject_bad_capacity() -> None:
    with pytest.raises(ValueError, match="capacity"):
        ex.FIFOCache(0)
    with pytest.raises(ValueError, match="capacity"):
        ex.LRUCache(0)
    with pytest.raises(ValueError, match="capacity"):
        ex.LFUCache(0)
