---
description: "Ask the wiki a question, retrieve and synthesize relevant pages, optionally crystallize the answer back into the wiki"
lang: ru
argument-hint: "<question>"
---
# /ask

> Задать вопрос базе знаний вики. LLM читает context_brief.md для глобального контекста, находит релевантные страницы, синтезирует ответ с цитированием. Хорошие ответы можно кристаллизовать обратно в вики.

## Входы

- question: вопрос на естественном языке

- --crystallize (опц.): кристаллизовать ответ в вики (по умолч. только ответ)

- --format (опц.): формат вывода: markdown (по умолч.) | table | timeline | bullets

## Выходы

- **Всегда**: синтезированный ответ с [[slug]] цитированием

- **При кристаллизации**:

  - wiki/outputs/{query-slug}.md — страница результата

  - или wiki/concepts/{slug}.md — новое понятие

  - или дополнение существующей wiki/ideas/{slug}.md / wiki/methods/{slug}.md / wiki/outputs/{slug}.md

  - обновлён wiki/graph/edges.jsonl, wiki/index.md, wiki/log.md

## Взаимодействие с вики

### Читает

- wiki/graph/context_brief.md, wiki/index.md, wiki/graph/open_questions.md

- wiki/papers/*.md, wiki/concepts/*.md, wiki/methods/*.md, wiki/topics/*.md, wiki/people/*.md

- wiki/ideas/*.md, wiki/experiments/*.md, wiki/Summary/*.md

### Пишет (только кристаллизация)

- wiki/outputs/{query-slug}.md — СОЗДАТЬ

- wiki/concepts/{slug}.md — СОЗДАТЬ или ИЗМЕНИТЬ

- wiki/ideas/{slug}.md / wiki/methods/{slug}.md / wiki/outputs/{slug}.md — ИЗМЕНИТЬ

- wiki/graph/edges.jsonl — ДОБАВИТЬ

- wiki/graph/context_brief.md, wiki/graph/open_questions.md — ПЕРЕСТРОИТЬ

- wiki/index.md — ИЗМЕНИТЬ

- wiki/log.md — ДОБАВИТЬ

### Рёбра графа (кристаллизация)

- output → paper|concept|idea|method: derived_from

- concept → paper: supports

## Процесс

**Предусловие**: рабочая директория — корень проекта. WIKI_ROOT=wiki/.

### Шаг 1: Глобальный контекст

1. Прочитай wiki/graph/context_brief.md

2. Прочитай wiki/graph/open_questions.md

3. Если нет — перестрой:

   `ash

   python3 tools/research_wiki.py rebuild-context-brief wiki/

   python3 tools/research_wiki.py rebuild-open-questions wiki/

   `

### Шаг 2: Поиск страниц

1. Сопоставь slug''и из index.md с вопросом

2. Выбери топ-15 по релевантности

3. Прочитай полное содержимое

### Шаг 3: Синтез ответа

- Каждое утверждение — с [[slug]]

- Формат по --format

- Помечай пробелы знаний

- Указывай status и 

ovelty_score идей

### Шаг 4: Оценка кристаллизации

Полезна если: синтез нескольких статей, новое понятие, заполнение пробела.

Не нужна если: пересказ одной страницы, простая справка.

### Шаг 5: Кристаллизация

`ash

python3 tools/research_wiki.py slug "<query-summary>"

`

`ash

python3 tools/research_wiki.py add-edge wiki/ --from outputs/<slug> --to papers/<source-slug> --type derived_from --evidence "query answer"

`

### Шаг 6: Обновление

`ash

python3 tools/research_wiki.py log wiki/ "ask | <query> | crystallized: <target>"

python3 tools/research_wiki.py rebuild-context-brief wiki/

python3 tools/research_wiki.py rebuild-open-questions wiki/

`

### Шаг 7: Отчёт

Сводка: число страниц, ответ, пробелы, рекомендации.

## Ограничения

- Без вымысла — только из содержимого вики

- [[slug]] должен существовать

- 

aw/ только чтение, graph/ только через инструменты

- Кристаллизация только с подтверждением

- ≤ 15 страниц

## Обработка ошибок

- context_brief.md отсутствует: python3 tools/research_wiki.py rebuild-context-brief wiki/

- вики пуста: предложи /init или /ingest

- slug конфликт: числовой суффикс

- index.md отсутствует: python3 tools/research_wiki.py init wiki/

## Зависимости

### Инструменты

- python3 tools/research_wiki.py slug "<title>"

- python3 tools/research_wiki.py add-edge wiki/ --from <id> --to <id> --type <type> --evidence "<text>"

- python3 tools/research_wiki.py rebuild-context-brief wiki/

- python3 tools/research_wiki.py rebuild-open-questions wiki/

- python3 tools/research_wiki.py log wiki/ "<message>"

- python3 tools/research_wiki.py init wiki/

### Скиллы

- /ingest

### Shared References

- .claude/skills/shared-references/citation-verification.md

