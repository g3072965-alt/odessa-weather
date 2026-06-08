import json
import urllib.parse
import urllib.request

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

        # Жестко вшитый рабочий токен нового бота и ID вашего приватного канала
        token = "8853778240:AAHVYQPWB9d6Xoe8zSsIgUOr9-e-KB4HAFA"
        chat_id = "-1002364375082"
        
        # Полный исправленный адрес API Telegram без посторонних сайтов
        tg_url = f"https://telegram.org{token}/sendMessage"
        
        # Передаем параметры через стандартную форму
        data = urllib.parse.urlencode({"chat_id": chat_id, "text": text}).encode('utf-8')
        req_tg = urllib.request.Request(tg_url, data=data, headers={'User-Agent': 'Mozilla/5.0'})
        
        with urllib.request.urlopen(req_tg, timeout=10) as tg_response:
            res_text = tg_response.read().decode('utf-8')
            
        print(f"УСПЕХ ТЕЛЕГРАМ: {res_text}")
        
    except Exception as e:
        print(f"КРИТИЧЕСКАЯ ОШИБКА: {e}")

if __name__ == "__main__":
    run_bot()
