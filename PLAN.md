# План тренажёра `pytutor`

## План: набор `dataclasses` (сдан)

Цель — 20 упражнений уровней 1–8 по `dataclasses`, формат как у предыдущих
наборов: заготовка с условием в докстринге, тесты, эталон, сброс из `stubs/`.

Принятые решения:

- **Объём:** 20 упражнений — модуль богат опциями, есть материал на все уровни.
- **Интеграция с `typing` не включается:** `Generic`/`TypeVar` остаются темой
  отдельного набора.
- **Капстоун — модель домена:** неизменяемые сущности, агрегат, `ClassVar`-журнал,
  цепочка `replace`.
- **Ориентир — документация Python 3.14** (`field(doc=)` появился в 3.14;
  `slots`, `kw_only`, `KW_ONLY`, `weakref_slot` — 3.10/3.11). На поведение 3.15
  (`frozendict` в `metadata`, `sentinel`) не опираемся.

Состав: основы и генерация методов → дефолты и фабрики → `frozen` → `order` →
`__post_init__` → `InitVar` → `ClassVar` → `slots` → `kw_only` → `replace` →
`asdict`/`astuple` → наследование → `repr`/`compare`/`hash` → `fields()` и
`metadata` → `make_dataclass` → вложенность → дескрипторы → альтернативные
конструкторы → неизменяемое дерево → капстоун.

Критерии готовности выполнены: `PYTUTOR_SOLUTION=1 uv run pytest` — 444 passed;
`uv run pytest` падает только на `NotImplementedError`; `ruff check .` и
`ruff format --check .` чистые; сброс из `stubs/` идемпотентен.

## План: набор `itertools`

Продолжение тренажёра `pytutor` после набора `functools`. Цель — 15 упражнений
уровней 1–8 по `itertools` в том же формате: заготовка с условием в докстринге,
автотесты, эталон, возможность сброса из `stubs/`.

## Принятые решения

- **Модуль:** `itertools` — прямое продолжение `functools` (функции над функциями →
  ленивые потоки), полностью укладывается в текущий харнесс: чистые функции,
  проверка через `list(...)`, без I/O и таймингов.
- **Объём:** 15 упражнений, уровни 1–8 — как в `functools`.
- **Python 3.14:** используем современные API — `batched(..., strict=True)` (3.13),
  `pairwise` (3.10), встроенный `zip(strict=True)` (3.10). Устаревшие рецепты не берём.
- **Острые углы важнее охвата:** тесты проверяют не только результат, но и
  одноразовость итераторов, `groupby` на несортированных данных, отсутствие
  отрицательных индексов в `islice`, вытеснение в `tee`/`deque`.
- **`operator`** не выносим отдельным набором (мало материала) — используем как
  вспомогательный модуль в упражнениях и в капстоуне.

## Что появится в репозитории

```
src/pytutor/exercises/itertools/
├── __init__.py
├── README.md                     # оглавление набора, как у functools
└── ex01_*.py … ex15_*.py         # условия в докстрингах, тела — NotImplementedError

stubs/itertools/ex01_*.py … ex15_*.py     # копии для scripts/reset_exercises.py
tests/exercises/itertools/test_ex01_*.py … test_ex15_*.py
solutions/itertools/ex01_*.py … ex15_*.py
```

Дополнительно: строка про `itertools` в таблице «Наборы упражнений» корневого
`README.md`. `scripts/reset_exercises.py` править не нужно — он обходит каталоги
`stubs/*` динамически.

## Состав набора

