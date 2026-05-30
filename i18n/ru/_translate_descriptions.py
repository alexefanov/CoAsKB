"""Batch-translate SKILL.md descriptions to Russian. Keep body unchanged."""
import re
from pathlib import Path

EN = Path(r"C:\CoAsKB\i18n\en\skills")
RU = Path(r"C:\CoAsKB\i18n\ru\skills")

# Russian translations for each skill's description
TRANSLATIONS = {
    "ask": "Задать вопрос вики — найти и обобщить релевантные страницы, опционально кристаллизовать ответ обратно в вики",
    "check": "Просканировать всю вики на проблемы здоровья и составить отчёт с рекомендациями по исправлению (все типы сущностей из runtime/schema/entities.yaml + целостность графа)",
    "daily-arxiv": "Запустить или управлять ежедневной лентой рекомендаций arXiv. Для разовых рекомендаций свежих статей, настройки/статуса/отключения GitHub Actions, email-дайджестов и явного высоконадёжного авто-ingest через /ingest",
    "discover": "Построить ранжированный шорт-лист кандидатов (по якорям, теме или состоянию вики), который пользователь или вышестоящий скилл может передать в /ingest. Не выполняет ingest, только предлагает",
    "edit": "Добавить или удалить исходные источники, или обновить содержимое вики по запросу пользователя",
    "exp-design": "Спроектировать эксперимент из идеи: выбрать метод, метрики, бейзлайн — и записать страницу эксперимента в вики",
    "exp-eval": "Оценить результаты эксперимента, вынести вердикт (успех/неудача/неопределённо) и обновить связанную страницу идеи",
    "exp-pilot-eval": "Оценить результаты пилотного эксперимента: прочитать результаты, применить лояльную логику вердикта",
    "exp-pilot-run": "Запустить пилотный эксперимент: написать код, развернуть, отследить, собрать сырые результаты",
    "exp-run": "Реализовать, развернуть и отследить эксперимент (локально или на удалённом GPU)",
    "exp-status": "Панель состояния запущенных экспериментов; авто-сбор результатов",
    "ideate": "Многофазовый конвейер генерации исследовательских идей: обзор ландшафта → дуальная мозговая атака → фильтрация и валидация → запись в вики → пилот",
    "ingest": "Внедрить источник в вики — создаёт страницы и строит все перекрёстные ссылки и рёбра графа. Запускать когда пользователь говорит \"внедри\", \"добавь этот документ\", передаёт .pdf/.tex/URL",
    "init": "Инициализировать вики из пользовательских источников с опциональным внешним поиском, затем внедрить итоговый набор параллельно",
    "novelty": "Многоисточниковая проверка новизны: веб + Semantic Scholar + вики + Review LLM",
    "paper-compile": "Скомпилировать LaTeX в PDF, авто-исправить ошибки, проверить объём и анонимность",
    "paper-draft": "Написать черновик статьи (LaTeX + рисунки) по разделу из плана, используя знания вики",
    "paper-plan": "Составить план статьи из валидированных идей + матрицы свидетельств",
    "poster": "Превратить готовый черновик статьи в печатный постер конференции (HTML + PNG)",
    "prefill": "Опционально заполнить foundations/ фоновыми знаниями из Wikipedia",
    "rebuttal": "Разобрать комментарии рецензентов и составить поточечный ответ",
    "refine": "Многораундовое улучшение: создать → рецензировать → исправить → перерецензировать",
    "research": "Сквозной оркестратор исследования с человеческими шлюзами",
    "reset": "Деструктивная очистка по областям: wiki | raw | log | checkpoints | all",
    "review": "Межмодельная adversarial-рецензия любого исследовательского артефакта",
    "setup": "Первичная настройка (API-ключи, язык, зависимости)",
    "survey": "Сгенерировать раздел Related Work для статьи из знаний вики — тематическая группировка → нарративная структура → LaTeX-вывод, следуя citation-verification и academic-writing",
    "visualize": "Сгенерировать или обновить артефакты визуализации графа знаний (веб-интерфейс, Obsidian-конфиг, Canvas)",
}

for skill_dir in sorted(EN.iterdir()):
    if not skill_dir.is_dir():
        continue
    name = skill_dir.name
    en_file = skill_dir / "SKILL.md"
    ru_file = RU / name / "SKILL.md"
    
    if not en_file.exists():
        continue
    
    text = en_file.read_text(encoding="utf-8")
    
    # Replace description in YAML frontmatter
    desc = TRANSLATIONS.get(name, "")
    if desc:
        # Replace the description line (first occurrence)
        text = re.sub(
            r'^description: .*$',
            f'description: {desc}',
            text,
            count=1,
            flags=re.MULTILINE
        )
    
    # Add Russian language hint to frontmatter
    if "---" in text:
        # Find the closing ---
        parts = text.split("---", 2)
        if len(parts) >= 3:
            # Insert lang field after description
            front = parts[1]
            if "lang:" not in front:
                front = re.sub(
                    r'^(description: .*)$',
                    r'\1\nlang: ru',
                    front,
                    count=1,
                    flags=re.MULTILINE
                )
            text = f"---{front}---\n{parts[2]}"
    
    ru_file.parent.mkdir(parents=True, exist_ok=True)
    ru_file.write_text(text, encoding="utf-8")
    print(f"  OK  {name}")

print("\nDone! Translated descriptions for all skills.")
