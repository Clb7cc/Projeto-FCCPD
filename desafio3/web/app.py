from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Web funcionando"

@app.route("/db")
def db_test():
    return "Teste com DB"

@app.route("/cache")
def cache_test():
    return "Teste com Redis"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
