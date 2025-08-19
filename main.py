from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)  # allow frontend to call backend

# ✅ Use your OpenAI API key stored in Render env variable
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"reply": "No message received"}), 400

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_message,
            max_tokens=150
        )
        reply = response.choices[0].text.strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"⚠️ Error: {str(e)}"}), 500

@app.route("/")
def home():
    return "Backend is running! Use /chat with POST requests."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
