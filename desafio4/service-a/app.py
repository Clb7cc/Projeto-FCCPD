from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/users")
def get_users():
    users = [
        {"id": 1, "name": "Caio", "active_since": "2022"},
        {"id": 2, "name": "Julia", "active_since": "2023"},
        {"id": 3, "name": "Marcos", "active_since": "2021"},
    ]
    return jsonify(users)

@app.get("/")
def home():
    return "Serviço A - API de Usuários"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)