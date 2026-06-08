import os
import requests
from flask import Flask

app = Flask(__name__)

def run_bot():
    try:
        # 1. Запрос живой погоды для Одессы через wttr.in
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

        # 2. Железобетонная отправка в Telegram через библиотеку requests
        token = "8853778240:AAHVYQPWB9d6Xoe8zSsIgUOr9-e-KB4HAFA"
        chat_id = "-1002364375082"
        
        tg_url = f"https://telegram.org{token}/sendMessage"
        tg_res = requests.post(tg_url, json={"chat_id": chat_id, "text": text}, timeout=10)
        
        if tg_res.status_code == 200:
            return "<h1>🎉 Успішно! Пост з живою погодою відправлений в Telegram-канал!</h1>"
        else:
            return f"<h1>❌ Помилка Telegram: {tg_res.status_code}</h1><p>{tg_res.text}</p>"
        
    except Exception as e:
        return f"<h1>⚠️ Критична помилка в коді:</h1><p>{e}</p>"

@app.route('/', methods=['GET', 'HEAD'])
def index():
    return run_bot()

if __name__ == "__main__":
    # Читаем порт, который выдает Render, либо ставим стандартный 10000
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
