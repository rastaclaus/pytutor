"""Бонусные тесты упражнения 13: ленивый инвертированный индекс.

Необязательное задание повышенной сложности. В базовый прогон не входит:

    uv run pytest -m bonus
"""

from __future__ import annotations

import pytest

from pytutor.exercises.collections import ex13_inverted_counter as ex


@pytest.mark.bonus
def test_lazy_index_yields_sorted_doc_lists() -> None:
    pairs = list(ex.inverted_index_iter(["рыба меч", "меч в латах", "рыба в реке"]))
    index = dict(pairs)
    assert index["рыба"] == [0, 2]
    assert index["меч"] == [0, 1]
    assert index["в"] == [1, 2]


@pytest.mark.bonus
def test_lazy_index_reads_source_once() -> None:
    calls: list[str] = []

    def documents():
        for doc in ("а б", "б в"):
            calls.append(doc)
            yield doc

    result = ex.inverted_index_iter(documents())
    assert len(calls) == 0  # до потребления источник не читается
    consumed = list(result)
    assert calls == ["а б", "б в"]
    assert dict(consumed) == {"а": [0], "б": [0, 1], "в": [1]}


@pytest.mark.bonus
def test_lazy_index_empty() -> None:
    assert list(ex.inverted_index_iter([])) == []
