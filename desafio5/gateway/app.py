from flask import Flask, jsonify
import requests

app = Flask(__name__)

USERS_URL = "http://service_users:5001/users"
ORDERS_URL = "http://service_orders:5002/orders"

@app.get("/users")
def get_users():
    try:
        users = requests.get(USERS_URL).json()
        return jsonify(users)
    except:
        return jsonify({"error": "Erro ao acessar service_users"}), 500

@app.get("/orders")
def get_orders():
    try:
        orders = requests.get(ORDERS_URL).json()
        return jsonify(orders)
    except:
        return jsonify({"error": "Erro ao acessar service_orders"}), 500

@app.get("/")
def root():
    return jsonify({"gateway": "online", "endpoints": ["/users", "/orders"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)