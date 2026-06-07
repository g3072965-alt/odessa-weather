import os
import requests
from flask import Flask

app = Flask(__name__)

CHANNEL_ID = "@odessa_meteo_day"

def get_weather_desc(code):
    codes = {
        0: "Ясно☀️", 1: "Переважно ясно🌤", 2: "Мінлива хмарність⛅️", 3: "Похмуро☁️",
        45: "Туман🌫", 48: "Осадочний туман🌫",
        51: "Легка мряка🌧", 53: "Помірна мряка🌧", 55: "Щільна мряка🌧",
        61: "Слабкий дощ🌧", 63: "Помірний дощ🌧", 65: "Сильний дощ🌧",
        71: "Слабкий снігопад❄️", 73: "Помірний снігопад❄️", 75: "Сильний снігопад❄️",
        80: "Слабкий зливовий дощ🌦", 81: "Помірний зливовий дощ🌦", 82: "Сильний зливовий дощ⛈",
        95: "Гроза⛈"
    }
    return codes.get(code, "Мінлива хмарність⛅️")

def run_bot():
    try:
        # 1. Ссылка на погоду в Одессе (полная и прямая)
        url = "http://open-meteo.com"
        res = requests.get(url, timeout=10).json()
        current = res['current']
        
        temp = round(current['temperature_2m'])
        feels_like = round(current['apparent_temperature'])
        desc = get_weather_desc(current['weather_code'])
        humidity = current['relative_humidity_2m']
        wind = round(current['wind_speed_10m'], 1)
        
        text = (
            "Доброго ранку, Одесо! 🌊⚓️\n\n"
            "Погода на сьогодні:\n"
            f"🌡 Температура: {temp}°C (відчувається як {feels_like}°C)\n"
            f"📝 На вулиці: {desc}\n"
            f"💧 Вологість: {humidity}%\n"
            f"💨 Вітер: {wind} м/с\n\n"
            "Бажаємо вам чудового та продуктивного дня! ✨"
        )

        # 2. Полная и прямая ссылка для отправки в Telegram (БЕЗ telegram.org)
        tg_url = "https://telegram.org"
        tg_res = requests.post(tg_url, json={"chat_id": CHANNEL_ID, "text": text}, timeout=10).json()
        
        if tg_res.get("ok"):
            return "<h1>Пост успішно відправлений в Telegram-канал! 🎉</h1>"
        else:
            return f"<h1>Помилка Telegram:</h1><p>{tg_res.get('description')}</p>"
        
    except Exception as e:
        return f"<h1>Критична помилка в коді:</h1><p>{e}</p>"

@app.route('/')
def index():
    return run_bot()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
