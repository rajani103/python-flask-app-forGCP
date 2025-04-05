from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    message = os.getenv("WELCOME_MSG", "Welcome to Cloud Run demo!")  # default if env var not set
    return jsonify({
        "message": message,
        "status": "success"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/env')
def env_demo():
    owner = os.getenv("APP_OWNER", "Not set")
    return jsonify({
        "environment": {
            "APP_OWNER": owner
        }
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
