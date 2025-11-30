from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/orders")
def orders():
    return jsonify([
        {"order_id": 101, "user_id": 1, "item": "Notebook"},
        {"order_id": 102, "user_id": 2, "item": "Mouse Gamer"},
        {"order_id": 103, "user_id": 1, "item": "Teclado Mecanico novo"}
    ])

@app.get("/")
def root():
    return jsonify({"service": "orders", "status": "online"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)