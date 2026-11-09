"""Тесты CLI тренажёра (``pytutor``): команда ``status``."""

from __future__ import annotations

import pytutor


def test_unfinished_detection_stub() -> None:
    path = pytutor.EXERCISES_DIR / "functools" / "ex01_reduce_basics.py"
    if not path.exists():
        return
    # В заготовке каждая функция — только raise NotImplementedError.
    assert len(pytutor._unfinished_functions(path)) >= 4


def test_set_progress_shape() -> None:
    done, total, _next_exercise = pytutor._set_progress("functools")
    assert total >= 15
    assert 0 <= done <= total


def test_status_command_smoke(capsys) -> None:
    assert pytutor.main(["status"]) == 0
    out = capsys.readouterr().out
    assert "Прогресс" in out
    assert "functools" in out
    assert "ИТОГО" in out


def test_status_single_set(capsys) -> None:
    assert pytutor.main(["status", "functools"]) == 0
    out = capsys.readouterr().out
    assert "functools" in out
    assert "boss" not in out


def test_set_listing_has_marks(capsys) -> None:
    assert pytutor.main(["functools"]) == 0
    out = capsys.readouterr().out
    assert "[x]" in out or "[ ]" in out


def test_unknown_set_fails() -> None:
    assert pytutor.main(["no-such-set"]) == 1
