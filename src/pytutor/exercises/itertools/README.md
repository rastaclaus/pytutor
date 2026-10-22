# Набор упражнений по `itertools`

15 упражнений от простого к сложному. Каждое упражнение — это модуль-заготовка
в `src/pytutor/exercises/itertools/`, автотесты к нему в
`tests/exercises/itertools/` и эталон в `solutions/itertools/`.

## Как проходить

1. Откройте очередной файл `src/pytutor/exercises/itertools/exNN_*.py`.
2. Прочитайте условие в докстринге модуля и функции, реализуйте их.
3. Запустите только это упражнение:

   ```bash
   uv run pytest -k ex01
   ```

4. Добейтесь, чтобы все тесты стали зелёными, и переходите к следующему.

Все упражнения работают с **итераторами**, а не со списками: вход может быть
бесконечным, одноразовым или ленивым. Если решение материализует поток целиком
там, где этого не требуется, тест это заметит (счётчики потребления в тестах).

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

В этом режиме модули заданий подменяются файлами из `solutions/`, поэтому всё
должно быть зелёным. Если тест падает и здесь — ошибка в тесте или эталоне.

## Список упражнений

| № | Файл | Тема | Уровень |
|---|------|------|---------|
| 1 | `ex01_count_repeat_cycle.py` | `count`, `repeat`, `cycle` + `islice` | 1 |
| 2 | `ex02_chain_flatten.py` | `chain`, `chain.from_iterable`, `flatten` | 2 |
| 3 | `ex03_islice_slices.py` | `islice`: срезы итераторов, `nth`, потребление | 2 |
| 4 | `ex04_take_drop_filter.py` | `takewhile`, `dropwhile`, `filterfalse`, `compress` | 3 |
| 5 | `ex05_accumulate.py` | `accumulate`: бегущие итоги, `initial` | 3 |
| 6 | `ex06_starmap_zip_args.py` | `starmap`, `repeat`, `functools.partial` | 3 |
| 7 | `ex07_zip_longest_strict.py` | `zip_longest`, `zip(strict=True)`, `grouper` | 4 |
| 8 | `ex08_pairwise_window.py` | `pairwise`, скользящее окно на `deque` | 4 |
| 9 | `ex09_groupby.py` | `groupby`: серии, `unique_justseen`, сортировка | 5 |
| 10 | `ex10_tee.py` | `tee`: независимые проходы, peek, lookahead | 5 |
| 11 | `ex11_batched_grouper.py` | `batched(strict=)`, `grouper`, `reshape` | 5 |
| 12 | `ex12_combinatorics.py` | `product`, `permutations`, `combinations*`, `powerset` | 6 |
| 13 | `ex13_iterator_protocol.py` | одноразовость, ленивость, `iter(callable, sentinel)` | 6 |
| 14 | `ex14_recipes.py` | рецепты: `sliding_window`, `running_mean`, `sum_of_squares` | 7 |
| 15 | `ex15_capstone.py` | ленивый ETL: разбор → батчи → агрегация | 8 |

## Подводные камни, которые проверяются

- итератор одноразовый: `sum(it)`, `list(it)`, `for` опустошают его;
- `groupby` группирует только подряд идущие элементы и «гасит» предыдущую группу;
- в `islice` нет отрицательных индексов;
- `takewhile` теряет элемент, на котором предикат впервые провалился;
- `zip` молчит про разную длину, а `zip(strict=True)` падает;
- `tee` буферизует прочитанное, если копии читаются неравномерно;
- `batched(strict=True)` падает на неполном хвосте.
