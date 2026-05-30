---
description: View the status of all running experiments; optionally auto-collect completed experiments and advance the pipeline
argument-hint: "[--pipeline <slug>] [--collect-ready] [--auto-advance]"

lang: ru---
# /exp-status

> Панель состояния запущенных экспериментов; авто-сбор результатов.

## Аргументы

- `--auto-collect` (опц.): собрать результаты завершённых экспериментов
- `--watch` (опц.): непрерывное наблюдение

## Поведение

1. Найди все страницы экспериментов (wiki/experiments/*.md).
2. Для каждого проверь status: running, completed, failed, designed.
3. Если `--auto-collect`: для running экспериментов проверь, завершились ли процессы.
4. Собери результаты завершённых.
5. Покажи панель:
   - **Выполняется**: slug, время запуска, прогресс
   - **Завершён**: slug, результат, метрики
   - **Спроектирован**: slug, статус готовности
   - **Ошибка**: slug, причина

## Выход
Таблица/дашборд состояния экспериментов.

## Зависимости
### Инструменты
- `python3 tools/research_wiki.py find wiki/ experiments`
