import os
import requests
from flask import Flask

app = Flask(__name__)

# Бот отправит сообщение сразу по двум адресам, чтобы исключить путаницу чатов
CHAT_INPUTS = ["@odesa_meteo", "-1002220194884"]

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
                "Бажаємо вам чутового та продуктивного дня! ✨"
            )
        else:
            return f"<h1>Помилка сервісу погоди: Status {response.status_code}</h1>"

        # Точный токен вашего нового бота @odessa_meteo_day_bot
        tg_url = "https://telegram.org"
        
        results = []
        for chat in CHAT_INPUTS:
            res = requests.post(tg_url, json={"chat_id": chat, "text": text}, timeout=10)
            results.append(f"Чат {chat}: {res.status_code}")
        
        return f"<h1>🎉 Скрипт виконано!</h1><p>Статуси відправок: {', '.join(results)}</p>"
        
    except Exception as e:
        return f"<h1>⚠️ Критична помилка в коді: {e}</h1>"

@app.route('/')
def index():
    return run_bot()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
