"""Эталон упражнения 18: альтернативные конструкторы."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Mapping


def declare_measurement() -> type:
    @dataclass
    class Measurement:
        """Измерение с единицей и источником."""

        value: float
        unit: str = "m"
        source: str = field(default="unknown")

        @classmethod
        def from_dict(cls, data: Mapping[str, Any]) -> Measurement:
            if "value" not in data:
                raise ValueError("в словаре отсутствует поле value")
            return cls(
                value=float(data["value"]),
                unit=data.get("unit", "m"),
                source=data.get("source", "unknown"),
            )

        @classmethod
        def from_text(cls, text: str) -> Measurement:
            parts = text.split()
            if not parts:
                raise ValueError("пустая строка")
            if len(parts) == 1:
                return cls(value=float(parts[0]))
            return cls(value=float(parts[0]), unit=parts[1])

    return Measurement


def parse_measurement(text: str) -> object:
    return declare_measurement().from_text(text)


def parse_measurement_dict(data: Mapping[str, Any]) -> object:
    return declare_measurement().from_dict(data)


def serialize(measurement: object) -> dict:  # type: ignore[type-arg]
    return {
        "value": measurement.value,  # type: ignore[attr-defined]
        "unit": measurement.unit,  # type: ignore[attr-defined]
        "source": measurement.source,  # type: ignore[attr-defined]
    }
