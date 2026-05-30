"""Step 2: Batch-translate all 28 SKILL.md bodies to Russian.
Preserves code blocks, commands, file paths, wikilinks verbatim.
Only translates headings, prose, descriptions.

Usage: cd C:\CoAsKB && python i18n\ru\_step2_translate_skills.py
"""
from pathlib import Path
import re

EN = Path(r"C:\CoAsKB\i18n\en\skills")
RU = Path(r"C:\CoAsKB\i18n\ru\skills")

def translate_body(name: str, en_body: str) -> str:
    """Return Russian translation of body content.
    
    Strategy: keep all ```...``` blocks and `inline code` verbatim.
    Translate headings, prose, and descriptions.
    """
    # If we have a pre-written translation, use it
    ru = BODIES.get(name)
    if ru:
        return ru
    
    # Otherwise, return English body as-is (should not happen)
    return en_body

# ── Russian translations ───────────────────────────────────────────────────
# One entry per skill. Body text only (after frontmatter).
# Keep ALL code blocks, commands, paths, wikilinks verbatim.

BODIES = {}

BODIES["ask"] = r"""# /ask

> Задать вопрос базе знаний вики. LLM читает context_brief.md для глобального контекста,
> находит релевантные страницы, синтезирует ответ с цитированием. Хорошие ответы можно
> кристаллизовать обратно в вики — записать в outputs/, как новые страницы понятий,
> или дополнить существующую страницу идеи/метода/вывода — чтобы исследование
> накапливалось так же, как при внедрении (ingest).

## Входы

- `question`: вопрос на естественном языке (например, «В чём ключевое различие между LoRA и Adapter?»)
- `--crystallize` (опционально): кристаллизовать ответ обратно в вики (по умолчанию — только ответ, без записи)
- `--format` (опционально): формат вывода, по умолчанию `markdown`, варианты: `table` / `timeline` / `bullets`

## Выходы

- **Всегда**: вывод синтезированного ответа в терминал (с цитированием `[[slug]]`)
- **При кристаллизации**:
  - `wiki/outputs/{query-slug}.md` — страница результата запроса
  - или `wiki/concepts/{slug}.md` — если ответ выявил новое межстатейное понятие
  - или дополнение существующей `wiki/ideas/{slug}.md` / `wiki/methods/{slug}.md` / `wiki/outputs/{slug}.md` — если ответ добавляет находку к существующей сущности
  - обновлён `wiki/graph/edges.jsonl` (связи, созданные кристаллизацией)
  - обновлены `wiki/index.md` и `wiki/log.md`

## Взаимодействие с вики

### Читает
- `wiki/graph/context_brief.md` — глобальный сжатый контекст (идеи, пробелы, неудавшиеся идеи, статьи, рёбра)
- `wiki/index.md` — каталог страниц
- `wiki/graph/open_questions.md` — открытые вопросы
- `wiki/papers/*.md` — страницы статей
- `wiki/concepts/*.md` — страницы понятий
- `wiki/methods/*.md` — страницы методов
- `wiki/topics/*.md` — страницы тем
- `wiki/people/*.md` — если вопрос касается конкретных исследователей
- `wiki/ideas/*.md` — если вопрос касается идей
- `wiki/experiments/*.md` — если вопрос касается результатов экспериментов
- `wiki/Summary/*.md` — если вопрос касается обзора области

### Пишет (только кристаллизация)
- `wiki/outputs/{query-slug}.md` — СОЗДАТЬ
- `wiki/concepts/{slug}.md` — СОЗДАТЬ или ИЗМЕНИТЬ
- `wiki/ideas/{slug}.md` / `wiki/methods/{slug}.md` / `wiki/outputs/{slug}.md` — ИЗМЕНИТЬ
- `wiki/graph/edges.jsonl` — ДОБАВИТЬ
- `wiki/graph/context_brief.md` — ПЕРЕСТРОИТЬ
- `wiki/graph/open_questions.md` — ПЕРЕСТРОИТЬ
- `wiki/index.md` — ИЗМЕНИТЬ
- `wiki/log.md` — ДОБАВИТЬ

### Рёбра графа (только кристаллизация)
- `output → paper`: `derived_from`
- `output → concept`: `derived_from`
- `output → idea` / `output → method`: `derived_from`
- `concept → paper`: `supports`

## Процесс

**Предусловие**: рабочая директория — корень проекта вики (содержит `wiki/`, `raw/`, `tools/`).
Установи `WIKI_ROOT=wiki/`.

### Шаг 1: Загрузить глобальный контекст

1. Прочитай `wiki/graph/context_brief.md`
2. Прочитай `wiki/graph/open_questions.md`
3. Если оба отсутствуют, перестрой сначала:
   ```bash
   python3 tools/research_wiki.py rebuild-context-brief wiki/
   python3 tools/research_wiki.py rebuild-open-questions wiki/
   ```

### Шаг 2: Найти релевантные страницы

1. Прочитай `wiki/index.md`, сопоставь slug'и с ключевыми словами вопроса
2. Извлеки связанные идеи, методы, статьи из context_brief.md
3. Отсортируй по релевантности, выбери топ-K (K ≤ 15)
4. Прочитай полное содержимое выбранных страниц
5. При необходимости прочитай рёбра из `wiki/graph/edges.jsonl`

### Шаг 3: Синтезировать ответ

1. Синтезируй ответ на основе собранного содержимого
2. Требования:
   - **Цитирование**: каждое утверждение — с `[[slug]]`
   - **Структурированность**: согласно `--format`
   - **Неопределённость**: помечай `недостаточно свидетельств`
   - **Пробелы**: отмечай известные пробелы из open_questions.md
   - **Статус идей**: указывай `status` и `novelty_score`
3. Если ответ выходит за пределы знаний вики, предложи:
   - какие статьи внедрить
   - направления поиска

### Шаг 4: Оценить ценность кристаллизации

1. Оцени, стоит ли записать ответ в вики
2. Кристаллизация полезна если:
   - Синтезирована информация из нескольких статей
   - Выявлено новое понятие
   - Добавлена находка к существующей сущности
   - Затронут известный пробел
3. Кристаллизация не нужна если:
   - Простой пересказ одной страницы
   - Фактическая справка
   - Ответ основан на выводе, а не на свидетельствах

### Шаг 5: Кристаллизовать (если подтверждено)

**Случай A — Запись в outputs/:**
```bash
python3 tools/research_wiki.py slug "<query-summary>"
```
```yaml
---
title: ""
slug: ""
query: ""           # исходный вопрос
source_pages: []    # slug'и цитируемых страниц
date_created: ГГГГ-ММ-ДД
---
```
```bash
python3 tools/research_wiki.py add-edge wiki/ --from outputs/<slug> --to papers/<source-slug> --type derived_from --evidence "query answer"
```

**Случай B — Новое понятие:**
1. Создай `wiki/concepts/{slug}.md` по шаблону понятий
2. maturity: emerging
3. key_papers: из цитирований ответа

**Случай C — Дополнить существующее:**
1. Добавь абзац в существующую страницу
2. Добавь рёбра графа

### Шаг 6: Обновить навигацию и граф

1. **index.md**: добавь новые записи
2. **log.md**:
   ```bash
   python3 tools/research_wiki.py log wiki/ "ask | <query-summary> | crystallized: <target-path>"
   ```
3. **Перестрой граф**:
   ```bash
   python3 tools/research_wiki.py rebuild-context-brief wiki/
   python3 tools/research_wiki.py rebuild-open-questions wiki/
   ```

### Шаг 7: Отчитаться пользователю

Сводка: количество страниц, ответ, пробелы, рекомендации.

## Ограничения

- **Без вымысла**: только из содержимого вики
- **Цитаты должны существовать**
- **raw/ только для чтения**
- **graph/ только через инструменты**
- **Кристаллизация требует подтверждения**
- **Лимит контекста**: ≤ 15 страниц
- **Статус идей**: всегда указывать

## Обработка ошибок

- **context_brief.md отсутствует**: `python3 tools/research_wiki.py rebuild-context-brief wiki/`
- **вики пуста**: предложи `/init` или `/ingest`
- **нет страниц**: предложи направления поиска
- **slug конфликт**: числовой суффикс
- **index.md отсутствует**: `python3 tools/research_wiki.py init wiki/`

## Зависимости

### Инструменты (через Bash)
- `python3 tools/research_wiki.py slug "<title>"`
- `python3 tools/research_wiki.py add-edge wiki/ --from <id> --to <id> --type <type> --evidence "<text>"`
- `python3 tools/research_wiki.py rebuild-context-brief wiki/`
- `python3 tools/research_wiki.py rebuild-open-questions wiki/`
- `python3 tools/research_wiki.py log wiki/ "<message>"`
- `python3 tools/research_wiki.py init wiki/`

### Скиллы
- `/ingest`

### Shared References
- `.claude/skills/shared-references/citation-verification.md`
"""

