"""Упражнение 17. Временные корзины: агрегация потоков событий. Уровень 7.

События приходят потоком: ``(время, метка)``. Их группируют в «корзины»
(buckets) — одинаковые интервалы времени — и для каждой корзины считают счётчики
меток. Это основа любого мониторинга: количество запросов в секунду/минуту.

Мы реализуем агрегацию по корзинам и потоковую версию, которая не держит в памяти
весь поток: достаточно хвоста из ``deque``.
"""

from __future__ import annotations

from collections import Counter, deque
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable, Iterator


Event = tuple[int, str]  # (время, метка)


def bucket_size(events: Iterable[Event], bucket: int) -> Counter[int]:
    """Вернуть ``Counter``: номер корзины -> число событий в ней.

    Номер корзины для времени ``t`` — ``t // bucket``. События с ``t < 0``
    игнорировать. Для ``bucket <= 0`` — ``ValueError``.
    """
    raise NotImplementedError


def bucket_labels(events: Iterable[Event], bucket: int) -> dict[int, list[str]]:
    """Сгруппировать метки событий по корзинам.

    Вернуть ``defaultdict``/обычный словарь: номер корзины -> список меток в
    порядке появления.
    """
    raise NotImplementedError


def top_labels_per_bucket(events: Iterable[Event], bucket: int) -> dict[int, list[tuple[str, int]]]:
    """Для каждой корзины вернуть топ-3 метки с частотами.

    Частоты — по убыванию, при равенстве — по алфавиту. Используйте ``Counter``
    и ``top_n``-логику.
    """
    raise NotImplementedError


def stream_buckets(events: Iterable[Event], bucket: int, window: int) -> Iterator[Counter[int]]:
    """Потоково выдавать счётчики корзин по мере прихода событий.

    Генератор возвращает ``Counter`` активных корзин после **каждого** события,
    но хранит не более ``window`` последних корзин (хвост через ``deque``).
    События вне ``window`` последних корзин вытесняются.
    """
    raise NotImplementedError
