import os
import requests
from flask import Flask

app = Flask(__name__)

CHANNEL_ID = "@odessa_meteo_day"
# Код берет чистый готовый адрес, который мы сейчас укажем в панели Render
TG_URL = os.environ.get("TG_URL")

def run_bot():
    if not TG_URL:
        return "Помилка: Секретна адреса TG_URL не знайдена в налаштуваннях Render!"
        
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = "https://wttr.in"
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            weather_data = response.text.strip()
            text = (
                "Доброго ранку, Одесо! 🌊⚓️\n\n"
                "Погода на сьогодні:\n"
                f"📊 Дані: {weather_data}\n\n"
                "Бажаємо вам чутового та продуктивного дня! ✨"
            )
        else:
            return f"Помилка погодного сервісу: {response.status_code}"

        # Отправка сообщения строго по адресу из настроек хостинга
        tg_res = requests.post(TG_URL, json={"chat_id": CHANNEL_ID, "text": text}, timeout=10)
        return f"Успішно! Відповідь Telegram: {tg_res.text}"
        
    except Exception as e:
        return f"Помилка в роботі скрипта: {e}"

@app.route('/')
def index():
    return run_bot()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
