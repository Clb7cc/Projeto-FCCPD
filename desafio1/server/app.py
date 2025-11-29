from flask import Flask
import sys

app = Flask(__name__)

@app.route("/")
def home():
    print("Recebi uma requisicao!", file=sys.stderr, flush=True)
    return "Eae jorge, tudo certo"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)