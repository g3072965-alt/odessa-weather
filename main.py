import os
import json
import urllib.parse
import urllib.request
from flask import Flask

app = Flask(__name__)

def run_bot():
    try:
        # 1. Системный запрос живой погоды для Одессы через wttr.in
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

        # Новый чистый токен и жесткий ID вашего приватного канала
        token = "8853778240:AAHVYQPWB9d6Xoe8zSsIgUOr9-e-KB4HAFA"
        chat_id = "-1002364375082"
        
        tg_url = f"https://telegram.org{token}/sendMessage"
        
        # Передаем параметры через стандартную форму
        data = urllib.parse.urlencode({"chat_id": chat_id, "text": text}).encode('utf-8')
        req_tg = urllib.request.Request(tg_url, data=data, headers={'User-Agent': 'Mozilla/5.0'})
        
        with urllib.request.urlopen(req_tg, timeout=10) as tg_response:
            res_text = tg_response.read().decode('utf-8')
            
        return f"<h1>🎉 Успішно! Пост з живою погодою відправлений!</h1><p>{res_text}</p>"
        
    except Exception as e:
        return f"<h1>⚠️ Критична помилка в коді:</h1><p>{e}</p>"

@app.route('/', methods=['GET', 'HEAD'])
def index():
    return run_bot()

if __name__ == "__main__":
    # Жестко прописываем стандартный порт 10000 без чтения ломающих переменных окружения
    app.run(host="0.0.0.0", port=10000)
