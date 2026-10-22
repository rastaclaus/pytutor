"""Эталон упражнения 20: капстоун: конвейер аналитики текста."""

from __future__ import annotations

from collections import Counter, OrderedDict, deque, namedtuple
from itertools import pairwise
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable

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
    result: list[str] = []
    for word in text.split():
        cleaned = "".join(ch for ch in word if ch.isalpha())
        if cleaned:
            result.append(cleaned.lower())
    return result


def _significant_words(text: str) -> list[str]:
    return [word for word in tokenize(text) if word not in STOP_WORDS]


def word_frequencies(text: str) -> Counter[str]:
    return Counter(_significant_words(text))


def bigram_frequencies(text: str) -> Counter[tuple[str, str]]:
    words = _significant_words(text)
    return Counter(pairwise(words))


def _sorted_top(items: Iterable[tuple[object, int]], n: int) -> list:
    return sorted(items, key=lambda item: (-item[1], str(item[0])))[:n]


def top_words(text: str, n: int) -> list[WordCount]:
    return [WordCount(word, count) for word, count in _sorted_top(word_frequencies(text).items(), n)]


def top_bigrams(text: str, n: int) -> list[tuple[tuple[str, str], int]]:
    return _sorted_top(bigram_frequencies(text).items(), n)


def report(text: str, n: int) -> OrderedDict[str, list[WordCount]]:
    result: OrderedDict[str, list[WordCount]] = OrderedDict()
    result["top_words"] = top_words(text, n)
    result["top_bigrams"] = [WordCount(f"{left} {right}", count) for (left, right), count in top_bigrams(text, n)]
    return result


def tail(items: Iterable[str], size: int) -> deque[str]:
    return deque(items, maxlen=size)
