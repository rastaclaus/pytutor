"""Тесты упражнения 6: ``starmap`` и ``repeat``."""

from __future__ import annotations

from pytutor.exercises.itertools import ex06_starmap_zip_args as ex


def test_apply_pairs() -> None:
    assert ex.apply_pairs(pow, [(2, 5), (3, 2)]) == [32, 9]
    assert ex.apply_pairs(lambda a, b: a - b, [(5, 3)]) == [2]
    assert ex.apply_pairs(pow, []) == []


def test_dot_product() -> None:
    assert ex.dot_product([1, 2, 3], [4, 5, 6]) == 32
    assert ex.dot_product([], []) == 0
    # zip останавливается по короткому входу.
    assert ex.dot_product([1, 2], [10]) == 10


def test_total_cost() -> None:
    assert ex.total_cost([(2, 3), (10, 2)]) == 26
    assert ex.total_cost([]) == 0


def test_repeat_apply() -> None:
    assert ex.repeat_apply(str.upper, "ab", 3) == ["AB", "AB", "AB"]
    assert ex.repeat_apply(str.upper, "ab", 0) == []


def test_pair_with_constant() -> None:
    assert ex.pair_with_constant(["a", "b"], 0) == [("a", 0), ("b", 0)]
    assert ex.pair_with_constant([], 1) == []


def test_apply_all() -> None:
    assert ex.apply_all([abs, lambda value: value + 1], -3) == [3, -2]
    assert ex.apply_all([], 5) == []


def test_make_formatter() -> None:
    formatter = ex.make_formatter("kg")
    assert formatter(5) == "5 kg"
    assert ex.make_formatter("m")(2) == "2 m"


def test_format_values() -> None:
    assert ex.format_values([1, 2], "s") == ["1 s", "2 s"]
    assert ex.format_values([], "s") == []
