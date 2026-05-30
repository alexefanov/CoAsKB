---
description: Seed wiki/foundations/ with domain background knowledge so subsequent /ingest does not create duplicate concept pages for textbook material
argument-hint: "[domain] [--add 'concept name']"

lang: ru---
# /prefill

> Опционально заполнить foundations/ фоновыми знаниями из Wikipedia.

## Аргументы

- `--topic <тема>` (обязательно): тема для заполнения
- `--lang <код>` (опц.): язык Wikipedia (по умолч. en)
- `--max-articles <N>` (опц.): макс. число статей (по умолч. 5)

## Поведение

1. Определи ключевые термы по теме.
2. Для каждого — выполни поиск в Wikipedia:
   ```
   WebFetch: https://en.wikipedia.org/api/rest_v1/page/summary/<term>
   ```
3. Извлеки: заголовок, краткое описание, ключевые факты.
4. Для каждой статьи создай страницу в `wiki/foundations/`:
   ```yaml
   ---
   title: ""
   slug: ""
   source: Wikipedia
   ---
   ```
5. Обнови index.md и log.md.

## Выходы
- Страницы в wiki/foundations/
- Обновлён index.md

## Зависимости
### Инструменты
- WebFetch (Wikipedia API)
- `python3 tools/research_wiki.py slug "<title>"`
