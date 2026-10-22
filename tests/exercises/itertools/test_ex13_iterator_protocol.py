"""Тесты упражнения 13: протокол итератора."""

from __future__ import annotations

from collections.abc import Iterator

from pytutor.exercises.itertools import ex13_iterator_protocol as ex


def test_exhaust_list_can_be_reused() -> None:
    assert ex.exhaust([1, 2]) == ([1, 2], [1, 2])


def test_exhaust_iterator_is_single_use() -> None:
    assert ex.exhaust(iter([1, 2])) == ([1, 2], [])


def test_materialise_fixes_single_use() -> None:
    assert ex.materialise(iter([1, 2])) == ([1, 2], [1, 2])


def test_is_iterator() -> None:
    assert ex.is_iterator(iter([1])) is True
    assert ex.is_iterator(value for value in [1]) is True
    assert ex.is_iterator([1]) is False
    assert ex.is_iterator("abc") is False


def test_read_until_sentinel() -> None:
    values = iter([1, 2, -1, 3])
    assert ex.read_until_sentinel(lambda: next(values, -1), -1) == [1, 2]


def test_read_until_sentinel_from_start() -> None:
    assert ex.read_until_sentinel(lambda: 0, 0) == []


def test_lazy_map_is_lazy() -> None:
    seen: list[int] = []
    stream, journal = ex.lazy_map_side_effects([1, 2, 3], seen)
    assert journal == []
    assert isinstance(stream, Iterator)
    assert next(stream) == 2
    assert journal == [1]
    assert list(stream) == [4, 6]
    assert journal == [1, 2, 3]


def test_count_until_limit_stops_early() -> None:
    seen: list[int] = []
    # 1 + 2 + 3 + 4 = 10 > 8, поэтому последнее добавленное — 4.
    assert ex.count_until_limit(8, seen) == 4
    assert seen == [1, 2, 3, 4]
