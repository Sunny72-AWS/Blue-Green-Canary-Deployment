from flask import Flask, jsonify
import os

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "1.0")
APP_COLOR = os.getenv("APP_COLOR", "blue")


@app.route("/")
def home():
    return jsonify({
        "project": "Blue-Green Canary Deployment",
        "application": "AWS Flask Application",
        "version": APP_VERSION,
        "environment": APP_COLOR,
        "status": "Running Successfully"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "Healthy",
        "version": APP_VERSION,
        "environment": APP_COLOR
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
