"""Упражнение 2 (boss). Агрегация потока событий доставки. Уровень 7.

Сценарий: сервер доставки пишет события вида ``(courier, event_type, amount)``.
Типы: ``"pickup"``, ``"deliver"``, ``"cancel"``. Из потока нужно собрать
статистику курьеров.

Реализуйте:

* ``validate_event(event)`` — кортеж из трёх строк; если тип не входит в
  ``EVENT_TYPES``, бросить ``ValueError`` (в сообщении есть ``event_type``).

* ``courier_totals(events)`` — ``defaultdict``-словарь «курьер -> сумма
  по доставкам минус отмены» (``deliver`` прибавляет, ``cancel`` вычитает,
  ``pickup`` игнорируется). Порядок ключей — по первому появлению.

* ``events_by_type(events)`` — ``Counter`` по типам событий.

* ``top_couriers(events, n)`` — топ-N курьеров по итоговой сумме из
  ``courier_totals``: по убыванию суммы, при равенстве — по алфавиту имени.
  Возвращает список кортежей ``(курьер, сумма)``.

* ``window_counts(events, window)`` — сколько событий каждого типа попало
  в скользящее окно последних ``window`` событий потока (учитывать порядок):
  ``dict[тип, Counter]`` — слишком громоздко; верните ``Counter`` по типам
  в пределах последних ``window`` событий. ``window <= 0`` ->
  ``ValueError`` (в сообщении есть ``window``).

* ``busy_courier(events)`` — курьер с наибольшим числом событий; при равенстве —
  встретившийся раньше; для пустого потока — ``None``.

Термины: **поток** может быть генератором — материализовать его дважды нельзя;
если функция нужна дважды, материализуйте список один раз внутри.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable

EVENT_TYPES = frozenset({"pickup", "deliver", "cancel"})


def validate_event(event: tuple[str, str, int]) -> None:
    """Проверить тип события; неизвестный тип — ``ValueError`` (``event_type``)."""
    raise NotImplementedError


def courier_totals(events: Iterable[tuple[str, str, int]]) -> dict[str, int]:
    """Курьер -> сумма доставок минус отмены; ``pickup`` игнорируется."""
    raise NotImplementedError


def events_by_type(events: Iterable[tuple[str, str, int]]) -> Counter[str]:
    """``Counter`` по типам событий."""
    raise NotImplementedError


def top_couriers(events: Iterable[tuple[str, str, int]], n: int) -> list[tuple[str, int]]:
    """Топ-N курьеров по сумме; ничья — по алфавиту."""
    raise NotImplementedError


def window_counts(events: Iterable[tuple[str, str, int]], window: int) -> Counter[str]:
    """Частоты типов в последних ``window`` событиях; ``window <= 0`` -> ``ValueError``."""
    raise NotImplementedError


def busy_courier(events: Iterable[tuple[str, str, int]]) -> str | None:
    """Курьер с наибольшим числом событий; ничья — первый встретившийся."""
    raise NotImplementedError
