"""Тесты упражнения 1: ``Counter`` — простой счёт частот."""

from __future__ import annotations

from collections import Counter

import pytest

from pytutor.exercises.collections import ex01_counter_basics as ex


def test_count_characters() -> None:
    assert ex.count_characters("aab") == Counter(a=2, b=1)
    assert ex.count_characters("") == Counter()


def test_count_words() -> None:
    assert ex.count_words(["a", "b", "a"]) == Counter(a=2, b=1)
    assert ex.count_words([]) == Counter()


def test_most_common_items() -> None:
    counter = Counter(a=3, b=1, c=2)
    assert ex.most_common_items(counter, 2) == [("a", 3), ("c", 2)]
    assert ex.most_common_items(counter, 10) == [("a", 3), ("c", 2), ("b", 1)]
    assert ex.most_common_items(Counter(), 1) == []


def test_most_common_items_rejects_negative_n() -> None:
    with pytest.raises(ValueError, match="n"):
        ex.most_common_items(Counter(a=1), -1)


def test_total_count() -> None:
    assert ex.total_count(Counter(a=2, b=3)) == 5
    assert ex.total_count(Counter()) == 0


def test_unique_items() -> None:
    assert ex.unique_items(Counter(a=2, b=0, c=1)) == ["a", "c"]


def test_expand() -> None:
    assert ex.expand(Counter(a=2, b=1)) == ["a", "a", "b"]
    assert ex.expand(Counter(a=0)) == []
