# app.py
from flask import Flask, request, jsonify
import os
import requests  # Gemini API call ke liye

app = Flask(__name__)

# Gemini API key environment variable se
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("prompt", "")

    if not user_message:
        return jsonify({"response": "No message received."})

    # Gemini API call
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": user_message,
        "max_tokens": 150
    }

    try:
        response = requests.post("https://api.gemini.com/v1/complete", headers=headers, json=payload)
        response.raise_for_status()
        gemini_data = response.json()
        ai_text = gemini_data.get("text", "Sorry, I didn't get that.")
        return jsonify({"response": ai_text})
    except Exception as e:
        print("Error:", e)
        return jsonify({"response": "⚠️ Error connecting to AI."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
