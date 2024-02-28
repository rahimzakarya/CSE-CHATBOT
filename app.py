from flask import Flask, request, jsonify
from Chat import get_response
app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

# Add a route for a hello world message
@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()
# waitress-serve --listen=127.0.0.1:8000 app:app