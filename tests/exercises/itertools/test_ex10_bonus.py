"""Бонусные тесты упражнения 10 (itertools): скользящее окно через ``tee``.

Необязательное задание повышенной сложности. В базовый прогон не входит:

    uv run pytest -m bonus
"""

from __future__ import annotations

import pytest

from pytutor.exercises.itertools import ex10_tee as ex


@pytest.mark.bonus
def test_windowed_basic() -> None:
    assert list(ex.windowed([1, 2, 3, 4], 2)) == [(1, 2), (2, 3), (3, 4)]
    assert list(ex.windowed("ABCDE", 3)) == [
        ("A", "B", "C"),
        ("B", "C", "D"),
        ("C", "D", "E"),
    ]


@pytest.mark.bonus
def test_windowed_edge_cases() -> None:
    assert list(ex.windowed([1, 2], 3)) == []
    assert list(ex.windowed([], 1)) == []
    assert list(ex.windowed([1, 2, 3], 1)) == [(1,), (2,), (3,)]


@pytest.mark.bonus
def test_windowed_rejects_bad_size() -> None:
    with pytest.raises(ValueError, match="size"):
        list(ex.windowed([1], 0))
    with pytest.raises(ValueError, match="size"):
        list(ex.windowed([1], -2))


@pytest.mark.bonus
def test_windowed_is_lazy() -> None:
    calls: list[int] = []

    def source():
        for value in range(100):
            calls.append(value)
            yield value

    result = ex.windowed(source(), 3)
    assert len(calls) == 0  # до потребления источник не читается
    first = next(result)
    assert first == (0, 1, 2)
    assert calls == [0, 1, 2]  # прочитаны только элементы первого окна
