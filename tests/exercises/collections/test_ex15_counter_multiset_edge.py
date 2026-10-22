"""Тесты упражнения 15: крайние случаи ``Counter``."""

from __future__ import annotations

from collections import Counter

from pytutor.exercises.collections import ex15_counter_multiset_edge as ex


def test_nonzero_items() -> None:
    source = Counter(a=2, b=0, c=-1, d=3)
    assert ex.nonzero_items(source) == Counter(a=2, d=3)


def test_keys_with_positive_count() -> None:
    source = Counter(a=2, b=0, c=-1, d=3)
    assert ex.keys_with_positive_count(source) == ["a", "d"]


def test_is_submultiset() -> None:
    assert ex.is_submultiset(Counter(a=2), Counter(a=3, b=1)) is True
    assert ex.is_submultiset(Counter(a=4), Counter(a=3)) is False
    assert ex.is_submultiset(Counter(a=-1), Counter(a=3)) is True
    assert ex.is_submultiset(Counter(), Counter()) is True


def test_symmetric_difference() -> None:
    assert ex.symmetric_difference(Counter(a=4, b=1), Counter(a=1, b=1, c=2)) == Counter(a=3, c=2)
    assert ex.symmetric_difference(Counter(a=2), Counter(a=2)) == Counter()


def test_normalize() -> None:
    assert ex.normalize(Counter(b=1, a=2, c=0, d=-1)) == Counter(a=2, b=1)
