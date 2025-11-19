from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/users")
def get_users():
    users = [
        {"id": 1, "name": "Caio"},
        {"id": 2, "name": "Julia"},
        {"id": 3, "name": "Marcos"}
    ]
    return jsonify(users)

@app.get("/")
def home():
    return "Users Service OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)