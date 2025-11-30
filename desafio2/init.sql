CREATE TABLE IF NOT EXISTS clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255)
);

INSERT INTO clientes (nome) VALUES ('Caio'), ('Maria'), ('João');