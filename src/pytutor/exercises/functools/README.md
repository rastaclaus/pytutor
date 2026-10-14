# Набор упражнений по `functools`

15 упражнений от простого к сложному. Каждое упражнение — это модуль-заготовка
в `src/pytutor/exercises/functools/`, автотесты к нему в
`tests/exercises/functools/` и эталон в `solutions/functools/`.

## Как проходить

1. Откройте очередной файл `src/pytutor/exercises/functools/exNN_*.py`.
2. Прочитайте условие в докстринге модуля и функции, реализуйте их.
3. Запустите только это упражнение:

   ```bash
   uv run pytest -k ex01
   ```

4. Добейтесь, чтобы все тесты стали зелёными, и переходите к следующему.

Граничные случаи (`[]`, `None`, одинаковые аргументы, повторные вызовы) в тестах
тоже проверяются — читайте сообщения об ошибках.

## Полезные команды

```bash
uv run pytest -k ex05     # одно упражнение
uv run pytest             # все упражнения
uv run pytest -x -vv      # остановиться на первой ошибке, подробный вывод
```

## Проверка эталонов

Чтобы убедиться, что тесты и эталоны согласованы (полезно после правок):

```bash
PYTUTOR_SOLUTION=1 uv run pytest
```

В этом режиме модули заданий подменяются файлами из `solutions/`, поэтому всё
должно быть зелёным. Если тест падает и здесь — ошибка в тесте или эталоне.

## Список упражнений

| № | Файл | Тема | Уровень |
|---|------|------|---------|
| 1 | `ex01_reduce_basics.py` | `reduce`: произведение, конкатенация, сумма с `initial` | 1 |
| 2 | `ex02_reduce_aggregation.py` | `reduce`: flatten, частоты, самое частое, `group_by` | 2 |
| 3 | `ex03_partial_basics.py` | `partial`: фиксация аргументов, `map` + `partial` | 2 |
| 4 | `ex04_partial_pipeline.py` | `compose`/`pipeline` на `reduce` + `partial`, `partialmethod` | 3 |
| 5 | `ex05_wraps_identity.py` | зачем нужен `wraps`, `__wrapped__` | 3 |
| 6 | `ex06_decorator_with_args.py` | декораторы с аргументами: `repeat`, `retry` | 4 |
| 7 | `ex07_lru_cache_basics.py` | `lru_cache`/`cache`: Фибоначчи, Каталан | 4 |
| 8 | `ex08_lru_cache_edge.py` | `maxsize`, `typed`, `cache_info`, eviction | 5 |
| 9 | `ex09_cached_property.py` | `cached_property`: ленивое свойство, инвалидация | 5 |
| 10 | `ex10_total_ordering.py` | `total_ordering`: одна пара сравнений — все шесть | 5 |
| 11 | `ex11_cmp_to_key.py` | `cmp_to_key`: компараторы, естественная сортировка | 6 |
| 12 | `ex12_singledispatch.py` | обобщённая функция по типу + регистрация | 6 |
| 13 | `ex13_singledispatchmethod.py` | диспетчеризация методов по типу аргумента | 7 |
| 14 | `ex14_memoize_own.py` | свой `memoize` на `wraps` + `dict`, ключ из подписи | 7 |
| 15 | `ex15_capstone.py` | конвейер: `retry` + `cache` + `partial` + `reduce` | 8 |
