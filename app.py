import os
import requests
from flask import Flask, request, Response

app = Flask(__name__)

TELEGRAM_BASE = "https://api.telegram.org"

@app.route('/<path:path>', methods=['GET', 'POST'])
def proxy(path):
    url = f"{TELEGRAM_BASE}/{path}"
    try:
        if request.method == 'POST':
            resp = requests.post(url, json=request.get_json(), timeout=30)
        else:
            resp = requests.get(url, params=request.args, timeout=30)
        return Response(resp.content, status=resp.status_code, content_type=resp.headers.get('Content-Type', 'application/json'))
    except Exception as e:
        return Response(f"Proxy error: {e}", status=502)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
