"""Тесты упражнения 20: капстоун — конвейер аналитики текста."""

from __future__ import annotations

from collections import OrderedDict, deque

from pytutor.exercises.collections import ex20_capstone_text_analytics as ex

TEXT = "Шла Маша по шоссе и сосала сушку, а потом Маша шла по парку и сосала сушку опять."


def test_tokenize() -> None:
    assert ex.tokenize("Привет, мир!") == ["привет", "мир"]
    assert ex.tokenize("  Абв 123 гд!") == ["абв", "гд"]


def test_word_frequencies_excludes_stop_words() -> None:
    freqs = ex.word_frequencies("и в на как что")
    assert freqs == OrderedDict()
    freqs = ex.word_frequencies("кот и пёс и кот")
    assert freqs == OrderedDict([("кот", 2), ("пёс", 1)])


def test_bigram_frequencies() -> None:
    bigrams = ex.bigram_frequencies("дом кот дом кот")
    assert bigrams[("дом", "кот")] == 2
    assert bigrams[("кот", "дом")] == 1


def test_top_words() -> None:
    top = ex.top_words(TEXT, 3)
    assert top[0].word == "маша"
    assert top[0].count == 2
    assert top[1].word == "сосала"
    assert top[2].word == "сушку"
    assert all(isinstance(item, ex.WordCount) for item in top)


def test_top_words_tie_break() -> None:
    top = ex.top_words("x y x z y", 3)
    assert top == [
        ex.WordCount("x", 2),
        ex.WordCount("y", 2),
        ex.WordCount("z", 1),
    ]


def test_top_bigrams() -> None:
    bigrams = ex.top_bigrams(TEXT, 2)
    assert bigrams[0][1] == 2
    assert bigrams[0][0] == ("сосала", "сушку")


def test_report() -> None:
    result = ex.report(TEXT, 2)
    assert isinstance(result, OrderedDict)
    assert list(result) == ["top_words", "top_bigrams"]
    assert len(result["top_words"]) == 2
    assert len(result["top_bigrams"]) == 2


def test_tail() -> None:
    result = ex.tail(iter(["a", "b", "c", "d"]), 2)
    assert isinstance(result, deque)
    assert list(result) == ["c", "d"]
    assert list(ex.tail(iter(["a"]), 5)) == ["a"]
