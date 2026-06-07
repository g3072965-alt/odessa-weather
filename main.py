import os
import requests
from flask import Flask

app = Flask(__name__)

# Бот будет автоматически брать секретный токен из настроек Render
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = "@odessa_meteo_day"

def run_bot():
    if not BOT_TOKEN:
        return "Помилка: Секретний BOT_TOKEN не знайдено в налаштуваннях Render!"
        
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
                "Бажаємо вам чудового та продуктивного дня! ✨"
            )
        else:
            return f"Помилка погодного сервісу: {response.status_code}"

        tg_url = f"https://telegram.org{BOT_TOKEN}/sendMessage"
        tg_res = requests.post(tg_url, json={"chat_id": CHANNEL_ID, "text": text}, timeout=10)
        return f"Успішно! Відповідь Telegram: {tg_res.text}"
        
    except Exception as e:
        return f"Помилка в роботі скрипта: {e}"

@app.route('/')
def index():
    return run_bot()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