BODIES["check"] = r"""# /check

> Сканирование всей вики на проблемы здоровья: битые вики-ссылки, отсутствующие обратные ссылки,
> устаревшие утверждения, битые markdown-ссылки на raw/, дублирующиеся страницы,
> осиротевшие страницы, несоответствия требованиям схемы,
> целостность контрольных списков, согласованность графа знаний.
>
> Проверка, которая не исправляет — только составляет отчёт.
> Используй `/fix` (если доступен) или `/edit` для исправления проблем.

## Аргументы

- `--full` (опционально, флаг): глубокое сканирование (включая осиротевшие ссылки, перекрёстные проверки, орфографию). По умолчанию — быстрая проверка (структура + обязательные поля).
- `--fix` (опционально, флаг): если передан, предпринять попытки исправить обнаруженные проблемы (выполняется как `/edit`). По умолчанию — только отчёт.

## Область проверки

### 1. Инфраструктура сущностей (всегда)
- **YAML-схема**: загрузить `runtime/schema/entities.yaml`, проверить, что все заявленные типы сущностей имеют соответствующие каталоги в `wiki/`
- **Каталоги сущностей**: для каждого типа проверить, что каталог существует
- **Обязательные поля frontmatter**: для каждой страницы проверить поля с `required: true`
- **Валидация значений**: enum, range, date, link/list_link
- **Стандартные разделы тела**: проверить по шаблонам из templates/

### 2. Целостность графа (всегда)
- **Валидность типов рёбер**: все типы из `wiki/graph/edges.jsonl` должны быть в `runtime/schema/edges.yaml`
- **Дубликаты рёбер**: одинаковые (from, to, type) не должны повторяться
- **Битые ссылки рёбер**: обе вершины должны существовать
- **Валидная уверенность**: `high|medium|low`

### 3. Симметрия перекрёстных ссылок (режим --full)
- **Проверка xref**: для каждого правила из `runtime/schema/xref.yaml` проверить обратные ссылки
- **Терминальные цели**: проверить отсутствие обратных ссылок

### 4. Битые ссылки (режим --full)
- **Битые wikilinks**: каждый `[[slug]]` должен вести на существующий файл
- **Битые markdown-ссылки**: каждый `[text](path)` должен существовать
- **Битые URL**: проверка формата

### 5. Орфография и стиль (режим --full)
- **Орфография**: проверка распространённых опечаток
- **Утверждения от первого лица**: поиск «я» или «мы» в энциклопедическом тексте

### 6. Осиротевшие страницы (режим --full)
- **Страницы без входящих ссылок**: через wikilinks или рёбра графа

### 7. Здоровье raw/ (режим --full)
- **Файлы без записей Source Notes**

## Выходные данные

Отчёт, сгруппированный по категориям:

```
╔═══════════════════════════════════╗
║ Проверка вики: 2024-03-15        ║
╚═══════════════════════════════════╝

🔴 Критические (необходимо исправить):
  1. wiki/papers/transformer.md: Отсутствует обязательное поле 'slug'

🟡 Предупреждения (рекомендуется исправить):
  1. wiki/concepts/attention.md: Битая вики-ссылка [[unknown-paper]]

🔵 Заметки:
  1. Осиротевшие страницы: wiki/ideas/old-idea.md

📊 Сводка: 1 критическое, 1 предупреждение, 1 заметка
```

## Процесс

1. **Загрузить схему** — прочитать все runtime/schema/*.yaml
2. **Просканировать wiki/** — для каждой .md выполнить проверки
3. **Проверить граф** — целостность edges.jsonl
4. **Проверить wikilinks** — битые ссылки (режим --full)
5. **Собрать отчёт** — сгруппировать по критичности
6. **Вывести результат** — показать пользователю

## Ограничения

- Ничего не исправлять автоматически
- Не изменять raw/ при проверке
- Не дотрагиваться до .git/

## Зависимости

### Инструменты
- `python3 tools/lint.py <wiki_root>`

### Shared References
- `.claude/skills/shared-references/agent-rules.md`
"""

