from flask import Flask
import requests

app = Flask(__name__)

SERVICE_A_URL = "http://service_a:5001/users"

@app.route("/process")
def process():
    try:
        response = requests.get(SERVICE_A_URL)
        users = response.json()

        result = []
        for u in users:
            result.append(f"Usuário {u['nome']} ativo desde 2024")

        return "\n".join(result)

    except Exception as e:
        return f"Erro ao comunicar com service A: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)