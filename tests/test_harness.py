"""Тесты самого харнесса: подмена заданий эталонами при ``PYTUTOR_SOLUTION=1``.

Проверки не зависят от того, решены ли упражнения в рабочей копии: тестовые
фикстуры создают временный «мини-репозиторий» внутри ``tmp_path`` и запускают
pytest в нём.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFTEST = ROOT / "tests" / "conftest.py"

EXERCISE = '''\
from __future__ import annotations


def double(value: int) -> int:
    """Удвоить число."""
    raise NotImplementedError
'''

SOLUTION = '''\
from __future__ import annotations


def double(value: int) -> int:
    """Удвоить число."""
    return value * 2
'''

TEST = """\
from __future__ import annotations

from pytutor.exercises.demo import ex01_double as ex


def test_double() -> None:
    assert ex.double(21) == 42
"""


def _build_sandbox(tmp_path: Path) -> Path:
    """Собрать мини-репозиторий с одним набором ``demo``."""
    (tmp_path / "src" / "pytutor" / "exercises" / "demo").mkdir(parents=True)
    (tmp_path / "src" / "pytutor" / "__init__.py").write_text("", encoding="utf-8")
    (tmp_path / "src" / "pytutor" / "exercises" / "__init__.py").write_text("", encoding="utf-8")
    (tmp_path / "src" / "pytutor" / "exercises" / "demo" / "__init__.py").write_text("", encoding="utf-8")
    (tmp_path / "src" / "pytutor" / "exercises" / "demo" / "ex01_double.py").write_text(EXERCISE, encoding="utf-8")

    (tmp_path / "solutions" / "demo").mkdir(parents=True)
    (tmp_path / "solutions" / "demo" / "ex01_double.py").write_text(SOLUTION, encoding="utf-8")

    (tmp_path / "tests").mkdir()
    (tmp_path / "tests" / "conftest.py").write_text(CONFTEST.read_text(encoding="utf-8"), encoding="utf-8")
    (tmp_path / "tests" / "test_demo.py").write_text(TEST, encoding="utf-8")
    (tmp_path / "pyproject.toml").write_text(
        '[tool.pytest.ini_options]\ntestpaths = ["tests"]\naddopts = "--import-mode=importlib"\n',
        encoding="utf-8",
    )
    return tmp_path


def _run(tmp_path: Path, *, solution: bool) -> subprocess.CompletedProcess[str]:
    env = {**os.environ, "PYTHONPATH": str(tmp_path / "src")}
    if solution:
        env["PYTUTOR_SOLUTION"] = "1"
    else:
        env.pop("PYTUTOR_SOLUTION", None)
    return subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider"],
        cwd=tmp_path,
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )


def test_exercise_stub_fails(tmp_path: Path) -> None:
    sandbox = _build_sandbox(tmp_path)
    result = _run(sandbox, solution=False)
    assert result.returncode != 0
    assert "NotImplementedError" in result.stdout


def test_solution_mode_replaces_module(tmp_path: Path) -> None:
    sandbox = _build_sandbox(tmp_path)
    result = _run(sandbox, solution=True)
    assert result.returncode == 0, result.stdout + result.stderr
