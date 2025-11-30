from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/users")
def users():
    return jsonify([
        {"id": 1, "name": "Caio Bezerra"},
        {"id": 2, "name": "Julia Zeferino"},
        {"id": 3, "name": "Ana Souza"}
    ])

@app.get("/")
def root():
    return jsonify({"service": "users", "status": "online"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)