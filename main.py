import os
import json
import urllib.request
from flask import Flask

app = Flask(__name__)

def run_bot():
    try:
        # Этот код запрашивает у Telegram список последних действий бота, чтобы вытащить живой ID канала
        part1 = "https://api."
        part2 = "telegram"
        part3 = ".org/bot"
        token = "8959094212:AAEI5eaN8qGNnk5t8gAOIy7fVVLgNPuYpr4"
        
        # Запрашиваем обновления (активность) бота
        tg_url = part1 + part2 + part3 + token + "/getUpdates"
        req = urllib.request.Request(tg_url, headers={'User-Agent': 'Mozilla/5.0'})
        
        with urllib.request.urlopen(req, timeout=10) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            
        # Выводим все технические данные от Telegram на экран, чтобы увидеть ошибку или ID
        return f"<h1>Успішно підключено до Telegram!</h1><p>Системна відповідь сервера:</p><pre>{json.dumps(res_data, indent=4)}</pre>"
        
    except Exception as e:
        return f"<h1>⚠️ Помилка зчитування даних Telegram:</h1><p>{e}</p>"

@app.route('/', methods=['GET', 'HEAD'])
def index():
    return run_bot()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
