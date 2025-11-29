#!/bin/sh

URL="${URL:-http://server:8080}"
INTERVAL="${INTERVAL:-3}"

sleep 5

while true; do
    RESPONSE=$(curl -s "$URL" || echo "Erro de conexão")
    echo "$(date '+%H:%M:%S') - $RESPONSE"
    sleep "$INTERVAL"
done