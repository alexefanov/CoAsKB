---
description: "Generate an academic poster from a drafted paper — distill sections into a single-page HTML poster with figures and inter-section transitions"
lang: ru
argument-hint: "[paper-dir] [--review] [--anonymous] [--no-figures] [--no-logos] [--no-refine]"
---
# /poster

> Превратить готовый черновик статьи в печатный постер конференции (HTML + PNG).

## Аргументы

- `--from <файл.tex>` (обязательно): главный .tex файл статьи

- `--output <директория>` (опц.): директория для вывода (по умолч. outputs/poster/)

- `--format` (опц.): формат: html (по умолч.) | png | both

## Поведение

1. Прочитай статью (аннотация, введение, метод, результаты, выводы).

2. Извлеки ключевые элементы: заголовок, авторы, фигуры, таблицы, результаты.

3. Создай HTML-постер:

   - Заголовок и авторы (крупно)

   - Разделы: Motivation, Method, Results, Conclusion

   - Фигуры (из статьи)

   - Ключевые метрики (выделено)

4. Если `--format png` или `both` — конвертируй HTML в PNG.

5. Сохрани файлы.

## Выходы

- HTML-постер

- (Опц.) PNG-изображение

## Зависимости

### Инструменты

- `python3 tools/compile_poster.py --input <file.tex> --output <dir>`

