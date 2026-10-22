"""Тренажёр по модулям стандартной библиотеки Python.

Пакет содержит наборы упражнений (``pytutor.exercises.<модуль>``) и небольшую
CLI для навигации по ним.
"""

from __future__ import annotations

import sys
from pathlib import Path

EXERCISES_DIR = Path(__file__).resolve().parent / "exercises"


def _exercise_sets() -> list[str]:
    """Вернуть имена наборов упражнений (подпакеты ``exercises``)."""
    return sorted(path.name for path in EXERCISES_DIR.iterdir() if path.is_dir() and (path / "__init__.py").exists())


def _exercise_files(module: str) -> list[Path]:
    """Вернуть файлы упражнений набора по возрастанию номера."""
    return sorted((EXERCISES_DIR / module).glob("ex*.py"))


def main(argv: list[str] | None = None) -> int:
    """Показать наборы упражнений и их файлы.

    Использование::

        pytutor            # список наборов
        pytutor itertools  # файлы одного набора
    """
    args = sys.argv[1:] if argv is None else argv
    sets = _exercise_sets()

    if not args:
        print("Наборы упражнений:")
        for name in sets:
            print(f"  {name:<12} {len(_exercise_files(name))} упражнений")
        print("\nПодробности: pytutor <набор>")
        return 0

    module = args[0]
    if module not in sets:
        print(f"Неизвестный набор: {module}. Доступны: {', '.join(sets)}", file=sys.stderr)
        return 1

    print(f"Упражнения набора {module}:")
    for path in _exercise_files(module):
        print(f"  {path.stem}")
    return 0
