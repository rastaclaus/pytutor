"""Тесты упражнения 18: альтернативные конструкторы."""

from __future__ import annotations

import pytest

from pytutor.exercises.dataclasses import ex18_constructors as ex


def test_from_text_with_unit() -> None:
    measurement = ex.parse_measurement("12.5 cm")
    assert measurement.value == 12.5
    assert measurement.unit == "cm"


def test_from_text_without_unit() -> None:
    measurement = ex.parse_measurement("7")
    assert measurement.value == 7.0
    assert measurement.unit == "m"


def test_from_text_empty() -> None:
    with pytest.raises(ValueError):
        ex.parse_measurement("   ")


def test_from_dict() -> None:
    measurement = ex.parse_measurement_dict({"value": 3, "unit": "kg", "extra": 1})
    assert (measurement.value, measurement.unit, measurement.source) == (3.0, "kg", "unknown")


def test_from_dict_requires_value() -> None:
    with pytest.raises(ValueError, match="value"):
        ex.parse_measurement_dict({"unit": "kg"})


def test_serialize() -> None:
    measurement = ex.parse_measurement_dict({"value": 1, "source": "sensor"})
    assert ex.serialize(measurement) == {"value": 1.0, "unit": "m", "source": "sensor"}
