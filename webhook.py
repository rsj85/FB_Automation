from flask import Flask, request
import requests
import os

app = Flask(__name__)

PAGE_ACCESS_TOKEN = 'EAAOqBk9pfb0BO479ABHt6wAnaBgKX4FSqQrcpp6vNytzr8LQk757ZCydp8PYLCWx12WgczsQYSIkJZCIbBISxtKChsC4F25XVoGM5LP1ZBfmnqKfZAjYBYMUetkb0sxdhv24VA42joIICjhelhaG1TJiyDumfZBU1ZA1XMajUK7zkEiOV2iX8veYAwtO66JwZDZD'
VERIFY_TOKEN = 'my_fb_automation_token'


@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        # Facebook verification
        verify_token = "your_verify_token_here"
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == verify_token:
            return challenge, 200
        else:
            return "Verification failed", 403

    elif request.method == "POST":
        # Handle incoming messages here
        data = request.get_json()
        print(data)  # For now, just log it
        return "EVENT_RECEIVED", 200


@app.route("/")
def index():
    return "Hello, this is the webhook server."


def send_message(recipient_id, text):
    """Send a message to the recipient via the Send API."""
    url = "https://graph.facebook.com/v19.0/me/messages"
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": text},
        "messaging_type": "MESSAGE_TAG",
        "tag": "ACCOUNT_UPDATE"
    }
    headers = {"Content-Type": "application/json"}
    params = {"access_token": PAGE_ACCESS_TOKEN}

    response = requests.post(url, json=payload, headers=headers, params=params)
    print(response.status_code, response.text)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render provides this
    app.run(host="0.0.0.0", port=port)
