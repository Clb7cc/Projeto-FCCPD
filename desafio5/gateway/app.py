from flask import Flask, jsonify
import requests

app = Flask(__name__)

USERS_SERVICE = "http://users-service:5001/users"
ORDERS_SERVICE = "http://orders-service:5002/orders"


@app.get("/users")
def users():
    response = requests.get(USERS_SERVICE)
    return jsonify(response.json())


@app.get("/orders")
def orders():
    response = requests.get(ORDERS_SERVICE)
    return jsonify(response.json())


@app.get("/")
def home():
    return "API Gateway ativo. Endpoints: /users e /orders"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)