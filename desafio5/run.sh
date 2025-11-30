#!/bin/bash

echo "Subindo serviços..."
docker-compose up -d --build

echo "Aguardando serviços iniciarem..."
sleep 5

echo ""
echo "Testando rota /users do gateway:"
curl -s http://localhost:8000/users
echo ""

echo ""
echo "Testando rota /orders do gateway:"
curl -s http://localhost:8000/orders
echo ""

echo ""
echo "Teste completo."
