from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/orders")
def get_orders():
    orders = [
        {"order_id": 101, "user_id": 1, "item": "Notebook"},
        {"order_id": 102, "user_id": 2, "item": "Mouse"},
        {"order_id": 103, "user_id": 3, "item": "Teclado"}
    ]
    return jsonify(orders)

@app.get("/")
def home():
    return "Orders Service OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)