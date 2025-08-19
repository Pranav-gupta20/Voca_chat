from flask import Flask, request, jsonify
import os
import requests  # for calling Gemini API
from flask import Flask, request, jsonify, send_from_directory
app = Flask(__name__, static_folder='static')

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')



# Get Gemini API key from environment variable
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message") or data.get("prompt")

    if not user_message:
        return jsonify({"response": "No message received."})

    try:
        # Replace this with the actual Gemini API request structure
        response = requests.post(
            "https://api.gemini.example/chat",  # <-- Gemini endpoint
            headers={"Authorization": f"Bearer {GEMINI_API_KEY}"},
            json={"input": user_message}
        )
        response.raise_for_status()
        ai_response = response.json().get("response", "Sorry, I didn't get that.")
    except Exception as e:
        print("Error:", e)
        ai_response = "⚠️ Error connecting to AI."

    return jsonify({"response": ai_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))




