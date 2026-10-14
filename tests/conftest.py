"""Общая настройка тестов тренажёра.

По умолчанию тесты проверяют ваши реализации в
``src/pytutor/exercises/...``.

Если выставлена переменная окружения ``PYTUTOR_SOLUTION=1``, модули заданий
подменяются эталонными реализациями из ``solutions/...``. Это нужно, чтобы
убедиться: тесты и эталоны согласованы между собой.

Запуск:

    uv run pytest                       # проверяем ваши решения
    PYTUTOR_SOLUTION=1 uv run pytest    # проверяем эталоны
"""

from __future__ import annotations

import importlib
import importlib.util
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOLUTIONS_DIR = ROOT / "solutions"
EXERCISES_PKG = "pytutor.exercises"


def _install_solutions() -> None:
    """Подменить модули упражнений эталонами (только при PYTUTOR_SOLUTION=1)."""
    if os.environ.get("PYTUTOR_SOLUTION") != "1":
        return
    if not SOLUTIONS_DIR.is_dir():
        return

    for path in sorted(SOLUTIONS_DIR.rglob("*.py")):
        # Пропускаем служебные файлы вроде __init__.py.
        if path.name.startswith("_"):
            continue

        rel = path.relative_to(SOLUTIONS_DIR)
        parts = list(rel.with_suffix("").parts)
        modname = ".".join([EXERCISES_PKG, *parts])

        spec = importlib.util.spec_from_file_location(modname, path)
        if spec is None or spec.loader is None:  # pragma: no cover - защита от опечаток
            raise RuntimeError(f"Не удалось загрузить эталон: {path}")
        module = importlib.util.module_from_spec(spec)
        sys.modules[modname] = module
        spec.loader.exec_module(module)

        # Чтобы работал и `from pytutor.exercises.functools import exNN`, и доступ
        # через атрибут пакета.
        parent_name = modname.rsplit(".", 1)[0]
        parent = importlib.import_module(parent_name)
        setattr(parent, parts[-1], module)


_install_solutions()
