---
description: Interactive API key configuration guide — checks current .env state and walks you through Semantic Scholar, DeepXiv, and Review LLM setup

lang: ru---
# /setup

> Одноразовая настройка окружения: установка зависимостей,
> конфигурация .env, активация локали, проверка инструментов.

## Аргументы

- `--lang <код>` (опционально): язык (по умолчанию `ru`)
- `--no-venv` (опционально): пропустить создание виртуального окружения
- `--skip-dotenv` (опционально): не копировать .env

## Поведение

1. **Поиск Python** — проверь наличие `python3` (Windows: `python`).
2. **Виртуальное окружение** — создай `.venv`, установи зависимости:
   ```bash
   python3 -m venv .venv
   .venv/bin/pip install -r requirements.txt
   ```
3. **Файл .env** — скопируй `.env.example` → `.env`.
4. **Активация локали** — скопируй `i18n/<lang>/CLAUDE.md` → корень.
5. **Проверка** — запусти:
   ```bash
   python3 tools/research_wiki.py --help
   python3 tools/lint.py --help
   ```
6. **Отчёт** — покажи статус установки.

## Использование

```bash
# Установка (русский по умолчанию)
./setup.sh

# Выбор языка
./setup.sh --lang en
./setup.sh --lang zh

# Windows
powershell -ExecutionPolicy Bypass -File .\setup.ps1
powershell -ExecutionPolicy Bypass -File .\setup.ps1 -Lang en
```
