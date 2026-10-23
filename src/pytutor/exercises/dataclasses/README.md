# Набор упражнений по `dataclasses`

20 упражнений от простого к сложному. Каждое упражнение — это модуль-заготовка
в `src/pytutor/exercises/dataclasses/`, автотесты к нему в
`tests/exercises/dataclasses/` и эталон в `solutions/dataclasses/`.

## Как проходить

1. Откройте очередной файл `src/pytutor/exercises/dataclasses/exNN_*.py`.
2. Прочитайте условие в докстринге модуля и функции/класса, реализуйте их.
3. Запустите только это упражнение:

   ```bash
   uv run pytest -k ex01
   ```

4. Добейтесь, чтобы все тесты стали зелёными, и переходите к следующему.

В отличие от предыдущих наборов, здесь половина работы — **объявить класс с
нужными опциями декоратора**. Условие всегда говорит, какие поля и с какими
опциями нужны; тесты проверяют поведение (сгенерированные методы, ошибки,
`fields()`, `asdict`), а не текст исходника.

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
| 1 | `ex01_basics.py` | `@dataclass`: `__init__`, `__repr__`, `__eq__`, порядок полей | 1 |
| 2 | `ex02_defaults_factories.py` | `field(default=)`, `default_factory`, изменяемые дефолты | 1 |
| 3 | `ex03_frozen.py` | `frozen=True`, `FrozenInstanceError`, авто-`__hash__` | 2 |
| 4 | `ex04_order.py` | `order=True`: сравнения, сортировка, `TypeError` с чужим типом | 2 |
| 5 | `ex05_post_init.py` | `__post_init__`, вычисляемые поля `field(init=False)` | 3 |
| 6 | `ex06_initvar.py` | `InitVar`: параметры только для инициализации | 3 |
| 7 | `ex07_classvar.py` | `ClassVar`: псевдо-поля, общие атрибуты | 3 |
| 8 | `ex08_slots.py` | `slots=True`, отсутствие `__dict__`, `weakref_slot` | 4 |
| 9 | `ex09_kw_only.py` | `kw_only`, `KW_ONLY`, `__match_args__` | 4 |
| 10 | `ex10_replace.py` | `replace()`: копия, повторный `__post_init__` | 4 |
| 11 | `ex11_asdict_astuple.py` | `asdict`/`astuple`: рекурсия, глубокая копия | 4 |
| 12 | `ex12_inheritance.py` | наследование полей, `super().__post_init__()` | 5 |
| 13 | `ex13_custom_eq_repr.py` | `field(repr=, compare=, hash=)`, `unsafe_hash` | 5 |
| 14 | `ex14_fields_metadata.py` | `fields()`, `Field`, `metadata` только для чтения | 6 |
| 15 | `ex15_make_dataclass.py` | `make_dataclass()`: классы во время выполнения | 6 |
| 16 | `ex16_nested.py` | вложенные dataclass, `default_factory` для контейнеров | 6 |
| 17 | `ex17_descriptors.py` | поля-дескрипторы: приведение типа и валидация | 7 |
| 18 | `ex18_constructors.py` | альтернативные конструкторы (`classmethod` + разбор) | 7 |
| 19 | `ex19_deep_model.py` | `frozen` + `slots` + `kw_only`: неизменяемое дерево | 7 |
| 20 | `ex20_capstone.py` | капстоун: модель домена на всех возможностях модуля | 8 |

## Подводные камни, которые проверяются

- `x: list = []` запрещён (`ValueError`), нужен `default_factory`;
- `frozen=True` + `eq=True` даёт `__hash__`, изменяемый dataclass — нет;
- `order=True` без `eq=True` — `ValueError` при объявлении класса;
- `__post_init__` не вызывается, если `__init__` не сгенерирован;
- `InitVar` и `ClassVar` не попадают в `fields()`;
- `slots=True` запрещает новые атрибуты и убирает `__dict__`;
- keyword-only поля не входят в `__match_args__`;
- `replace()` не трогает `init=False`-поля и пересчитывает `__post_init__`;
- `asdict()` делает глубокую копию и падает на не-dataclass;
- поле с дефолтом в базе перед полем без дефолта в наследнике — `TypeError`;
- `metadata` — `MappingProxyType`, менять нельзя.
