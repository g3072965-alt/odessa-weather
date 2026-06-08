import os
import urllib.parse
import urllib.request
from flask import Flask

app = Flask(__name__)

# ИСПРАВЛЕНО: Постоянное и точное имя вашего публичного канала
CHANNEL_ID = "@odessa_meteo_day"

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
            "Бажаємо вам чутового та продуктивного дня! ✨"
        )

        # 2. Собираем адрес API Telegram
        part1 = "https://api."
        part2 = "telegram"
        part3 = ".org/bot"
        token = "8959094212:AAEI5eaN8qGNnk5t8gAOIy7fVVLgNPuYpr4"
        method = "/sendMessage"
        tg_url = part1 + part2 + part3 + token + method
        
        # ИСПРАВЛЕНО: Отправляем данные как обычную форму, которую Telegram одобряет без фильтров
        data_dict = {
            "chat_id": CHANNEL_ID,
            "text": text
        }
        payload = urllib.parse.urlencode(data_dict).encode('utf-8')
        
        req_tg = urllib.request.Request(
            tg_url, 
            data=payload, 
            headers={'Content-Type': 'application/x-www-form-urlencoded'}
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
