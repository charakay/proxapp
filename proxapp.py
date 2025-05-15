from flask import Flask, request
import requests

app = Flask(__name__)

RECEIVER_URL = "https://<your-receiver-app>.choreo.dev/record"

@app.route("/proxy", methods=["POST", "GET"])
def proxy():
    headers = dict(request.headers)
    # Remove original IP headers
    headers.pop("X-Forwarded-For", None)

    # Forward the request to App B
    resp = requests.request(
        method=request.method,
        url=RECEIVER_URL,
        headers=headers,
        data=request.get_data()
    )
    return resp.content, resp.status_code
