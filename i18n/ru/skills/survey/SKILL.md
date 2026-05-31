---
description: "Generate a Related Work section for a paper from wiki knowledge — thematic grouping → narrative structure → LaTeX output, following citation-verification and academic-writing"
lang: ru
argument-hint: "<research-question-or-idea-slugs> [--format latex|markdown] [--max-papers 30]"
---
# /survey
> Сгенерировать раздел Related Work для статьи из знаний вики — тематическая группировка → нарративная структура → LaTeX-вывод.

## Аргументы
- `--topic <тема>` (обязательно): тема обзора
- `--from <slug1,slug2,...>` (опциональноретные страницы для включения
- `--output <файл>` (опционально): путь для .tex (по умолчанию outputs/survey-<slug>.tex)

## Поведение
1. Собери релевантные страницы (из аргумента или поиском по теме).
2. Сгруппируй по тематическим кластерам:
   - Например, «методы на основе X», «применения в Y»
   - Внутри кластера — хронологический порядок
3. Построй нарратив: от общих работ к частным, от старых к новым.
4. Напиши LaTeX:
   ```

   \section{Related Work}

   \subsection{Направление 1}

   \cite{author2023} сделал X...

   ```

5. Проверь цитирования (каждый `\cite` — с подтверждённым BibTeX).
6. Сохрани `.tex` файл.

## Выходы
- `.tex` файл раздела Related Work
- (опционально) обновлён `.bib` файл

## Зависимости
### Инструменты
- `python3 tools/research_wiki.py find wiki/ <kind> --field <field> <value>`

### Shared References
- academic-writing.md, citation-verification.md
