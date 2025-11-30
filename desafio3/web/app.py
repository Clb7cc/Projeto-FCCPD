from flask import Flask
import psycopg2
import redis
import os

app = Flask(__name__)

# Configuração do PostgreSQL
db_host = os.getenv("DB_HOST", "db")
db_name = os.getenv("POSTGRES_DB", "desafio3")
db_user = os.getenv("POSTGRES_USER", "user")
db_password = os.getenv("POSTGRES_PASSWORD", "password")

# Configuração do Redis
redis_host = os.getenv("REDIS_HOST", "cache")
redis_port = 6379

@app.route("/")
def home():
    return "Web funcionando"

@app.route("/db")
def test_db():
    try:
        conn = psycopg2.connect(
            host=db_host, database=db_name, user=db_user, password=db_password
        )
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        result = cur.fetchone()
        conn.close()
        return f"DB OK: {result}"
    except Exception as e:
        return f"Erro DB: {str(e)}"

@app.route("/cache/set")
def cache_set():
    try:
        r = redis.Redis(host=redis_host, port=redis_port)
        r.set("teste", "sucesso")
        return "Redis SET OK"
    except Exception as e:
        return f"Erro Redis SET: {str(e)}"

@app.route("/cache/get")
def cache_get():
    try:
        r = redis.Redis(host=redis_host, port=redis_port)
        value = r.get("teste")
        return f"Redis GET: {value.decode()}"
    except Exception as e:
        return f"Erro Redis GET: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
