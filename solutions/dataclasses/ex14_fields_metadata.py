"""Эталон упражнения 14: интроспекция полей."""

from __future__ import annotations

from dataclasses import MISSING, dataclass, field, fields


def declare_column() -> type:
    @dataclass
    class Column:
        """Описание колонки таблицы."""

        name: str = field(metadata={"primary_key": True})
        kind: str = field(default="text", metadata={"nullable": True})
        size: int = 0

    return Column


def field_names() -> list[str]:
    return [item.name for item in fields(declare_column())]


def primary_key_names() -> list[str]:
    return [item.name for item in fields(declare_column()) if item.metadata.get("primary_key")]


def fields_without_default() -> list[str]:
    return [
        item.name for item in fields(declare_column()) if item.default is MISSING and item.default_factory is MISSING
    ]


def metadata_is_read_only() -> bool:
    metadata = fields(declare_column())[0].metadata
    try:
        metadata["primary_key"] = False  # type: ignore[index]
    except TypeError:
        return True
    return False
