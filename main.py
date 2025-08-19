from flask import Flask, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__)

# Serve frontend
@app.route("/")
def index():
    return send_from_directory('.', 'index.html')

# Chat endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message") or data.get("prompt")
    
    # Gemini API request
    api_key = os.environ.get("OPENAI_API_KEY")
    headers = {"Authorization": f"Bearer {api_key}"}
    payload = {"input": user_message}
    
    # Replace URL with your Gemini API endpoint
    response = requests.post("https://api.gemini.example.com/v1/chat", headers=headers, json=payload)
    resp_json = response.json()
    
    # Example: adjust depending on Gemini response structure
    ai_response = resp_json.get("response", "Sorry, I didn't get that.")
    return jsonify({"response": ai_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

