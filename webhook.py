from flask import Flask, request
import requests
import os

app = Flask(__name__)

PAGE_ACCESS_TOKEN = 'EAAOqBk9pfb0BOwqzENiPEGA5564slErYxCei4xZAKgGvFZAEOGIxPrJdv7XOp0iM9qk9etODrtPEb4KjQ4Wr73T832PrAngiZANWZBYF09IrJ5tJ9WRFQcRqHzIEkD83oHlLH7xDOQX4YKKBLwf8NX5EXAKnSU4tOmZAHIXXBXnzGBZAzzNxmbqZCrT6URNvwZDZD'
VERIFY_TOKEN = 'my_fb_automation_token'


@app.route("/", methods=["GET"])
def index():
    return "Hello, this is the webhook server."


@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        # Facebook verification
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            print("Webhook verified successfully")
            return challenge, 200
        else:
            print("Verification failed")
            return "Verification token mismatch", 403

    elif request.method == "POST":
        print("Webhook received a POST request")
        return "EVENT_RECEIVED", 200


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
