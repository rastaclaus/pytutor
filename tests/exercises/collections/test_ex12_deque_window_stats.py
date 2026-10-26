"""Тесты упражнения 12: скользящее окно: статистика в потоке."""

from __future__ import annotations

import pytest

from pytutor.exercises.collections import ex12_deque_window_stats as ex


def test_moving_average() -> None:
    result = list(ex.moving_average([1, 2, 3, 4], 2))
    assert result == [1.5, 2.5, 3.5]
    assert list(ex.moving_average([1, 2], 5)) == []
    assert list(ex.moving_average([], 2)) == []


def test_moving_average_rejects_non_positive_size() -> None:
    with pytest.raises(ValueError, match="size"):
        list(ex.moving_average([1], 0))
    with pytest.raises(ValueError, match="size"):
        list(ex.moving_average([1], -1))


def test_moving_max_rejects_non_positive_size() -> None:
    with pytest.raises(ValueError, match="size"):
        list(ex.moving_max([1], 0))


def test_moving_min_rejects_non_positive_size() -> None:
    with pytest.raises(ValueError, match="size"):
        list(ex.moving_min([1], -2))


def test_deviation_from_mean_rejects_non_positive_size() -> None:
    with pytest.raises(ValueError, match="size"):
        list(ex.deviation_from_mean([1], 0))


def test_moving_max() -> None:
    assert list(ex.moving_max([1, 3, 2, 5], 2)) == [3, 3, 5]


def test_moving_min() -> None:
    assert list(ex.moving_min([3, 1, 2, 5], 2)) == [1, 1, 2]


def test_deviation_from_mean() -> None:
    result = list(ex.deviation_from_mean([1, 3, 5, 7], 2))
    assert result == [1.0, 1.0, 1.0]
