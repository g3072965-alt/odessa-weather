import os
import requests
from flask import Flask

app = Flask(__name__)

# Имя вашего канала (с двумя 's')
CHANNEL_ID = "@odessa_meteo_day"

def run_bot():
    try:
        # Запрос живой погоды для Одессы
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
            return f"<h1>Помилка сервісу погоди: Status {response.status_code}</h1>"

        # ИСПРАВЛЕНО: Точный токен из BotFather (с нулем '0' вместо буквы 'O')
        tg_url = "https://telegram.org"
        tg_res = requests.post(tg_url, json={"chat_id": CHANNEL_ID, "text": text}, timeout=10).json()
        
        if tg_res.get("ok"):
            return "<h1>🎉 Успішно! Пост з живою погодою відправлений в Telegram-канал!</h1>"
        else:
            return f"<h1>❌ Помилка Telegram:</h1><p>{tg_res.get('description')}</p>"
        
    except Exception as e:
        return f"<h1>⚠️ Критична помилка в коді: {e}</h1>"

@app.route('/')
def index():
    return run_bot()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