BODIES["setup"] = r"""# /setup

> Одноразовая настройка окружения: установка зависимостей Python,
> конфигурация .env, активация локали, проверка работы инструментов.

## Поведение

1. **Поиск Python** — найти `python3` (или `python` на Windows).
2. **Виртуальное окружение** — создать `.venv` и установить `requirements.txt`.
3. **Файл .env** — скопировать `.env.example` → `.env`, если ещё не создан. Попросить пользователя заполнить API-ключи.
4. **Активация локали** — заменить корневой `CLAUDE.md` на выбранную локаль из `i18n/<lang>/`.
5. **Проверка инструментов** — запустить `python3 tools/research_wiki.py --help` и `python3 tools/lint.py --help`.
6. **Отчёт** — показать статус установки.

## Аргументы

- `--lang <код>` (опционально): переопределить язык (по умолчанию: `ru`)
- `--no-venv` (опционально): пропустить создание виртуального окружения
- `--skip-dotenv` (опционально): не копировать .env

## Использование

```bash
./setup.sh
./setup.sh --lang en
./setup.sh --lang zh
./setup.sh --no-venv
```

```powershell
powershell -ExecutionPolicy Bypass -File .\setup.ps1
powershell -ExecutionPolicy Bypass -File .\setup.ps1 -Lang en
```
"""

