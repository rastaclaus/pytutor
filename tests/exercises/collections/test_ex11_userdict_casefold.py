"""Тесты упражнения 11: ``UserDict`` — регистронезависимые ключи."""

from __future__ import annotations

from pytutor.exercises.collections import ex11_userdict_casefold as ex


def test_case_insensitive_get_set() -> None:
    d = ex.CaseInsensitiveDict()
    d["Hello"] = 1
    assert d["hello"] == 1
    assert d["HELLO"] == 1
    d["HELLO"] = 2
    assert len(d) == 1
    assert d["hello"] == 2


def test_case_insensitive_delete_and_contains() -> None:
    d = ex.CaseInsensitiveDict()
    d["Привет"] = 1
    assert "привет" in d
    assert "ПРИВЕТ" in d
    del d["ПРИВЕТ"]
    assert "привет" not in d
    assert len(d) == 0


def test_case_insensitive_missing_key() -> None:
    d = ex.CaseInsensitiveDict()
    with __import__("pytest").raises(KeyError):
        _ = d["ну"]
    assert None not in d


def test_count_case_insensitive() -> None:
    result = ex.count_case_insensitive(["Кот", "кот", "КОТ", "пёс"])
    assert result == {"Кот": 3, "пёс": 1}
