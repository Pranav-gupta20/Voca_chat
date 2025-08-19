from flask import Flask, request, jsonify, send_from_directory
import requests

app = Flask(__name__)

# Direct Gemini API key (for testing only!)
GEMINI_API_KEY = "AIzaSyAlGcAiQoEwgeEtert1SQF3oRbtVARGlXs"

# Serve frontend
@app.route("/")
def index():
    return send_from_directory('.', 'index.html')

# Chat endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"response": "No message received."})

    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": user_message,
        "max_output_tokens": 150
    }

    try:
        response = requests.post(
            "https://api.generativeai.google/v1beta2/models/text-bison-001:generate",
            headers=headers,
            json=payload,
            timeout=10
        )
        response.raise_for_status()
        gemini_data = response.json()
        print("Gemini response:", gemini_data)

        ai_text = gemini_data.get("candidates", [{}])[0].get("output", "Sorry, I didn't get that.")
        return jsonify({"response": ai_text})

    except requests.exceptions.RequestException as e:
        print("Error connecting to Gemini API:", e)
        return jsonify({"response": "⚠️ Error connecting to AI."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


