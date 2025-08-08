# app.py - very small Flask app
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(message="Hello from Flask microservice!")

if __name__ == "__main__":
    # In container we bind to 0.0.0.0 and port 8080 (GCP-friendly)
    app.run(host="0.0.0.0", port=8080)
