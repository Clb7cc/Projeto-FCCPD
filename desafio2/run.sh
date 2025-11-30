#!/bin/bash

echo "Subindo containers..."
docker compose up -d
sleep 5

echo "Consulta inicial:"
docker exec -i desafio2_db psql -U user -d desafio2 -c "SELECT * FROM clientes;"

echo "Derrubando containers..."
docker compose down
sleep 3

echo "Subindo containers novamente..."
docker compose up -d
sleep 5

echo "Consulta após recriação:"
docker exec -i desafio2_db psql -U user -d desafio2 -c "SELECT * FROM clientes;"

echo "Processo concluído."
bash run.sh
