"""Тесты упражнения 5: арифметика ``Counter``."""

from __future__ import annotations

from collections import Counter

import pytest

from pytutor.exercises.collections import ex05_counter_arithmetic as ex


def test_combine() -> None:
    assert ex.combine(Counter(a=1), Counter(a=2, b=1)) == Counter(a=3, b=1)
    assert ex.combine() == Counter()


def test_add_counts() -> None:
    assert ex.add_counts(Counter(a=1, b=2), Counter(b=1)) == Counter(a=1, b=3)


def test_difference_counts() -> None:
    assert ex.difference_counts(Counter(a=3, b=1), Counter(a=5)) == Counter(b=1)


def test_overlap_counts() -> None:
    assert ex.overlap_counts(Counter(a=3, b=2), Counter(a=1, c=5)) == Counter(a=1)


def test_union_counts() -> None:
    assert ex.union_counts(Counter(a=3, b=2), Counter(a=1, c=5)) == Counter(a=3, b=2, c=5)


def test_subtract_inplace() -> None:
    left = Counter(a=3, b=1)
    result = ex.subtract_inplace(left, Counter(a=5))
    assert result is left
    assert left == Counter(a=-2, b=1)


def test_merge_strategies() -> None:
    left = Counter(a=3, b=1)
    right = Counter(a=1, b=2, c=1)
    assert ex.merge_strategies(left, right, "add") == Counter(a=4, b=3, c=1)
    assert ex.merge_strategies(left, right, "max") == Counter(a=3, b=2, c=1)
    assert ex.merge_strategies(left, right, "min") == Counter(a=1, b=1)
    assert ex.merge_strategies(left, right, "sub") == Counter(a=2)


def test_merge_strategies_rejects_unknown() -> None:
    with pytest.raises(ValueError, match="стратегия"):
        ex.merge_strategies(Counter(), Counter(), "unknown")
