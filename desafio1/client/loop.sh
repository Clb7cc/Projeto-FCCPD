#!/bin/bash

while true; do
    echo "Requisição :"
    curl -s http://webserver:8080
    echo ""
    sleep 5
done