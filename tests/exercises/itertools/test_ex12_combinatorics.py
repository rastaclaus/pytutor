"""Тесты упражнения 12: комбинаторика."""

from __future__ import annotations

from pytutor.exercises.itertools import ex12_combinatorics as ex


def test_all_pairs() -> None:
    assert ex.all_pairs("AB") == [("A", "A"), ("A", "B"), ("B", "A"), ("B", "B")]
    assert ex.all_pairs("") == []


def test_permutations_of() -> None:
    assert ex.permutations_of("ABC", 2) == [
        ("A", "B"),
        ("A", "C"),
        ("B", "A"),
        ("B", "C"),
        ("C", "A"),
        ("C", "B"),
    ]
    # r больше длины входа — пусто, а не ошибка.
    assert ex.permutations_of("AB", 3) == []


def test_combinations_of() -> None:
    assert ex.combinations_of("ABC", 2) == [("A", "B"), ("A", "C"), ("B", "C")]
    assert ex.combinations_of("ABC", 0) == [()]
    assert ex.combinations_of("AB", 3) == []


def test_combinations_with_repeats() -> None:
    assert ex.combinations_with_repeats("AB", 2) == [
        ("A", "A"),
        ("A", "B"),
        ("B", "B"),
    ]


def test_powerset() -> None:
    assert ex.powerset([1, 2]) == [(), (1,), (2,), (1, 2)]
    assert ex.powerset([]) == [()]
    assert len(ex.powerset([1, 2, 3])) == 8


def test_counts_match_actual_lengths() -> None:
    assert ex.count_permutations(4, 2) == len(ex.permutations_of("ABCD", 2)) == 12
    assert ex.count_combinations(4, 2) == len(ex.combinations_of("ABCD", 2)) == 6
    assert ex.count_combinations(4, 0) == 1


def test_dice_sums() -> None:
    distribution = ex.dice_sums()
    assert distribution[2] == 1
    assert distribution[7] == 6
    assert distribution[12] == 1
    assert sum(distribution.values()) == 36
    assert list(distribution) == sorted(distribution)
