from flask import Flask, request
import requests

app = Flask(__name__)

VERIFY_TOKEN = "sultan123"

@app.route('/')
def home():
    return "Sultan Bot is Live!"

@app.route('/webhook', methods=['GET'])
def verify():
    if request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Verification failed", 403

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print(data)
    return "ok", 200

if __name__ == '__main__':
    app.run()
