"""Тесты упражнения 5: ``accumulate``."""

from __future__ import annotations

import pytest

from pytutor.exercises.itertools import ex05_accumulate as ex


def test_running_sum() -> None:
    assert ex.running_sum([1, 2, 3]) == [1, 3, 6]
    assert ex.running_sum([]) == []
    assert ex.running_sum([5]) == [5]


def test_running_sum_with_start() -> None:
    assert ex.running_sum_with_start(10, [1, 2]) == [10, 11, 13]
    # initial попадает в результат даже для пустого входа.
    assert ex.running_sum_with_start(42, []) == [42]


def test_running_product() -> None:
    assert ex.running_product([2, 3, 4]) == [2, 6, 24]
    assert ex.running_product([]) == []


def test_running_max() -> None:
    assert ex.running_max([3, 1, 4, 2]) == [3, 3, 4, 4]
    assert ex.running_max([]) == []


def test_running_balance() -> None:
    assert ex.running_balance([100, -30, -50]) == [0, 100, 70, 20]
    assert ex.running_balance([]) == [0]


def test_final_sum() -> None:
    assert ex.final_sum([1, 2, 3]) == 6
    assert ex.final_sum([]) == 0


def test_running_pairwise_ratio() -> None:
    assert ex.running_pairwise_ratio([100, 2, 5]) == pytest.approx([100, 50, 10])
    assert ex.running_pairwise_ratio([7]) == [7]
    assert ex.running_pairwise_ratio([]) == []
