from flask import Flask, request, jsonify, send_from_directory
from openai import OpenAI
import os

app = Flask(__name__)

# ✅ OpenAI API Key
OPENAI_API_KEY = "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"

# Initialize client
client = OpenAI(api_key=OPENAI_API_KEY)

@app.route("/")
def index():
    return send_from_directory('.', 'index.html')

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"response": "No message received."})

    try:
        # 🔹 New 1.x Chat API syntax
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}],
            max_tokens=150
        )
        ai_text = response.choices[0].message.content.strip()
        return jsonify({"response": ai_text})

    except Exception as e:
        print("Error connecting to OpenAI API:", e)
        return jsonify({"response": f"⚠️ Error connecting to AI: {e}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)






