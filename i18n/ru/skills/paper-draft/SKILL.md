---
description: "Draft a LaTeX paper from PAPER_PLAN — write each section from wiki sources + generate figures/tables + BibTeX verification + de-AI polish"
lang: ru
argument-hint: "<paper-plan-path> [--review] [--sections <section-numbers>]"
---


# /paper-draft



> Написать черновик статьи (LaTeX + рисунки) по разделу из плана, используя знания вики.



## Аргументы



- `--from <slug-плана>` (обязательно): страница плана статьи

- `--section <имя>` (обязательно): раздел для написания (Introduction, Method, Experiments, Related Work, Discussion)

- `--output <путь>` (опц.): путь для сохранения .tex (по умолч. outputs/<slug>.<section>.tex)



## Поведение



1. Прочитай план статьи (структура, ключевые идеи, цитаты).

2. Собери релевантные страницы из вики по разделу.

3. Напиши раздел в LaTeX:

   - Используй `[[slug]]` для вики-ссылок

   - Для каждого `\cite{}` проверь BibTeX

4. Следуй принципам академического письма (shared-references/academic-writing.md).

5. Проверь цитирования по citation-verification.md.

6. Сохрани .tex файл.



## Требования к цитированию

- BibTeX только из DBLP, CrossRef, Semantic Scholar

- Неподтверждённые: префикс UNCONFIRMED_

- Проверка: `python3 tools/fetch_bib.py "<title>"`



## Выходы

- `.tex` файл раздела

- (Опц.) обновлён `.bib` файл



## Зависимости

### Инструменты

- `python3 tools/research_wiki.py find wiki/ <kind> --field <field> <value>`

- `python3 tools/research_wiki.py neighbors wiki/ <slug> --edge-type <type>`



### Shared References

- academic-writing.md, citation-verification.md

