"""Тесты упражнения 10: Top-N с развязкой ничьих."""

from __future__ import annotations

from collections import Counter

import pytest

from pytutor.exercises.collections import ex10_counter_topn_ties as ex


def test_top_n() -> None:
    counter = Counter(a=3, b=1, c=2, d=3)
    assert ex.top_n(counter, 2) == [("a", 3), ("d", 3)]
    assert ex.top_n(counter, 10) == [
        ("a", 3),
        ("d", 3),
        ("c", 2),
        ("b", 1),
    ]


def test_top_n_tie_break_by_key() -> None:
    counter = Counter(b=2, a=2)
    assert ex.top_n(counter, 2) == [("a", 2), ("b", 2)]


def test_bottom_n() -> None:
    counter = Counter(a=3, b=1, c=2, d=1)
    assert ex.bottom_n(counter, 2) == [("b", 1), ("d", 1)]
    assert ex.bottom_n(counter, 10) == [
        ("b", 1),
        ("d", 1),
        ("c", 2),
        ("a", 3),
    ]


def test_top_n_by_key() -> None:
    counter = Counter(b=2, a=3, c=1)
    assert ex.top_n_by_key(counter, 2) == [("a", 3), ("b", 2)]


def test_top_n_rejects_negative_n() -> None:
    counter = Counter(a=1)
    with pytest.raises(ValueError, match="n"):
        ex.top_n(counter, -1)


def test_bottom_n_rejects_negative_n() -> None:
    counter = Counter(a=1)
    with pytest.raises(ValueError, match="n"):
        ex.bottom_n(counter, -1)


def test_top_n_by_key_rejects_negative_n() -> None:
    counter = Counter(a=1)
    with pytest.raises(ValueError, match="n"):
        ex.top_n_by_key(counter, -1)


def test_rank_words() -> None:
    text = "кот пёс кот слон кот пёс"
    assert ex.rank_words(text, 2) == [("кот", 3), ("пёс", 2)]
