"""Тесты упражнения 13: инвертированный индекс."""

from __future__ import annotations

from collections import Counter

from pytutor.exercises.collections import ex13_inverted_counter as ex


def test_inverted_index() -> None:
    docs = ["рыба меч", "меч в латах", "рыба в реке"]
    index = ex.inverted_index(docs)
    assert index["рыба"] == [0, 2]
    assert index["меч"] == [0, 1]
    assert index["в"] == [1, 2]


def test_positions_of() -> None:
    assert ex.positions_of("a", "b a c a") == [1, 3]
    assert ex.positions_of("x", "b a") == []


def test_doc_frequency() -> None:
    index = ex.inverted_index(["a b", "a c", "b"])
    assert ex.doc_frequency(index) == Counter(a=2, b=2, c=1)


def test_search() -> None:
    index = ex.inverted_index(["рыба меч", "меч в латах", "рыба в реке"])
    assert ex.search(index, "рыба") == [0, 2]
    assert ex.search(index, "нет") == []


def test_top_terms() -> None:
    index = ex.inverted_index(["a b", "a c", "b"])
    assert ex.top_terms(index, 2) == [("a", 2), ("b", 2)]
