import os
import json
import urllib.request
from flask import Flask

app = Flask(__name__)

# Цифровой ID вашего приватного канала
CHANNEL_ID = "-1002364375082"

def run_bot():
    try:
        # 1. Запрос погоды для Одессы через системный urllib
        weather_url = "https://wttr.in"
        req_weather = urllib.request.Request(weather_url, headers={'User-Agent': 'Mozilla/5.0'})
        
        with urllib.request.urlopen(req_weather, timeout=10) as response:
            weather_data = response.read().decode('utf-8').strip()
            
        text = (
            "Доброго ранку, Одесо! 🌊⚓️\n\n"
            "Погода на сьогодні:\n"
            f"📊 Дані: {weather_data}\n\n"
            "Бажаємо вам чудового та продуктивного дня! ✨"
        )

        # 2. Прямая системная отправка в Telegram без сторонних библиотек
        tg_url = "https://telegram.org"
        payload = json.dumps({"chat_id": CHANNEL_ID, "text": text}).encode('utf-8')
        
        req_tg = urllib.request.Request(
            tg_url, 
            data=payload, 
            headers={'Content-Type': 'application/json'}
        )
        
        with urllib.request.urlopen(req_tg, timeout=10) as tg_response:
            res_text = tg_response.read().decode('utf-8')
            
        return f"<h1>🎉 Успішно! Системна відправка виконана!</h1><p>{res_text}</p>"
        
    except Exception as e:
        return f"<h1>⚠️ Критична помилка в системному коді:</h1><p>{e}</p>"

@app.route('/', methods=['GET', 'HEAD'])
def index():
    return run_bot()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
