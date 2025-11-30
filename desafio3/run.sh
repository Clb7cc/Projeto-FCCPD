#!/bin/bash

echo "Subindo serviços..."
docker compose up -d

echo "Aguardando serviços iniciarem..."
sleep 5

echo -e "\nTestando rota principal:"
curl -s http://localhost:8080/

echo -e "\n\nTestando comunicação com o banco:"
curl -s http://localhost:8080/db

echo -e "\n\nGravando valor no Redis:"
curl -s http://localhost:8080/cache/set

echo -e "\n\nLendo valor do Redis:"
curl -s http://localhost:8080/cache/get

echo -e "\n\nTeste completo."
