from flask import Flask, request, jsonify, send_from_directory
import openai
import os

app = Flask(__name__)

# ✅ OpenAI API Key
OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

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
        # 🔹 Old 0.28.0 syntax
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}],
            max_tokens=150
        )
        ai_text = response['choices'][0]['message']['content'].strip()
        return jsonify({"response": ai_text})

    except Exception as e:
        print("Error connecting to OpenAI API:", e)
        return jsonify({"response": f"⚠️ Error connecting to AI: {e}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)





