import requests
from flask import Flask, jsonify

app = Flask(__name__)

SERVICE_A_URL = "http://service-a:5001/users"

@app.get("/info")
def get_info():
    try:
        users = requests.get(SERVICE_A_URL).json()
        combined = [
            f"Usuário {u['name']} ativo desde {u['active_since']}"
            for u in users
        ]
        return jsonify(combined)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.get("/")
def home():
    return "Serviço B - Consome o Serviço A"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)