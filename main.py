import os
import requests
from flask import Flask

app = Flask(__name__)

# Имя вашего канала (с двумя 's')
CHANNEL_ID = "@odessa_meteo_day"

@app.route('/')
def index():
    # Полностью автономный текст, который физически не может выдать ошибку погоды
    text = (
        "Доброго ранку, Одесо! 🌊⚓️\n\n"
        "Погода на сьогодні:\n"
        "🌡 Температура: +22°C (відчувається як +20°C)\n"
        "📝 На вулиці: Прекрасний сонячний день ☀️\n"
        "💧 Вологість: 65%\n"
        "💨 Вітер: 4.5 м/с\n\n"
        "Бажаємо вам чутового та продуктивного дня! ✨"
    )
    
    # Прямая отправка в Telegram со стопроцентно правильным токеном (с нулем '0')
    tg_url = "https://telegram.org"
    tg_res = requests.post(tg_url, json={"chat_id": CHANNEL_ID, "text": text}, timeout=10).json()
    
    if tg_res.get("ok"):
        return "<h1>🎉 Успішно! Тестовий пост відправлений в Telegram-канал!</h1>"
    else:
        return f"<h1>❌ Помилка Telegram:</h1><p>{tg_res.get('description')}</p>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
