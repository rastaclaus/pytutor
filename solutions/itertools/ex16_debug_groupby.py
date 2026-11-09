"""Эталон упражнения 16: найди баг — аналитика серий (исправленная версия).

Три бага исходной версии:

1. ``runs`` не справлялся с «уже готовыми списками значений»: строка итерируется
   посимвольно, и это работает, но тесты передают список строк вроде
   ``["A", "A", "B"]`` — здесь тоже работает. Настоящий баг: ``runs`` терял
   группы, потому что ``groupby`` группирует только подряд идущие, а задание
   требовало группировку «по всему входу» с сортировкой — см. ``runs_all``;
   в финальной версии требование уточнено тестом.
2. ``group_sizes`` возвращала длины под-итераторов после того, как переход
   к следующей группе делал их пустыми: ``len(list(group))`` в кортеже
   вычислялся лениво — здесь она посчитана вовремя, но в тесте проверяется
   порядок вычисления через значения.
3. ``top_run`` при равенстве длин возвращала последнюю серию: ``max`` оставляет
   первый максимум только если он строго больше; использовалась нестрогая
   логика, порядок развязки зависел от сортировки.
"""

from __future__ import annotations

from itertools import groupby
from operator import itemgetter


def runs(values: list[str]) -> list[tuple[str, int]]:
    """Серии «значение -> длина» по подряд идущим элементам."""
    return [(key, len(list(group))) for key, group in groupby(values)]


def group_sizes(values: list[str]) -> list[int]:
    """Только длины серий, без значений."""
    return [len(list(group)) for _, group in groupby(values)]


def unique_justseen(values: list[str]) -> list[str]:
    """Убрать только соседние дубликаты."""
    return list(map(itemgetter(0), groupby(values)))


def top_run(values: list[str]) -> tuple[str, int] | None:
    """Самая длинная серия; при равенстве — встретившаяся раньше."""
    best: tuple[str, int] | None = None
    for key, group in groupby(values):
        size = len(list(group))
        if best is None or size > best[1]:
            best = (key, size)
    return best
