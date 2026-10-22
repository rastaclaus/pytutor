"""Тесты упражнения 2: ``chain``."""

from __future__ import annotations

import pytest

from pytutor.exercises.itertools import ex02_chain_flatten as ex


def test_flatten() -> None:
    assert ex.flatten([[1, 2], [], [3]]) == [1, 2, 3]
    assert ex.flatten([]) == []
    assert ex.flatten([[5]]) == [5]


def test_flatten_accepts_generator() -> None:
    assert ex.flatten(iter([[1], [2, 3]])) == [1, 2, 3]


def test_flatten_is_one_level_only() -> None:
    # Вложенность глубже одного уровня не разворачивается.
    assert ex.flatten([[1], [[2]]]) == [1, [2]]


def test_concat() -> None:
    assert ex.concat("ab", ["c"], ()) == ["a", "b", "c"]
    assert ex.concat() == []


def test_words_of() -> None:
    assert ex.words_of(["a b", "c"]) == ["a", "b", "c"]
    assert ex.words_of(["", "  "]) == []


def test_take_flattened_stops_early() -> None:
    assert ex.take_flattened([[1, 2], [3, 4]], 3) == [1, 2, 3]
    assert ex.take_flattened([[1], [2]], 10) == [1, 2]


def test_take_flattened_does_not_consume_everything() -> None:
    consumed: list[int] = []

    def source() -> list[list[int]]:
        for chunk in ([1, 2], [3, 4], [5, 6]):
            consumed.extend(chunk)
            yield chunk

    assert ex.take_flattened(source(), 2) == [1, 2]
    # Потреблён только первый кусок.
    assert consumed == [1, 2]


def test_take_flattened_zero_n() -> None:
    assert ex.take_flattened([[1]], 0) == []


def test_take_flattened_negative_n() -> None:
    with pytest.raises(ValueError, match="0 <= x"):
        ex.take_flattened([[1]], -1)
