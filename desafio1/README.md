# Desafio 1: Containers em Rede

## Objetivo
Demonstrar a comunicação entre containers Docker através de uma rede personalizada, isolando a troca de dados entre um servidor web e um cliente automatizado.

## Descrição do Projeto
Uma arquitetura cliente-servidor simples rodando em containers distintos:
1.  **Servidor**: Uma API Flask que responde na porta 8080.
2.  **Cliente**: Um script em loop que consome essa API periodicamente.

## Estrutura dos Arquivos

### 1. `docker-compose.yml`
Configura a topologia da rede:
* **Services**:
    * `webserver`: Serviço Python/Flask. Exposto na porta 8080.
    * `client`: Serviço Alpine Linux. Possui `depends_on: webserver` para iniciar na ordem correta.
* **Networks**: Define a rede `desafio1_net` (driver bridge) para permitir a resolução de nomes (DNS interno).

### 2. Pasta `server/`
* **`app.py`**:
    * Rota `/`: Retorna um JSON simples (`{"message": "Servidor ativo!..."}`) para confirmar que a requisição chegou.
* **`Dockerfile`**:
    * Usa imagem `python:3.10-slim`.
    * Instala o framework Flask e expõe a aplicação.

### 3. Pasta `client/`
* **`loop.sh`**:
    * Script Bash que executa um `curl` para `http://webserver:8080` a cada 5 segundos.
    * Utiliza o nome do serviço (`webserver`) como endereço, provando que o DNS do Docker está funcionando.
* **`Dockerfile`**:
    * Usa imagem `alpine:latest` (leve).
    * Instala `curl` e `bash` para executar o script de loop.

### 4. `run.sh`
* Automação para subir o ambiente. Executa `docker compose up --build` para construir as imagens e iniciar os logs no terminal.

## Funcionamento
Ao subir o ambiente, o container `client` começa a "conversar" com o container `webserver`.
Como ambos estão na mesma rede (`desafio1_net`), o cliente não precisa saber o IP do servidor; ele apenas chama pelo nome definido no Compose (`webserver`).

## Como Rodar
1.  Dê permissão e inicie o ambiente:
    ```bash
    chmod +x run.sh
    ./run.sh
    ```
2.  Observe os logs no terminal:
    * Você verá mensagens repetidas a cada 5 segundos:
    ```text
     Requisição :
    {"message": "Servidor ativo! Comunicação funcionando."}
    ```