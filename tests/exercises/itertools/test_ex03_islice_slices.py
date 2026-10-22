"""Тесты упражнения 3: ``islice``."""

from __future__ import annotations

from collections.abc import Iterator
from itertools import count

import pytest

from pytutor.exercises.itertools import ex03_islice_slices as ex


def test_head() -> None:
    assert ex.head(3, count(10)) == [10, 11, 12]
    assert ex.head(0, count()) == []
    assert ex.head(5, [1, 2]) == [1, 2]


def test_drop_first() -> None:
    assert ex.drop_first(2, [0, 1, 2, 3]) == [2, 3]
    assert ex.drop_first(0, [1, 2]) == [1, 2]
    assert ex.drop_first(5, [1, 2]) == []


def test_drop_first_consumes_iterator() -> None:
    iterator = iter(range(5))
    assert list(iterator) == [0, 1, 2, 3, 4]
    iterator = iter(range(5))
    assert ex.drop_first(2, iterator) == [2, 3, 4]
    assert list(iterator) == []


def test_every_nth() -> None:
    assert ex.every_nth(3, range(7)) == [0, 3, 6]
    assert ex.every_nth(1, [1, 2, 3]) == [1, 2, 3]
    assert ex.every_nth(10, range(3)) == [0]


def test_every_nth_rejects_non_positive() -> None:
    with pytest.raises(ValueError, match="n"):
        ex.every_nth(0, range(3))


def test_nth() -> None:
    assert ex.nth(count(), 0) == 0
    assert ex.nth(count(100), 4) == 104
    assert ex.nth([1, 2], 5) is None
    assert ex.nth([1, 2], 5, default=-1) == -1


def test_nth_does_not_exhaust_large_series() -> None:
    assert ex.nth(count(), 10_000) == 10_000


def test_nth_rejects_negative_index() -> None:
    with pytest.raises(ValueError, match="index"):
        ex.nth([1, 2, 3], -1)


def test_first_three_returns_lazy_iterator() -> None:
    result = ex.first_three(count())
    assert isinstance(result, Iterator)
    assert list(result) == [0, 1, 2]
    # islice одноразовый, как и любой итератор.
    assert list(result) == []
