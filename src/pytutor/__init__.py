"""Тренажёр по модулям стандартной библиотеки Python.

Пакет содержит наборы упражнений (``pytutor.exercises.<модуль>``) и небольшую
CLI для навигации по ним.
"""

from __future__ import annotations

import ast
import sys
from pathlib import Path

EXERCISES_DIR = Path(__file__).resolve().parent / "exercises"


def _exercise_sets() -> list[str]:
    """Вернуть имена наборов упражнений (подпакеты ``exercises``)."""
    return sorted(path.name for path in EXERCISES_DIR.iterdir() if path.is_dir() and (path / "__init__.py").exists())


def _exercise_files(module: str) -> list[Path]:
    """Вернуть файлы упражнений набора по возрастанию номера."""
    return sorted((EXERCISES_DIR / module).glob("ex*.py"))


def _unfinished_functions(path: Path) -> list[str]:
    """Вернуть имена функций/классов с телом «только ``NotImplementedError``».

    Считаем незаконченным любой ``def``/``class``, во всех ``return``-путях
    которого стоит один ``raise NotImplementedError``.
    """
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except SyntaxError:
        return []

    unfinished: list[str] = []

    def has_not_implemented_only(body: list[ast.stmt]) -> bool:
        """Все содержательные операторы тела — ``raise NotImplementedError``."""
        meaningful = [stmt for stmt in body if not isinstance(stmt, ast.Expr | ast.Pass | ast.AnnAssign)]
        if not meaningful:
            return False  # тело из докстринга — это «данные», не задание
        return all(
            isinstance(stmt, ast.Raise)
            and (
                stmt.exc is None
                or (isinstance(stmt.exc, ast.Name) and stmt.exc.id == "NotImplementedError")
                or (
                    isinstance(stmt.exc, ast.Call)
                    and isinstance(stmt.exc.func, ast.Name)
                    and stmt.exc.func.id == "NotImplementedError"
                )
            )
            for stmt in meaningful
        )

    def walk(node: ast.AST, prefix: str) -> None:
        for child in ast.iter_child_nodes(node):
            if isinstance(child, ast.ClassDef):
                name = f"{prefix}{child.name}"
                if has_not_implemented_only(child.body):
                    unfinished.append(name)
                else:
                    walk(child, "")
            elif isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                name = f"{prefix}{child.name}"
                if has_not_implemented_only(child.body):
                    unfinished.append(name)
                walk(child, "")

    walk(tree, "")
    return unfinished


def _set_progress(module: str) -> tuple[int, int, str | None]:
    """Вернуть ``(сделано, всего, следующее_упражнение)`` для набора."""
    files = _exercise_files(module)
    total = len(files)
    done = 0
    next_exercise: str | None = None
    for path in files:
        if not _unfinished_functions(path):
            done += 1
        elif next_exercise is None:
            next_exercise = path.stem
    return done, total, next_exercise


def _print_status(module: str | None) -> None:
    """Показать прогресс по наборам."""
    sets = [module] if module is not None else _exercise_sets()
    print("Прогресс (по телам функций без NotImplementedError):")
    total_done, total_all = 0, 0
    for name in sets:
        done, total, next_exercise = _set_progress(name)
        total_done += done
        total_all += total
        percent = round(100 * done / total) if total else 0
        suffix = f" — дальше: {next_exercise}" if next_exercise else ""
        print(f"  {name:<12} {done:>3}/{total:<3} ({percent:>3}%){suffix}")
    if len(sets) > 1:
        percent = round(100 * total_done / total_all) if total_all else 0
        print(f"\n  {'ИТОГО':<12} {total_done:>3}/{total_all:<3} ({percent}%)")


def main(argv: list[str] | None = None) -> int:
    """Показать наборы упражнений, их файлы или прогресс.

    Использование::

        pytutor            # список наборов
        pytutor itertools  # файлы одного набора
        pytutor status     # прогресс по всем наборам
        pytutor status functools  # прогресс одного набора
    """
    args = sys.argv[1:] if argv is None else argv
    sets = _exercise_sets()

    if not args:
        print("Наборы упражнений:")
        for name in sets:
            print(f"  {name:<12} {len(_exercise_files(name))} упражнений")
        print("\nПодробности: pytutor <набор>; прогресс: pytutor status")
        return 0

    module = args[0]
    if module == "status":
        _print_status(args[1] if len(args) > 1 else None)
        return 0

    if module not in sets:
        print(f"Неизвестный набор: {module}. Доступны: {', '.join(sets)}, status", file=sys.stderr)
        return 1

    print(f"Упражнения набора {module}:")
    for path in _exercise_files(module):
        unfinished = _unfinished_functions(path)
        mark = " " if unfinished else "x"
        print(f"  [{mark}] {path.stem}")
    return 0
