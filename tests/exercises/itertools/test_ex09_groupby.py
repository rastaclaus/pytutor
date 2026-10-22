"""Тесты упражнения 9: ``groupby``."""

from __future__ import annotations

from itertools import groupby

from pytutor.exercises.itertools import ex09_groupby as ex


def test_runs() -> None:
    assert ex.runs("AAABBC") == [("A", 3), ("B", 2), ("C", 1)]
    assert ex.runs("") == []
    assert ex.runs("AB") == [("A", 1), ("B", 1)]


def test_groups_as_lists_without_key() -> None:
    assert ex.groups_as_lists("AAB") == [("A", ["A", "A"]), ("B", ["B"])]


def test_groups_as_lists_with_key() -> None:
    assert ex.groups_as_lists("aAbB", key=str.lower) == [
        ("a", ["a", "A"]),
        ("b", ["b", "B"]),
    ]


def test_groups_are_not_adjacent() -> None:
    # "ABA" — подряд идущих групп три, хотя значений всего два.
    assert ex.runs("ABA") == [("A", 1), ("B", 1), ("A", 1)]


def test_unique_justseen() -> None:
    assert ex.unique_justseen("AAABBCA") == ["A", "B", "C", "A"]
    assert ex.unique_justseen("") == []


def test_group_by_parity_ignores_input_order() -> None:
    assert ex.group_by_parity([1, 2, 3, 4]) == {"нечётные": [1, 3], "чётные": [2, 4]}
    assert ex.group_by_parity([4, 1, 3, 2]) == {"нечётные": [1, 3], "чётные": [4, 2]}
    assert ex.group_by_parity([]) == {}


def test_longest_run() -> None:
    assert ex.longest_run("AABBBCC") == ("B", 3)
    assert ex.longest_run("") is None
    # При равной длине побеждает первая серия.
    assert ex.longest_run("AABB") == ("A", 2)


def test_group_words_by_length() -> None:
    assert ex.group_words_by_length(["ab", "c", "de", "f"]) == {
        1: ["c", "f"],
        2: ["ab", "de"],
    }


def test_groups_are_materialised_so_nothing_disappears() -> None:
    # Сырой groupby теряет данные: после перехода к следующей группе
    # предыдущая становится пустой.
    seen: list[list[int]] = []
    pending = groupby([1, 1, 2])
    first_key, first_group = next(pending)
    second_key, second_group = next(pending)
    seen.append(list(first_group))
    seen.append(list(second_group))
    assert (first_key, second_key) == (1, 2)
    assert seen == [[], [2]]

    # А groups_as_lists материализует группы сразу — данные целы.
    assert ex.groups_as_lists([1, 1, 2]) == [(1, [1, 1]), (2, [2])]