| № | Файл | Тема | Новые инструменты | Ур. |
|---|------|------|-------------------|-----|
| 1 | `ex01_count_repeat_cycle.py` | Счётчики и повторы, обрезка `islice` | `count`, `repeat`, `cycle`, `islice` | 1 |
| 2 | `ex02_chain_flatten.py` | Объединение потоков и `flatten` | `chain`, `chain.from_iterable` | 2 |
| 3 | `ex03_islice_slices.py` | Срезы итераторов, потребление, `nth` с default | `islice` | 2 |
| 4 | `ex04_take_drop_filter.py` | Условные префиксы и фильтры | `takewhile`, `dropwhile`, `filterfalse`, `compress` | 3 |
| 5 | `ex05_accumulate.py` | Бегущие итоги | `accumulate` (`func`, `initial`) | 3 |
| 6 | `ex06_starmap_zip_args.py` | Аргументы «уже сплюснуты» в кортежи | `starmap`, `repeat`, `functools.partial` | 3 |
| 7 | `ex07_zip_longest_strict.py` | Неравные длины и `strict` | `zip_longest`, `zip(strict=True)` | 4 |
| 8 | `ex08_pairwise_window.py` | Соседние пары и скользящее окно | `pairwise`, `deque(maxlen=)` | 4 |
| 9 | `ex09_groupby.py` | Серии, `unique_justseen`, требование сортировки | `groupby` | 5 |
| 10 | `ex10_tee.py` | Независимые проходы, peek/lookahead, цена памяти | `tee` | 5 |
| 11 | `ex11_batched_grouper.py` | Батчи и `grouper`, `reshape` матрицы | `batched(strict=)`, `zip_longest` | 5 |
| 12 | `ex12_combinatorics.py` | Комбинаторика и `powerset` | `product`, `permutations`, `combinations*`, `math.comb` | 6 |
| 13 | `ex13_iterator_protocol.py` | Ленивость, одноразовость, sentinel-итератор | `iter`, `next`, `iter(callable, sentinel)` | 6 |
| 14 | `ex14_recipes.py` | Рецепты из документации | `sliding_window`, `running_mean`, `sum_of_squares` | 7 |
| 15 | `ex15_capstone.py` | Ленивый ETL по лог-строкам | всё вместе + `partial` | 8 |

### Ключевые проверки по упражнениям

1. Бесконечные источники обязательно обрезаются `islice`; `repeat(x, n)` конечен.
2. `flatten` — один уровень вложенности; пустой вход; генератор, а не список.
3. `drop` реально потребляет исходный итератор; `nth` не падает на коротком входе;
   `islice` с отрицательным индексом — `ValueError`.
4. `takewhile`/`dropwhile` останавливаются на первом провале (элемент теряется);
   `compress` обрывается по короткому `selectors`.
5. `initial` добавляет элемент; `accumulate(..., max)` — бегущий максимум.
6. `starmap` vs `map`; `repeat` как поставщик константы; `partial` для фиксации.
7. `zip_longest` с `fillvalue`; `zip(strict=True)` даёт `ValueError` на разной длине.
8. `pairwise` теряет первый элемент и пуст на входе < 2; окно через `deque(maxlen)`.
9. `groupby` на несортированном входе даёт «рваные» группы; предыдущая группа
   недействительна после перехода — сохраняем `list(g)`; пустой вход.
10. `tee` даёт независимые итераторы; peek через `tee(it, 1)`; проверка, что
    проход по одной копии не мешает другой.
11. `batched` с неполным хвостом; `strict=True` → `ValueError`; `n < 1` → `ValueError`.
12. `permutations` vs `combinations` vs `combinations_with_replacement`;
    `powerset` в порядке возрастания длины; сверка количества с `math.comb`.
13. `sum(it)` опустошает; повторный `list(it)` пуст; `iter(callable, sentinel)`
    останавливается на сентинеле; ленивость через счётчик вызовов.
14. `sliding_window` через `deque`; `running_mean` через `accumulate` + `count`;
    `sum_of_squares` через `tee` + `sumprod`.
15. Пайплайн: чтение строк → фильтр → `batched` → `groupby` → `accumulate`;
    проверка, что до `list()` ничего не вычисляется (счётчик вызовов парсера).

## Порядок работ

1. Создать `src/pytutor/exercises/itertools/` с `__init__.py`, `README.md` и
   заготовками `ex01…ex15` (докстринг-условие + `raise NotImplementedError`).
2. Написать `tests/exercises/itertools/` — по одному файлу на упражнение,
   включая граничные случаи из таблицы выше.
