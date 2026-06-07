import requests

BOT_TOKEN = "8822928835:AAEZ_Z0JGDGHTNjDZMz_0hOt7G-k4mvNe1o"
CHANNEL_ID = "@odessa_meteo_day"

def get_weather_desc(code):
    codes = {
        0: "Ясно☀️", 1: "Переважно ясно🌤", 2: "Мінлива хмарність⛅️", 3: "Похмуро☁️",
        45: "Туман🌫", 48: "Осадочний туман🌫",
        51: "Легка мряка🌧", 53: "Помірна мряка🌧", 55: "Щільна мряка🌧",
        61: "Слабкий дощ🌧", 63: "Помірний дощ🌧", 65: "Сильний дощ🌧",
        71: "Слабкий снігопад❄️", 73: "Помірний снігопад❄️", 75: "Сильний снігопад❄️",
        80: "Слабкий зливовий дощ🌦", 81: "Помірний зливовий дощ🌦", 82: "Сильний зливовий дощ⛈",
        95: "Гроза⛈"
    }
    return codes.get(code, "Мінлива хмарність⛅️")

def run_bot():
    try:
        # Запрос погоды для Одессы (Open-Meteo полностью бесплатен)
        url = "https://open-meteo.com"
        res = requests.get(url).json()
        current = res['current']
        
        temp = round(current['temperature_2m'])
        feels_like = round(current['apparent_temperature'])
        desc = get_weather_desc(current['weather_code'])
        humidity = current['relative_humidity_2m']
        wind = round(current['wind_speed_10m'], 1)
        
        text = (
            "Доброго ранку, Одесо! 🌊⚓️\n\n"
            "Погода на сьогодні:\n"
            f"🌡 Температура: {temp}°C (відчувається як {feels_like}°C)\n"
            f"📝 На вулиці: {desc}\n"
            f"💧 Влажність: {humidity}%\n"
            f"💨 Вітер: {wind} м/с\n\n"
            "Бажаємо вам чудового та продуктивного дня! ✨"
        )
        
        # Отправка в Telegram через вашего бота
        tg_url = f"https://telegram.org{BOT_TOKEN}/sendMessage"
        requests.post(tg_url, json={"chat_id": CHANNEL_ID, "text": text})
        print("Успешно отправлено!")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    run_bot()
