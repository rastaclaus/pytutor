"""Эталон упражнения 11: ``asdict`` и ``astuple``."""

from __future__ import annotations

from dataclasses import asdict, astuple, dataclass, field


def declare_models() -> tuple[type, type]:
    @dataclass
    class Point:
        """Точка."""

        x: int
        y: int

    @dataclass
    class Segment:
        """Отрезок между двумя точками."""

        start: Point
        end: Point
        weight: float = 1.0
        labels: list[str] = field(default_factory=list)

    return Point, Segment


def to_dict(obj: object) -> dict:  # type: ignore[type-arg]
    return asdict(obj)  # type: ignore[type-var]


def to_tuple(obj: object) -> tuple:  # type: ignore[type-arg]
    return astuple(obj)  # type: ignore[type-var]


def nested_roundtrip() -> dict:  # type: ignore[type-arg]
    point_cls, segment_cls = declare_models()
    segment = segment_cls(point_cls(0, 0), point_cls(3, 4), 2.5)
    return asdict(segment)


def is_deep_copy() -> bool:
    point_cls, segment_cls = declare_models()
    segment = segment_cls(point_cls(0, 0), point_cls(3, 4), 2.5, ["main"])
    data = asdict(segment)
    data["labels"].append("mutated")
    data["weight"] = 99.0
    return segment.labels == ["main"] and segment.weight == 2.5
