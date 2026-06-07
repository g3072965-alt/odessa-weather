import os
import requests
from flask import Flask

app = Flask(__name__)

BOT_TOKEN = "8822928835:AAEZ_Z0JGDGHTNjDZMz_0hOt7G-k4mvNe1o"
CHANNEL_ID = "@odessa_meteo_day"

def run_bot():
    try:
        # Запрашиваем погоду напрямую через wttr.in (без каких-либо прокси!)
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = "https://wttr.in"
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            weather_data = response.text.strip()
            text = (
                "Доброго ранку, Одесо! 🌊⚓️\n\n"
                "Погода на сьогодні:\n"
                f"📊 Дані: {weather_data}\n\n"
                "Бажаємо вам чудового та продуктивного дня! ✨"
            )
        else:
            return f"Помилка погодного сервісу: {response.status_code}"

        # Отправка сообщения в ваш Telegram-канал
        tg_url = f"https://telegram.org{BOT_TOKEN}/sendMessage"
        tg_res = requests.post(tg_url, json={"chat_id": CHANNEL_ID, "text": text}, timeout=10)
        return f"Успішно! Відповідь Telegram: {tg_res.text}"
        
    except Exception as e:
        return f"Помилка в роботі скрипта: {e}"

# Главная страница вашего сайта. При её открытии будет отправляться погода.
@app.route('/')
def index():
    return run_bot()

if __name__ == "__main__":
    # Обязательная привязка к порту для Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

