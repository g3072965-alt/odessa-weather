import os
import requests
from flask import Flask

app = Flask(__name__)

CHANNEL_ID = "@odessa_meteo_day"
TG_URL = os.environ.get("TG_URL")

def run_bot():
    print(True, "=== ЗАПУСК БОТА ===")
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = "https://wttr.in"
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            weather_data = response.text.strip()
            text = (
                "Доброго ранку, Одесо! 🌊⚓\n\n"
                "Погода на сьогодні:\n"
                f"📊 Дані: {weather_data}\n\n"
                "Бажаємо вам чудового та продуктивного дня! ✨"
            )
        else:
            print(f"Помилка wttr.in: {response.status_code}")
            return f"Помилка wttr.in: {response.status_code}"

        # Проверяем, откуда брать ссылку: из настроек Render или жестко из кода
        final_url = TG_URL.strip() if TG_URL else "https://telegram.org"
        print(f"Отправка на адрес: {final_url}")
        
        tg_res = requests.post(final_url, json={"chat_id": CHANNEL_ID, "text": text}, timeout=10)
        print(f"Ответ от Telegram: {tg_res.text}")
        return f"Результат: {tg_res.text}"
        
    except Exception as e:
        print(f"КРИТИЧЕСКАЯ ОШИБКА: {e}")
        return f"Ошибка в коде: {e}"

@app.route('/')
def index():
    return run_bot()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
