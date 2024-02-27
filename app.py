from flask import Flask, request, jsonify
from Chat import get_response
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/chat", methods=["POST"])
def chat():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
# waitress-serve --listen=127.0.0.1:8000 app:app