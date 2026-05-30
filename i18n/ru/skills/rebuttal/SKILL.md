---
description: Parse review comments → atomize concerns (Rvx-Cy) → map to wiki ideas/methods → check evidence → Review LLM stress-test → generate rebuttal

lang: ru
argument-hint: <review-file-or-path> [--paper-slug <slug>] [--venue <venue>] [--stress-test] [--format formal|rich]

---

# /rebuttal



> Разобрать комментарии рецензентов и составить поточечный ответ.



## Аргументы



- `--reviews <файл|текст>` (обязательно): текст рецензий

- `--paper <slug>` (обязательно): страница статьи в вики



## Поведение



1. Прочитай рецензии (из файла или из аргумента).

2. Для каждого комментария:

   - Определи категорию: understanding, major, minor, suggestion

   - Подготовь ответ: благодарность + контраргумент/признание + план исправления

3. Сгруппируй ответы по рецензентам.

4. Оформи в формате rebuttal letter:

   ```

   ## Ответ рецензенту 1



   ### Комментарий 1.1

   > Текст комментария...

   

   **Ответ**: Благодарим за замечание. ...

   ```

5. Если нужны правки статьи — отметь.



## Выходы

- Rebuttal letter (markdown или LaTeX)

- (Опц.) Список необходимых правок статьи



## Зависимости

### Скиллы

- /edit — для внесения правок по рецензии

