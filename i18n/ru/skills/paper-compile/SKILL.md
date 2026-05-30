---
description: "LaTeX compile → PDF — latexmk compile + auto-fix + page count/anonymity/font/[UNCONFIRMED] checks + submission checklist"
lang: ru
argument-hint: "[paper-dir] [--fix] [--checklist]"
---
# /paper-compile
> Скомпилировать LaTeX в PDF, авто-исправить ошибки, проверить объём и анонимность.

## Аргументы
- `--input <файл.tex>` (обязательно): главный .tex файл
- `--output <файл.pdf>` (опционально): путь для PDF (по умолч. рядом с .tex)
- `--check-anonymity` (опционально): проверить анонимность
- `--max-pages <N>` (опционально): макс. число страниц

## Поведение
1. Скомпилируй LaTeX:
   ```bash

   pdflatex -interaction=nonstopmode input.tex

   bibtex input

   pdflatex -interaction=nonstopmode input.tex

   pdflatex -interaction=nonstopmode input.tex

   ```

2. Прочитай .log, найди ошибки и предупреждения.
3. Авто-исправь типичные ошибки (незакрытые окружения, отсутствующие файлы).
4. Перекомпилируй после исправлений.
5. Проверь объём: если `--max-pages`, сравни.
6. Если `--check-anonymity`: проверь отсутствие имён авторов, ссылок на свои работы.
7. Проверь все [UNCONFIRMED] BibTeX — если остались, предупреди.
8. Предоставь PDF.

## Выходы
- PDF файл
- Отчёт о компиляции (ошибки, предупреждения, объём)

## Зависимости
### Инструменты
- `pdflatex`, `bibtex` (должны быть установлены)
