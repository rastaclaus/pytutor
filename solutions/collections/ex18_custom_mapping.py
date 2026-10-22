"""Эталон упражнения 18: ``collections.abc.MutableMapping`` — свой словарь с нуля."""

from __future__ import annotations

from collections.abc import Iterator, MutableMapping


class LoggingDict(MutableMapping[str, int]):
    def __init__(self) -> None:
        self._data: dict[str, int] = {}
        self.log: list[str] = []

    def __getitem__(self, key: str) -> int:
        self.log.append(f"get:{key}")
        return self._data[key]

    def __setitem__(self, key: str, value: int) -> None:
        self.log.append(f"set:{key}={value}")
        self._data[key] = value

    def __delitem__(self, key: str) -> None:
        self.log.append(f"del:{key}")
        del self._data[key]

    def __iter__(self) -> Iterator[str]:
        return iter(self._data)

    def __len__(self) -> int:
        return len(self._data)


class AccessCountingDict(MutableMapping[str, int]):
    def __init__(self, initial: dict[str, int] | None = None) -> None:
        self._data: dict[str, int] = dict(initial or {})
        self.access: dict[str, int] = {}

    def __getitem__(self, key: str) -> int:
        self.access[key] = self.access.get(key, 0) + 1
        return self._data[key]

    def __setitem__(self, key: str, value: int) -> None:
        self._data[key] = value

    def __delitem__(self, key: str) -> None:
        del self._data[key]
        self.access.pop(key, None)

    def __iter__(self) -> Iterator[str]:
        return iter(self._data)

    def __len__(self) -> int:
        return len(self._data)

    def most_accessed(self, n: int) -> list[tuple[str, int]]:
        return sorted(self.access.items(), key=lambda item: (-item[1], item[0]))[:n]
