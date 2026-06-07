import os
import requests
from flask import Flask

app = Flask(__name__)

CHANNEL_ID = "@odessa_meteo_day"

def run_bot():
    try:
        # Сверхнадежный запрос погоды через wttr.in, который Render никогда не блокирует
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = "https://wttr.in"
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            weather_data = response.text.strip()
            
            # Формируем красивый текст поста
            text = (
                "Доброго ранку, Одесо! 🌊⚓️\n\n"
                "Погода на сьогодні:\n"
                f"📊 Дані: {weather_data}\n\n"
                "Бажаємо вам чудового та продуктивного дня! ✨"
            )
        else:
            return f"<h1>Помилка сервісу погоди:</h1><p>Статус {response.status_code}</p>"

        # Абсолютно прямая рабочая ссылка для отправки в Telegram
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
