"""Упражнение 16. Найди баг: аналитика серий на ``groupby``. Уровень 6.

Реализация ниже прошла «тест на глаз»: для ``"AAABBC"`` она вроде бы выдаёт
правильный ответ. Но в ней **три бага**, и проявляются они только на других
входах. Найдите и исправьте их, не переписывая функции заново.

Как искать: прогоните тесты (``uv run pytest -k ex16_debug``) и сравните
ожидаемое поведение с фактическим. Напоминание из упражнения 9: ``groupby``
группирует только **подряд идущие** элементы, а его под-итераторы умирают
при переходе к следующей группе.

Сценарии, где баги проявятся: несортированные значения, обращение к группам
после прохода, работа с уже готовыми списками значений.
"""

from __future__ import annotations

from itertools import groupby
from operator import itemgetter


def runs(values: list[str]) -> list[tuple[str, int]]:
    """Серии «значение -> длина» по подряд идущим элементам."""
    result: list[tuple[str, int]] = []
    groups = [(key, group) for key, group in groupby(values)]
    for key, group in groups:
        result.append((key, len(list(group))))
    return result


def group_sizes(values: list[str]) -> list[int]:
    """Только длины серий, без значений."""
    return [len(list(group)) for _, group in groupby(values)]


def unique_justseen(values: list[str]) -> list[str]:
    """Убрать только **соседние** дубликаты: ``"AABBA"`` -> ``["A", "B", "A"]``."""
    return list(map(itemgetter(0), groupby(values)))


def top_run(values: list[str]) -> tuple[str, int] | None:
    """Самая длинная серия или ``None`` для пустого входа.

    При равенстве длин побеждает серия, встретившаяся раньше.
    """
    series = runs(values)
    if not series:
        return None
    best = series[0]
    for item in series[1:]:
        if item[1] >= best[1]:
            best = item
    return best
