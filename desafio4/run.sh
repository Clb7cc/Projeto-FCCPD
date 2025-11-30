#!/bin/bash

echo "Subindo microsserviços..."
docker compose up -d

echo "Aguardando iniciar..."
sleep 4

echo -e "\nTestando Service A:"
curl -s http://localhost:5001/users
echo ""

echo -e "\nTestando Service B:"
curl -s http://localhost:5002/process
echo ""

echo -e "\nTeste concluído."