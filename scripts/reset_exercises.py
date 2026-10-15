"""Сбросить решения упражнений к исходному виду (заготовкам).

Заготовки лежат в ``stubs/<модуль>/ex*.py`` — это те же файлы упражнений, но с
телами-``raise NotImplementedError`` вместо решений (при этом «данные» функции и
классы, которые реализованы в рамках упражнения, сохранены как есть).

Скрипт просто копирует эти файлы поверх
``src/pytutor/exercises/<модуль>/``, затирая ваши решения. Никакого разбора кода —
только копирование, поэтому он идемпотентен и безопасен для повторных запусков.

Примеры:

    uv run python scripts/reset_exercises.py              # все наборы
    uv run python scripts/reset_exercises.py -m functools # один набор
    uv run python scripts/reset_exercises.py -m functools -e ex04

Чтобы добавить новый набор упражнений, положите его заготовки в
``stubs/<модуль>/``.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STUBS_DIR = ROOT / "stubs"
EXERCISES_DIR = ROOT / "src" / "pytutor" / "exercises"


def main(argv: list[str] | None = None) -> int:
    """Скопировать заготовки из stubs/ в src/pytutor/exercises/."""
    parser = argparse.ArgumentParser(description="Сбросить упражнения к исходным заготовкам из stubs/.")
    parser.add_argument("-m", "--module", help="Ограничиться набором (например, functools).")
    parser.add_argument(
        "-e",
        "--exercise",
        help="Ограничиться одним упражнением (например, ex04).",
    )
    args = parser.parse_args(argv)

    if not STUBS_DIR.is_dir():
        print(f"Не найден каталог заготовок: {STUBS_DIR}")
        return 1

    modules = [STUBS_DIR / args.module] if args.module else sorted(p for p in STUBS_DIR.iterdir() if p.is_dir())

    copied = 0
    for stubs_module in modules:
        if not stubs_module.is_dir():
            print(f"Пропущен несуществующий каталог заготовок: {stubs_module}")
            continue
        target_module = EXERCISES_DIR / stubs_module.name
        for stub in sorted(stubs_module.glob("ex*.py")):
            if args.exercise and not stub.stem.startswith(args.exercise):
                continue
            target = target_module / stub.name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(stub, target)
            print(f"{target.relative_to(ROOT)} ← {stub.relative_to(ROOT)}")
            copied += 1

    print(f"\nСброшено файлов: {copied}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
