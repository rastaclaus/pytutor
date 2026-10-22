"""Упражнение 14. Слияние ``ChainMap``: «плоский» словарь и отчёт. Уровень 6.

``ChainMap`` — представление «на лету», без копирования. Но часто нужен
материализованный результат: «плоский» словарь, где конфликты разрешены в
пользу приоритетного слоя, и отчёт о том, из какого слоя пришёл каждый ключ.

В этом упражнении мы учимся «вытаскивать» данные из ``ChainMap`` в разные формы.
"""

from __future__ import annotations

from collections import ChainMap
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def flatten(cm: ChainMap[str, int]) -> dict[str, int]:
    """Слить все слои в обычный словарь.

    Приоритет — у первого слоя (как при обычном поиске в ``ChainMap``).
    """
    raise NotImplementedError


def source_report(cm: ChainMap[str, int]) -> dict[str, int]:
    """Вернуть отчёт: ключ -> номер слоя, где он найден.

    Номера начинаются с 0 (самый приоритетный слой). Если ключ есть в нескольких
    слоях — указать первый.
    """
    raise NotImplementedError


def conflict_keys(cm: ChainMap[str, int]) -> list[str]:
    """Вернуть ключи, которые есть более чем в одном слое.

    Порядок — как в ``flatten``.
    """
    raise NotImplementedError


def update_all_layers(cm: ChainMap[str, int], key: str, value: int) -> ChainMap[str, int]:
    """Записать ``key=value`` во все слои, где ключ уже существует.

    В слоях, где ключа нет, ничего не менять. Вернуть ``cm``.
    """
    raise NotImplementedError


def merged_from(layers: Iterable[dict[str, int]]) -> dict[str, int]:
    """Слить произвольное число словарей в один.

    Более поздние словари имеют приоритет над более ранними.
    """
    raise NotImplementedError