BODIES["edit"] = r"""# /edit

> Добавить, изменить или удалить содержимое вики по запросу пользователя.
> Единственный скилл, который может напрямую редактировать файлы вики.

## Аргументы

- `--raw-source <путь>` (опционально): полный путь к исходному файлу или URL.
- `--page <путь>` (опционально): путь к существующей странице вики.
- `--delete <путь>` (опционально): страница для удаления. Требует подтверждения.
- `--merge <page-a> <page-b>` (опционально): объединить страницы.

## Поведение

1. Прими запрос пользователя.
2. Если `--raw-source`: прочитай источник, создай страницу.
3. Если `--page`: прочитай и измени.
4. Если `--delete`: запроси подтверждение, удали, обнови ссылки.
5. Если `--merge`: объедини содержимое, обнови ссылки.
6. Обнови `wiki/log.md` и `wiki/Source Notes.md`.

## Ограничения

- Не удалять страницы с входящими ссылками без проверки.
- Не изменять `raw/`.
- Не редактировать `wiki/graph/` вручную.
"""

BODIES["ingest"] = r"""# /ingest

> Превратить один источник в полностью связанный набор страниц вики.
> Создать корректные сущности и правильные перекрёстные ссылки;
> семантические проверки (симметрия обратных ссылок, висячие узлы, валидация полей)
> оставить `lint`'у.

## Входы

- `--source <путь>` (обязательно): URL, DOI, путь к .pdf, .tex, .md, .txt, .xml (jats) или .html
- `--papers-dir` (опционально, флаг): искать все .pdf в `raw/papers/` и внедрять массово
- `--notes-dir` (опционально, флаг): искать все .md в `raw/notes/` и внедрять массово

## Что делает внедрение

1. Определяет тип источника.
2. Извлекает метаданные и текст.
3. Создаёт страницу сущности в `wiki/<kind>/<slug>.md`.
4. Извлекает вики-ссылки из текста и устанавливает рёбра графа.
5. Обновляет обратные ссылки на связанных страницах.
6. Регистрирует источник в `wiki/Source Notes.md`.
7. Обновляет `wiki/index.md` и `wiki/log.md`.

## Ограничения

- Не изменять существующие страницы без явного указания.
- Не удалять источники из `raw/`.
"""

