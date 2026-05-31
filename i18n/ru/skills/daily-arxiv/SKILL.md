---
description: "Run or manage the daily arXiv recommendation feed. Use for one-off fresh-paper recommendations, scheduled GitHub Actions setup/status/disable, email digests, and explicit high-confidence auto-ingest through /ingest."
lang: ru
argument-hint: "[setup|status|disable] [--mode inform|auto-ingest] [--hours 24] [--categories <cat...>] [--max-recommendations 10] [--max-auto-ingest 1] [--send-email true|false]"
---
# /daily-arxiv
> Ежедневные рекомендации arXiv + авто-ingest. Управление лентой, дайджестами, GitHub Actions.

## Аргументы
- `--setup` (опциональнороить GitHub Actions для ежедневного запуска
- `--status` (опционально): показать статус текущей ленты
- `--disable` (опционально): отключить ежедневные рекомендации
- `--recommend` (опционально): сформировать разовые рекомендации сейчас
- `--categories` (опционально): список arXiv-категорий (по умолчанию cs.LG,cs.CV,cs.CL,cs.AI,stat.ML)

## Поведение
1. Проверь настройки: GitHub Actions, категории, email.
2. Получи свежие статьи из arXiv API по указанным категориям.
3. Оцени релевантность каждой статьи относительно текущей вики (через context_brief.md).
4. Отранжируй по релевантности.
5. Сформируй дайджест (текст или email).
6. Покажи пользователю. По запросу — передай топ-статьи в /ingest.

## Выходы
- Список рекомендаций с оценкой релевантности
- (опционально) Email-дайджест
- (опционально) Авто-ingest выбранных статей

## Зависимости
### Инструменты
- `python3 tools/research_wiki.py find wiki/ papers --field arxiv <id>` — проверка наличия

### Скиллы
- /ingest — для внедрения выбранных статей
