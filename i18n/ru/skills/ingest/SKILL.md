---
description: "Ingest a paper into the wiki — creates pages (papers + concepts + methods + people) and builds all cross-references and graph edges. Trigger whenever the user says \"ingest\", \"add this paper\", drops a `.pdf` / `.tex` / arXiv URL, or asks to fold a paper into the knowledge base."
lang: ru
argument-hint: "<local-path-or-arXiv-URL> [--discover] [--visualize]"
---
# /ingest

> Превратить один источник в полностью связанный набор страниц вики.
> Создать корректные сущности и правильные перекрёстные ссылки;
> семантические проверки оставить lint'у.

## Входы

- `--source <путь>` (обязательно): URL, DOI, путь к .pdf, .md, .txt, .html
- `--papers-dir` (опционально, флаг): внедрить все .pdf из `raw/papers/`
- `--notes-dir` (опционально, флаг): внедрить все .md из `raw/notes/`

## Что делает внедрение

1. Определи тип источника (pdf, url, tex, md, txt).
2. Извлеки метаданные: заголовок, авторы, дата, тип.
3. Извлеки текст и ключевые термины.
4. Создай страницу сущности в `wiki/<kind>/<slug>.md`.
5. Извлеки вики-ссылки из текста, установи рёбра графа.
6. Обнови обратные ссылки на связанных страницах.
7. Зарегистрируй источник в `wiki/Source Notes.md`.
8. Обнови `wiki/index.md` и `wiki/log.md`.

## Процесс

1. Прочитай `runtime/schema/entities.yaml` для структуры frontmatter.
2. Сгенерируй slug: `python3 tools/research_wiki.py slug "<заголовок>"`.
3. Создай страницу с полным frontmatter по схеме.
4. Найди связи с существующими страницами через `python3 tools/research_wiki.py find`.
5. Добавь рёбра: `python3 tools/research_wiki.py add-edge wiki/ --from X --to Y --type Z`.
6. Обнови обратные ссылки на целевых страницах.

## Ограничения

- Не изменять существующие страницы без явного указания.
- Не удалять источники из `raw/`.
- Не трогать `wiki/graph/` вручную.

## Зависимости

### Инструменты
- `python3 tools/research_wiki.py slug "<title>"`
- `python3 tools/research_wiki.py find wiki/ <kind> --field value`
- `python3 tools/research_wiki.py add-edge wiki/ --from X --to Y --type Z`

### Shared References
- `.claude/skills/shared-references/citation-verification.md`

