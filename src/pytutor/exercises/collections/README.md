# Набор упражнений по `collections`

20 упражнений от простого к сложному. Каждое упражнение — это модуль-заготовка
в `src/pytutor/exercises/collections/`, автотесты к нему в
`tests/exercises/collections/` и эталон в `solutions/collections/`.

## Как проходить

1. Откройте очередной файл `src/pytutor/exercises/collections/exNN_*.py`.
2. Прочитайте условие в докстринге модуля и функции, реализуйте их.
3. Запустите только это упражнение:

   ```bash
   uv run pytest -k ex01
   ```

4. Добейтесь, чтобы все тесты стали зелёными, и переходите к следующему.

## Полезные команды

```bash
uv run pytest -k ex09     # одно упражнение
uv run pytest             # все упражнения
uv run pytest -x -vv      # остановиться на первой ошибке, подробный вывод
```

## Проверка эталонов

```bash
PYTUTOR_SOLUTION=1 uv run pytest
```

## Список упражнений

| № | Файл | Тема | Уровень |
|---|------|------|---------|
| 1 | `ex01_counter_basics.py` | `Counter`: частота, `most_common`, `total`, `elements` | 1 |
| 2 | `ex02_deque_basics.py` | `deque`: очередь/стек, `appendleft`/`popleft`, `maxlen` | 1 |
| 3 | `ex03_defaultdict_grouping.py` | `defaultdict`: группировка, инвертирование | 2 |
| 4 | `ex04_namedtuple_models.py` | `namedtuple`: `defaults`, `_replace`, `_asdict` | 2 |
| 5 | `ex05_counter_arithmetic.py` | арифметика `Counter`: `+ - & |`, `subtract` | 3 |
| 6 | `ex06_chainmap_layers.py` | `ChainMap`: слои, `new_child`, `parents`, мутации | 3 |
| 7 | `ex07_deque_rotate.py` | `rotate`, `index`, `remove`: кольцо | 3 |
| 8 | `ex08_nested_defaultdict.py` | вложенные `defaultdict`: дерево, автоматические уровни | 4 |
| 9 | `ex09_ordereddict_lru.py` | `OrderedDict`: LRU-кэш, `move_to_end` | 4 |
| 10 | `ex10_counter_topn_ties.py` | top-N с развязкой ничьих | 4 |
| 11 | `ex11_userdict_casefold.py` | `UserDict`: регистронезависимые ключи | 5 |
| 12 | `ex12_deque_window_stats.py` | скользящие статистики на `deque(maxlen=N)` | 5 |
| 13 | `ex13_inverted_counter.py` | инвертированный индекс: `defaultdict` + `Counter` | 5 |
| 14 | `ex14_chainmap_merge.py` | слияние `ChainMap`: `flatten`, отчёт об источниках | 6 |
| 15 | `ex15_counter_multiset_edge.py` | крайние случаи `Counter`: мультимножества | 6 |
| 16 | `ex16_eviction_caches.py` | FIFO / LRU / LFU кэши | 6 |
| 17 | `ex17_event_buckets.py` | временные корзины, потоковая агрегация | 7 |
| 18 | `ex18_custom_mapping.py` | `MutableMapping` с нуля: лог, счётчик обращений | 7 |
| 19 | `ex19_cross_module.py` | связка collections × itertools × functools | 7 |
| 20 | `ex20_capstone_text_analytics.py` | капстоун: конвейер аналитики текста | 8 |

## Подводные камни, которые проверяются

- `Counter` — мультимножество: `+` отбрасывает неположительные итоги, `|` — нет;
- `elements()` игнорирует ключи со счётчиком <= 0;
- `most_common` не гарантирует порядок при равных частотах — нужна своя сортировка;
- мутации `ChainMap` меняют только первый слой;
- `deque(maxlen=N)` автоматически вытесняет старый элемент;
- `OrderedDict.move_to_end` — основа LRU;
- вложенные `defaultdict` требуют аккуратности: `get` не должен создавать узлы;
- `UserDict` безопаснее наследования `dict` для смены семантики ключей.
