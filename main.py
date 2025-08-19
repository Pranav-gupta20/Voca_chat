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