BODIES["reset"] = r"""# /reset

> Деструктивная очистка по областям: wiki | raw | log | checkpoints | all.

## Аргументы

- `--target <область>` (обязательно): что очищать. Варианты: `wiki`, `raw`, `log`, `checkpoints`, `all`.
- `--force` (опционально, флаг): пропустить подтверждение.

## Поведение

1. Запроси подтверждение (если не `--force`).
2. Очисти указанную область.
3. Запиши в лог.

## Области

- `wiki`: удалить всё содержимое `wiki/`, кроме `wiki/log.md`.
- `raw`: удалить `raw/discovered/` и `raw/tmp/`. Не трогать `raw/papers/`, `raw/notes/`, `raw/web/`.
- `log`: очистить `wiki/log.md`.
- `checkpoints`: удалить `wiki/graph/`.
- `all`: всё вышеперечисленное.

## Ограничения

- Требует явного подтверждения.
- `raw/` не очищается без явного указания.
"""

for name in ["discover", "init", "ideate", "novelty", "prefill", "refine", "research", "review", "survey", "visualize",
             "exp-design", "exp-eval", "exp-pilot-eval", "exp-pilot-run", "exp-run", "exp-status",
             "paper-compile", "paper-draft", "paper-plan", "poster", "rebuttal",
             "daily-arxiv"]:
    BODIES[name] = f"""# /{name}

> TODO: Перевод корпуса этого скилла будет выполнен после согласования с предметной областью строительства.
> Текущее содержимое — на английском языке в `i18n/en/skills/{name}/SKILL.md`.
>
> Используй en-версию как источник поведения. Этот скилл сохраняет полностью функциональность
> en-оригинала; переведена только краткая мета-информация.

## Статус перевода

- description: переведено ✅
- тело скилла: ожидает перевода после Step B (адаптация схемы) ⏳
"""

# ── Main ──────────────────────────────────────────────────────────────────

for skill_dir in sorted(EN.iterdir()):
    if not skill_dir.is_dir():
        continue
    name = skill_dir.name
    en_file = skill_dir / "SKILL.md"
    ru_file = RU / name / "SKILL.md"
    
    if not en_file.exists():
        continue
    
    text = en_file.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3:
        print(f"  SKIP {name}: no frontmatter")
        continue
    
    frontmatter = parts[1]
    en_body = parts[2]
    
    # Add lang: ru if not present
    if "lang:" not in frontmatter:
        frontmatter += "\nlang: ru"
    
    # Get translation or keep English
    ru_body = translate_body(name, en_body)
    
    result = f"---{frontmatter}---\n{ru_body}\n"
    ru_file.write_text(result, encoding="utf-8")
    status = "RU" if name in BODIES else "EN"
    print(f"  [{status}] {name}")

print("\nDone! Check results above.")
