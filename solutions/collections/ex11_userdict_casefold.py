"""Эталон упражнения 11: ``UserDict`` — свой словарь с другой семантикой."""

from __future__ import annotations

from collections import UserDict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable


class CaseInsensitiveDict(UserDict[str, int]):
    def __getitem__(self, key: str) -> int:
        return self.data[key.casefold()]

    def __setitem__(self, key: str, value: int) -> None:
        self.data[key.casefold()] = value

    def __delitem__(self, key: str) -> None:
        del self.data[key.casefold()]

    def __contains__(self, key: object) -> bool:
        if not isinstance(key, str):
            return False
        return key.casefold() in self.data


def count_case_insensitive(words: Iterable[str]) -> dict[str, int]:
    counter: CaseInsensitiveDict = CaseInsensitiveDict()
    display: dict[str, str] = {}
    for word in words:
        folded = word.casefold()
        if folded not in counter:
            display[folded] = word
            counter[word] = 0
        counter[word] += 1
    return {display[key]: count for key, count in counter.items()}
