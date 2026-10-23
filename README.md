# pytutor

Тренажёр по модулям стандартной библиотеки Python: наборы упражнений от простого к
сложному с автопроверкой через `pytest`.

Каждый набор — это подпакет в `src/pytutor/exercises/<модуль>/`. К упражнениям
идут тесты в `tests/exercises/<модуль>/`, эталонные решения в `solutions/<модуль>/`
и исходные заготовки в `stubs/<модуль>/`.

## Быстрый старт

```bash
uv sync                 # установить зависимости (в т.ч. pytest)
uv run pytest -k ex01   # прогнать одно упражнение
uv run pytest           # прогнать все упражнения
```

Изначально все тесты падают с `NotImplementedError` — это ожидаемо. Открывайте
файл упражнения, читайте условие в докстринге, реализуйте функции, пока тесты не
станут зелёными.

CLI для навигации по наборам:

```bash
uv run pytutor              # список наборов и число упражнений
uv run pytutor itertools    # файлы одного набора
```

## Уровни сложности

Все наборы используют одну шкалу. Уровень указан в докстринге модуля
упражнения — он говорит, сколько «слоёв» нужно удержать в голове сразу.

| Уровень | Что требуется | Пример |
|---------|---------------|--------|
| 1 | одна функция из API, один прямой вызов | `count` + `islice` |
| 2 | две функции вместе или простая трансформация | `chain`, `islice`-срезы |
| 3 | настройка поведения (аргумент-функция, флаг) | `accumulate(func=)` |
| 4 | граничные случаи и режимы | `zip(strict=True)` |
| 5 | неочевидная семантика объекта | `groupby`, `tee` |
| 6 | комбинация нескольких инструментов | `singledispatch`, `powerset` |
| 7 | самостоятельная реализация идеи модуля | свой `memoize` |
| 8 | многостадийный конвейер из всего набора | ленивый ETL |

Уровни не про количество кода, а про количество ловушек: на уровне 1 ошибка
видна сразу, на уровне 8 сначала надо правильно собрать конвейер.

## Наборы упражнений

| Модуль | Упражнений | Оглавление |
|--------|-----------|------------|
| `functools` | 15 | [src/pytutor/exercises/functools/README.md](src/pytutor/exercises/functools/README.md) |
| `itertools` | 15 | [src/pytutor/exercises/itertools/README.md](src/pytutor/exercises/itertools/README.md) |
| `collections` | 20 | [src/pytutor/exercises/collections/README.md](src/pytutor/exercises/collections/README.md) |
| `dataclasses` | 20 | [src/pytutor/exercises/dataclasses/README.md](src/pytutor/exercises/dataclasses/README.md) |

## Проверка эталонов

Чтобы убедиться, что тесты согласованы с эталонами (все тесты зелёные):

```bash
PYTUTOR_SOLUTION=1 uv run pytest
```

В этом режиме `tests/conftest.py` подменяет модули заданий реализациями из
`solutions/`.

## Сброс к исходному виду

Чтобы вернуть все упражнения к заготовкам (затереть свои решения), есть скрипт:

```bash
uv run python scripts/reset_exercises.py              # все наборы
uv run python scripts/reset_exercises.py -m functools # один набор
uv run python scripts/reset_exercises.py -m functools -e ex04
```

Он просто копирует заготовки из `stubs/<модуль>/` поверх
`src/pytutor/exercises/<модуль>/`. Скрипт идемпотентен — его можно запускать в
любой момент, в том числе повторно. «Данные» (заранее реализованные в рамках
упражнения) функции и классы сохранены в заготовках и не затираются.

## Структура

```
src/pytutor/exercises/<module>/   # задания (текущее состояние, вы их решаете)
stubs/<module>/                   # исходные заготовки для сброса
tests/exercises/<module>/         # автотесты
solutions/<module>/               # эталонные решения
scripts/reset_exercises.py        # сброс упражнений из stubs/
tests/conftest.py                 # переключение «задание / эталон»
tests/test_harness.py             # проверка самого переключения
```
