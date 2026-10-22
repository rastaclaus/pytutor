"""Упражнение 20. Капстоун: конвейер аналитики текста. Уровень 8.

Финальное упражнение набора собирает почти все типы ``collections`` в один
конвейер: ``Counter`` для частот, ``namedtuple`` для строк отчёта, ``deque`` для
«живого» хвоста, ``OrderedDict`` для упорядоченного вывода.

Задача — обработать текст и выдать отчёт о частотах слов и биграмм, с
детерминированной сортировкой и отсечением «стоп-слов». Всё — чистыми функциями,
без файловой системы.
"""

from __future__ import annotations

from collections import Counter, OrderedDict, deque, namedtuple
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator

WordCount = namedtuple("WordCount", ["word", "count"])


STOP_WORDS = frozenset(
    {
        "и",
        "в",
        "на",
        "с",
        "по",
        "за",
        "у",
        "а",
        "но",
        "или",
        "то",
        "это",
        "как",
        "так",
        "что",
        "бы",
        "не",
        "при",
        "к",
        "от",
    }
)


def tokenize(text: str) -> list[str]:
    """Разбить текст на слова в нижнем регистре.

    Слова разделяются пробелами; знаки препинания и цифры удаляются.
    ``tokenize("Привет, мир!")`` -> ``["привет", "мир"]``.
    """
    raise NotImplementedError


def word_frequencies(text: str) -> Counter[str]:
    """Вернуть ``Counter`` частот слов без стоп-слов."""
    raise NotImplementedError


def bigram_frequencies(text: str) -> Counter[tuple[str, str]]:
    """Вернуть ``Counter`` частот соседних пар слов (без стоп-слов)."""
    raise NotImplementedError


def top_words(text: str, n: int) -> list[WordCount]:
    """Вернуть top-N самых частых слов в виде ``WordCount``.

    При равенстве частот — по алфавиту. Отсечь стоп-слова.
    """
    raise NotImplementedError


def top_bigrams(text: str, n: int) -> list[tuple[tuple[str, str], int]]:
    """Вернуть top-N биграмм с частотами (та же сортировка)."""
    raise NotImplementedError


def report(text: str, n: int) -> OrderedDict[str, list[WordCount]]:
    """Собрать отчёт: ``{"top_words": [...], "top_bigrams": [...]}``."""
    raise NotImplementedError


def tail(items: Iterable[str], size: int) -> deque[str]:
    """Вернуть ``deque`` с последними ``size`` элементами потока."""
    raise NotImplementedError
