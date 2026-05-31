# runtime/ — Контракт времени выполнения вики

Единый источник истины о структурной корректности вики. YAML в `schema/` и `policy/` — контракт; `loader.py` — Python API доступа, используемый `tools/lint.py` и `tools/research_wiki.py`. **Шаг кодогенерации отсутствует** — правишь YAML, перезапускаешь инструмент.

## Структура папок

```
runtime/
├── __init__.py     помечает runtime/ как Python-пакет
├── loader.py       API доступа к схеме (импортируется tools/lint.py + research_wiki.py)
├── schema/         контракт форм данных (4 YAML-файла)
├── policy/         контроль доступа (writers.yaml)
└── templates/      скелеты тела страницы по типу сущности, используемые /init и /ingest
```

## Как добавлять

Каждое изменение ниже — **только YAML, ноль изменений Python**. Правишь, сохраняешь, готово.

### Сущности (`schema/entities.yaml` + `templates/`)

- **Новый тип сущности** — добавь блок верхнего уровня (`<kind>:` с `dir`, `fields`, опционально `lifecycle`, опционально `terminal: true`) и создай `templates/<kind>.md.tmpl` со скелетом тела страницы.
- **Новое поле на сущности** — добавь под `fields:` этого типа с `type` + опционально `required` / `default` / `range` / `values` / `to`.
- **Новое условно-обязательное правило** — укажи `required_when: { other_field: value }` на поле. `lint` проверяет автоматически.
- **Новое состояние или переход жизненного цикла** — отредактируй карту `lifecycle.transitions:` сущности. `research_wiki.py transition` проверяет автоматически.

### Рёбра (`schema/edges.yaml`)

- **Новый тип ребра** — добавь блок верхнего уровня с `endpoints`, `direction` (`directed | symmetric`), `workflow`, `attributes`.
- **Новый атрибут на ребре** — добавь под `attributes:` этого типа с `type` + опционально `required` / `values`. `add-edge` собирает, `lint` проверяет.
- **Другое место хранения** — укажи в `conventions.yaml::edge_storage::exceptions` (по умолчанию — `wiki/graph/edges.jsonl`).

### Перекрёстные ссылки (`schema/xref.yaml`)

- **Новое правило прямой → обратной ссылки** — добавь в `rules:` блок `forward` (`kind` + одно из `frontmatter_field` / `body_section` / `edge_type`, плюс `target`) и блок `reverse` (`kind` + `frontmatter_field` или `body_section`, плюс `action: append_slug | append_record`). `lint` проверяет автоматически.

### Контроль доступа (`policy/writers.yaml`)

- **Ограничь, кто пишет поле** — добавь `<kind>.<field>: { writers: [skill1, skill2] }` в `fields:`. Добавь `frozen_after_first_write: true`, если поле нельзя изменять после создания.
- **Ограничь, кто пишет тип ребра** — добавь `<edge_type>: [skill1, skill2]` в `edges:`.

### Соглашения (`schema/conventions.yaml`)

- **Изменить правило slug, грамматику лога, зоны владения** — отредактируй соответствующий ключ верхнего уровня.

## Когда изменения Python НУЖНЫ

Только при расширении **самого языка схемы**, а не при добавлении данных:

- Новый тип поля (например, `list_date`, `tuple_str`) — расширь `loader.py::_valid_values_for`
- Новое действие xref (например, `replace_slug` вместо `append_slug`) — расширь `lint.py::_has_reverse`
- Новая сквозная утилита (например, `edge_supports_evidence_search`) — добавь в `loader.py`

## Вне области действия

- Промпты скиллов и логика рабочих процессов — `.claude/skills/<skill>/`
- Критичность lint'а / политика авто-исправления — выводится из `required` / `default` в схеме
- История миграций — git log + одноразовые скрипты; папка `migrations/` не предусмотрена
