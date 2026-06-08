import os
import requests
from flask import Flask

app = Flask(__name__)

# ИСПРАВЛЕНО: Жесткий цифровой ID вашего приватного канала из ссылки
CHANNEL_ID = "-1002364375082"

def run_bot():
    try:
        # Надежный текстовый запрос погоды для Одессы через wttr.in
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

        # Точный токен вашего нового бота @odessa_meteo_day_bot
        tg_url = "https://telegram.org"
        tg_res = requests.post(tg_url, json={"chat_id": CHANNEL_ID, "text": text}, timeout=10)
        
        if tg_res.status_code == 200:
            return "<h1>🎉 Успішно! Пост з живою погодою відправлений в приватний Telegram-канал!</h1>"
        else:
            return f"<h1>❌ Помилка Telegram: {tg_res.status_code}</h1><p>{tg_res.text}</p>"
        
    except Exception as e:
        return f"<h1>⚠️ Критична помилка в коді: {e}</h1>"

@app.route('/')
def index():
    return run_bot()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
