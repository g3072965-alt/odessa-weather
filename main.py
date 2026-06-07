import os
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    # Текст сообщения
    text = (
        "Доброго ранку, Одесо! 🌊⚓️\n\n"
        "Погода на сьогодні:\n"
        "🌡 Температура: +22°C (відчувається як +20°C)\n"
        "📝 На вулиці: Прекрасний сонячний день ☀️\n"
        "💧 Вологість: 65%\n"
        "💨 Вітер: 4.5 м/с\n\n"
        "Бажаємо вам чудового та продуктивного дня! ✨"
    )
    
    # Прямая отправка в Telegram одной строкой
    tg_url = "https://telegram.org"
    requests.post(tg_url, json={"chat_id": "@odessa_meteo_day", "text": text}, timeout=10)
    
    return "<h1>Повідомлення надіслано! Перевірте свій Telegram-канал @odessa_meteo_day 🎉</h1>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