3. Написать `solutions/itertools/` — эталоны.
4. Скопировать заготовки в `stubs/itertools/`.
5. Обновить корневой `README.md` (строка набора).
6. Прогнать `PYTUTOR_SOLUTION=1 uv run pytest` — всё зелёное.
7. Прогнать `uv run pytest -q` — падает ровно на `NotImplementedError`.
8. `ruff check .` и `ruff format --check .` — чисто.

## Критерии готовности

- 15 упражнений, уровни 1–8, каждый файл содержит связное условие и подсказки.
- Тесты детерминированные, быстрые, без сети, файловой системы и `sleep`.
- `PYTUTOR_SOLUTION=1 uv run pytest` — 100% зелёный.
- `uv run python scripts/reset_exercises.py -m itertools` работает идемпотентно.
- Линтер и форматтер довольны.

## Технический долг (закрыт)

Ревью репозитория после сдачи набора `itertools` показало: сам набор чистый, но
остальной репозиторий разошёлся с текущей версией Ruff (0.17). Было: 56 ошибок
`ruff check .` и 12 неформатированных файлов, все — вне `itertools`.

Как закрыли:

1. **Зелёный линт.** `ruff format .` + точечные правки; правила, конфликтующие с
   учебным стилем, осознанно внесены в `ignore`/`per-file-ignores` с
   комментариями (`D203`, `UP047`, `EM101/EM102`, `TRY003`, `PT011`, `RUF001`,
   `TD002/TD003/FIX002`, `S101`, `PLR2004`, `PLW1641`). Сейчас `ruff check .` и
   `ruff format --check .` чистые.
2. **Обёртка.** `src/pytutor/__init__.py` стал CLI: `pytutor` показывает наборы,
   `pytutor <набор>` — файлы набора. Описание в `pyproject.toml` поправлено.
3. **Рубрика уровней 1–8** добавлена в корневой `README.md`.
4. **Тест на харнесс.** `tests/test_harness.py` собирает временный мини-репозиторий
   и проверяет, что заглушка падает, а `PYTUTOR_SOLUTION=1` подменяет модуль
   эталоном (не зависит от того, решены ли реальные упражнения).

CI (GitHub Actions) — пока отложен; вернуться, когда понадобится защита от
регрессий при добавлении наборов.

## Сданные наборы

- `dataclasses` — 20 упражнений (уровни 1–8): `@dataclass` и его опции
  (`frozen`, `order`, `slots`, `kw_only`, `unsafe_hash`), `field()` с
  `default_factory`/`repr`/`compare`/`metadata`, `__post_init__`, `InitVar`,
  `ClassVar`, наследование, `replace`, `asdict`/`astuple`, `fields()`,
  `make_dataclass`, поля-дескрипторы, альтернативные конструкторы,
  неизменяемое дерево и капстоун по модели домена.
- `itertools` — 15 упражнений (уровни 1–8).
- `functools` — 15 упражнений (уровни 1–8).
- `collections` — 20 упражнений (уровни 1–8): `Counter`, `deque`,
  `defaultdict`, `namedtuple`, `ChainMap`, `OrderedDict`, `UserDict`,
  `MutableMapping`, вложенные структуры, кэши, кросс-наборная связка и капстоун
  по аналитике текста.

## Дальше по очереди

`typing` → `re` → `pathlib` → `contextlib`
→ `logging` / `unittest.mock` → `concurrent.futures`.

Порядок — по убыванию практической пользы и объёму материала:

- `typing` — дженерики, `TypeVar`, `Protocol`, `overload`; материал для верхних
  уровней;
- `re` — объёмный и практичный;
- `pathlib` — обязателен для любого продакшн-кода;
- `contextlib` — менеджеры контекста, `contextmanager`, `ExitStack`; небольшой,
  но яркий набор;
- `logging` / `unittest.mock` — фундаментальны, но требуют аккуратности с I/O:
  возможно, придётся разрешить `tmp_path`/`caplog` и смягчить правило «без
  файловой системы»;
- `concurrent.futures` — финальный капстоун-набор.

Бонус-идеи (не блокируют дорожную карту): кросс-наборный капстоун
(`functools` × `itertools`, частично уже есть в `ex15_capstone.py`);
`asyncio` — в долгую перспективу.
