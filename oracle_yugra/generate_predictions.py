import json
import random

# Parts for generating predictions
subjects = [
    "Кедр", "Обь", "Олень", "Тайга", "Дом", "Дорога", "Костёр", "Северное сияние",
    "Ворона", "Шаманский бубен", "Снег", "Тропа", "Река", "Ветер", "Звезда",
    "Очаг", "Мороз", "Рассвет", "Месяц", "Лес"
]

actions = [
    "принесет", "подарит", "откроет", "укажет", "сохранит", "осветит", "защитит", "направит",
    "притянет", "покажет", "согреет", "наполнит", "укрепит", "приумножит", "встретит"
]

objects = [
    "удачу", "тепло", "радость", "спокойствие", "мудрость", "силу", "свет",
    "мир", "богатство", "здоровье", "вдохновение", "надежду", "успех", "добро", "любовь"
]

conditions = [
    "в пути", "в твоем доме", "сегодня", "на этой неделе", "в скором времени",
    "в твоем сердце", "на твоей тропе", "в твоих делах", "на рассвете", "в трудную минуту",
    "среди снегов", "под северным сиянием", "у очага", "в семье", "в промысле",
    "когда пойдет снег", "на новом месте", "в пути", "в дороге", "в делах"
]

extras = [
    "Слушай голос тайги.",
    "Пусть духи будут благосклонны.",
    "Верь в свои силы.",
    "Пусть твоя дорога будет светлой.",
    "Улыбнись новому дню.",
    "Сохрани тепло в сердце.",
    "Пусть удача сопутствует тебе.",
    "Прислушайся к ветру.",
    "Следуй за северным сиянием.",
    "Пусть очаг твой не гаснет.",
    "Шагай смело.",
    "Будь как могучий кедр.",
    "Тайга хранит свои секреты.",
    "Свет звезд укажет путь.",
    "Добро всегда возвращается."
]

predictions = set()

# Generate unique combinations
while len(predictions) < 1000:
    subj = random.choice(subjects)
    act = random.choice(actions)
    obj = random.choice(objects)
    cond = random.choice(conditions)
    extra = random.choice(extras)

    # Capitalize the first letter and build sentence
    prediction = f"{subj} {act} тебе {obj} {cond}. {extra}"
    predictions.add(prediction)

# Convert to list and save as JS array format
pred_list = list(predictions)

js_content = f"const PREDICTIONS = {json.dumps(pred_list, ensure_ascii=False, indent=2)};\n"

with open("predictions.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Generated {len(pred_list)} unique predictions in predictions.js")
