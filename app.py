from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8688330377:AAG9WA9ynTsWJmp93l1cdGw7mpWLl4N3tlA"
CHAT_ID = "997414309"

def send_message(text):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": text
        }
    )

@app.route("/")
def home():
    return "BOT ONLINE"

@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.json

    signal = data.get("signal","")
    pair = data.get("pair","XAUUSD")
    profit = data.get("profit","")

    if signal == "TP":
        send_message(
            f"✅ TP preso\n{pair}\nProfitto: {profit}"
        )

    elif signal == "SL":
        send_message(
            f"❌ SL preso\n{pair}\nRisultato: {profit}"
        )

    return {"ok": True}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
