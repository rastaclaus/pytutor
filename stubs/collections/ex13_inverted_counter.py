"""Упражнение 13. Инвертированный индекс: словарь + Counter. Уровень 5.

Инвертированный индекс — структура поиска: для каждого термина хранится список
документов (или позиций), где он встречается. Построение на ``defaultdict(list)``
естественно. А ``Counter`` помогает сразу отвечать, сколько раз термин встретился
в документе.

Здесь мы строим мини-поиск по «документам» (строкам): индекс по словам и индекс
позиций вхождения.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


def inverted_index(documents: Iterable[str]) -> dict[str, list[int]]:
    """Построить индекс: слово -> список номеров документов (без повторов).

    Номер документа — его индекс в ``documents``. Документы разбиваются на слова
    по пробелам, регистр игнорируется; пустые слова пропускаются.
    """
    raise NotImplementedError


def positions_of(word: str, text: str) -> list[int]:
    """Вернуть позиции (индексы слов) вхождения ``word`` в ``text``.

    ``positions_of("a", "b a c a")`` -> ``[1, 3]``. Регистр игнорируется.
    """
    raise NotImplementedError


def doc_frequency(index: dict[str, list[int]]) -> Counter[str]:
    """Вернуть ``Counter``: слово -> сколько документов его содержат."""
    raise NotImplementedError


def search(index: dict[str, list[int]], term: str) -> list[int]:
    """Вернуть отсортированный список документов, содержащих ``term``.

    Если термина нет — пустой список.
    """
    raise NotImplementedError


def top_terms(index: dict[str, list[int]], n: int) -> list[tuple[str, int]]:
    """Вернуть top-N самых распространённых терминов (по числу документов)."""
    raise NotImplementedError
