import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Укажи сюда полную "Ссылку для вызова" твоей функции tg-bot
TARGET_URL = "https://functions.yandexcloud.net/d4eboud7qtgg5m6cr0js"

@app.route('/webhook', methods=['POST'])
def webhook():
    # Берём входящие данные от Telegram
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "message": "no data"}), 400

    # Пересылаем на Cloud Function
    try:
        resp = requests.post(TARGET_URL, json=data, headers={
            'Content-Type': 'application/json'
        }, timeout=10)
        # Возвращаем ответ от функции обратно Telegram (обычно просто 200 OK)
        return resp.content, resp.status_code
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
