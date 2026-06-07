import os
import requests
from flask import Flask

app = Flask(__name__)

CHANNEL_ID = "@odessa_meteo_day"

def run_bot():
    try:
        # Прямой запрос погоды без посредников
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

        # Абсолютно прямая и жесткая ссылка на API Telegram в одну строку
        tg_url = "https://telegram.org"
        
        # Отправляем запрос и возвращаем результат на экран
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
