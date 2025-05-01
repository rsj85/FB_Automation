from flask import Flask, request
import requests
import os
import json

app = Flask(__name__)

PAGE_ACCESS_TOKEN = 'EAAOqBk9pfb0BOwqzENiPEGA5564slErYxCei4xZAKgGvFZAEOGIxPrJdv7XOp0iM9qk9etODrtPEb4KjQ4Wr73T832PrAngiZANWZBYF09IrJ5tJ9WRFQcRqHzIEkD83oHlLH7xDOQX4YKKBLwf8NX5EXAKnSU4tOmZAHIXXBXnzGBZAzzNxmbqZCrT6URNvwZDZD'
VERIFY_TOKEN = 'my_fb_automation_token'


@app.route("/", methods=["GET"])
def index():
    return "Hello, this is the webhook server."


@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        # Verify token logic (already working)
        ...

    elif request.method == "POST":
        data = request.get_json()
        print("🔵 Full Webhook Payload:")
        print(json.dumps(data, indent=2))  # Pretty print for clarity

        for entry in data.get("entry", []):
            for event in entry.get("messaging", []):
                sender_id = event.get("sender", {}).get("id")
                message_text = event.get("message", {}).get("text")

                if sender_id and message_text:
                    print(f"✅ PSID: {sender_id} | Message: {message_text}")
                else:
                    print("⚠️ Event does not contain a user message.")

        return "EVENT_RECEIVED", 200


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
