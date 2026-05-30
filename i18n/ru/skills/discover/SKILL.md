---
description: Build a ranked shortlist of candidate papers (anchor-driven, topic-driven, or derived from current wiki state) that the user — or an upstream skill — may decide to feed into `/ingest`. Use whenever the user asks "what should I read next", "find papers similar to this one", "recommend related work", "what's around this topic", or whenever `/ingest` is invoked with `--discover`. Does not ingest; only proposes.
lang: ru
argument-hint: "(--anchor <id> [--anchor <id>] [--negative <id>] | --topic <str> | --from-wiki | --venue <slug> --year <int>) [--limit N]"
---

# /discover

> Построить ранжированный шорт-лист кандидатов (по якорям, теме или состоянию вики) для передачи в /ingest.

## Аргументы

- `--anchor <ид>` (опц.): найти работы, связанные с указанной сущностью
- `--topic <тема>` (опц.): найти работы по теме
- `--gap` (опц.): найти работы, заполняющие пробелы знаний (на основе open_questions.md)
- `--deep` (опц.): глубокий поиск (больше результатов)
- `--max <N>` (опц.): макс. число кандидатов (по умолч. 10)

## Поведение

1. Определи режим: по якорю, теме, пробелу.
2. Выполни внешний поиск (Semantic Scholar, arXiv, Crossref).
3. Исключи уже имеющиеся в вики.
4. Отранжируй по релевантности.
5. Сформируй шорт-лист с обоснованием.
6. Покажи пользователю. Передай в /ingest по запросу.

## Выход

Список кандидатов с: заголовок, авторы, год, релевантность, обоснование.

## Зависимости

### Инструменты
- `python3 tools/research_wiki.py find wiki/ <kind> --field <field> <value>` — проверка наличия

### Скиллы
- /ingest — для внедрения
