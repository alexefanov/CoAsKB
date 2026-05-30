---
description: Run or manage the daily arXiv recommendation feed. Use for one-off fresh-paper recommendations, scheduled GitHub Actions setup/status/disable, email digests, and explicit high-confidence auto-ingest through /ingest.
argument-hint: "[setup|status|disable] [--mode inform|auto-ingest] [--hours 24] [--categories <cat...>] [--max-recommendations 10] [--max-auto-ingest 1] [--send-email true|false]"

lang: ru---
# /daily-arxiv

> Ежедневные рекомендации arXiv + авто-ingest. Управление лентой, дайджестами, GitHub Actions.

## Аргументы

- `--setup` (опц.): настроить GitHub Actions для ежедневного запуска
- `--status` (опц.): показать статус текущей ленты
- `--disable` (опц.): отключить ежедневные рекомендации
- `--recommend` (опц.): сформировать разовые рекомендации сейчас
- `--categories` (опц.): список arXiv-категорий (по умолч. cs.LG,cs.CV,cs.CL,cs.AI,stat.ML)

## Поведение

1. Проверь настройки: GitHub Actions, категории, email.
2. Получи свежие статьи из arXiv API по указанным категориям.
3. Оцени релевантность каждой статьи относительно текущей вики (через context_brief.md).
4. Отранжируй по релевантности.
5. Сформируй дайджест (текст или email).
6. Покажи пользователю. По запросу — передай топ-статьи в /ingest.

## Выходы

- Список рекомендаций с оценкой релевантности
- (Опц.) Email-дайджест
- (Опц.) Авто-ingest выбранных статей

## Зависимости

### Инструменты
- `python3 tools/research_wiki.py find wiki/ papers --field arxiv <id>` — проверка наличия

### Скиллы
- /ingest — для внедрения выбранных статей
