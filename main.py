import os
import requests
from flask import Flask

app = Flask(__name__)

# Имя вашего канала (с двумя 's')
CHANNEL_ID = "@odessa_meteo_day"

def run_bot():
    try:
        # Сверхнадежный запрос погоды для Одессы без блокировок и зависаний
        url = "http://open-meteo.com"
        res = requests.get(url, timeout=10).json()
        current = res['current']
        temp = round(current['temperature_2m'])
        
        text = (
            "Доброго ранку, Одесо! 🌊⚓️\n\n"
            "Погода на сьогодні:\n"
            f"🌡 Температура: {temp}°C\n\n"
            "Бажаємо вам чудового та продуктивного дня! ✨"
        )

        # Абсолютно точный токен из BotFather (с нулем '0')
        tg_url = "https://telegram.org"
        tg_res = requests.post(tg_url, json={"chat_id": CHANNEL_ID, "text": text}, timeout=10).json()
        
        if tg_res.get("ok"):
            return "<h1>🎉 Успішно! Пост з живою погодою відправлений в Telegram-канал!</h1>"
        else:
            return f"<h1>❌ Помилка Telegram:</h1><p>{tg_res.get('description')}</p>"
        
    except Exception as e:
        return f"<h1>⚠️ Критична помилка в коді:</h1><p>{e}</p>"

@app.route('/')
def index():
    return run_bot()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
