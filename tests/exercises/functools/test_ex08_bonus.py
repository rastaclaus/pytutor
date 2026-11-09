"""Бонусные тесты упражнения 8 (functools): статистика ``lru_cache``.

Необязательное задание повышенной сложности. В базовый прогон не входит:

    uv run pytest -m bonus
"""

from __future__ import annotations

import pytest

from pytutor.exercises.functools import ex08_lru_cache_edge as ex


@pytest.mark.bonus
def test_stats_tracker_large_cache() -> None:
    stats = ex.make_stats_tracker(20)
    assert stats == {"hits": 5, "misses": 10, "currsize": 10}


@pytest.mark.bonus
def test_stats_tracker_tiny_cache() -> None:
    stats = ex.make_stats_tracker(3)
    assert stats == {"hits": 0, "misses": 15, "currsize": 3}


@pytest.mark.bonus
def test_stats_tracker_exact_fit() -> None:
    stats = ex.make_stats_tracker(10)
    assert stats == {"hits": 5, "misses": 10, "currsize": 10}
