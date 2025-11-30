# Desafio 3 — Orquestração de Serviços com Docker Compose

## Objetivo
Demonstrar o uso do Docker Compose para orquestrar múltiplos serviços interdependentes (Web, Banco de Dados e Cache), validando a comunicação entre eles por meio de uma rede interna.

## Descrição do Projeto
O projeto consiste em:

* **web**: Aplicação Flask que serve como front-end e se comunica com os outros serviços.
* **db**: Banco de Dados PostgreSQL para persistência.
* **cache**: Redis para armazenamento rápido de dados temporários.
* Um script automatizado (`run.sh`) que sobe o ambiente e testa todos os endpoints de comunicação.

## Estrutura do Projeto

### 1. docker-compose.yml
O coração da orquestração. Ele define:
* **Serviços:** `web`, `db` e `cache`.
* **Rede Interna:** `desafio3_net`, permitindo que os containers se "enxerguem" pelo nome (hostname).
* **Dependências:** O serviço `web` só inicia após `db` e `cache` estarem prontos (`depends_on`).
* **Volumes:** Persistência de dados para o Postgres no volume `pgdata`.

**O que isso garante?**
Que não precisamos gerenciar IPs manualmente. A aplicação web acessa o banco simplesmente chamando o host `db` e o cache chamando o host `cache`.

### 2. web/app.py
A aplicação Python/Flask que expõe as rotas de teste:
* `/`: Verifica se o servidor web está online.
* `/db`: Tenta conectar no PostgreSQL.
* `/cache/set` e `/cache/get`: Grava e lê dados no Redis.

### 3. run.sh
Script shell automatizado que executa todo o ciclo de teste:

1.  **Sobe todos os serviços em background:**
    ```bash
    docker compose up -d
    ```
2.  **Aguarda a inicialização:**
    Pausa estratégica para garantir que o banco e o Redis estejam prontos para conexões.
3.  **Executa testes de comunicação (via `curl`):**
    Testa a rota principal, a conexão com o banco e as operações de escrita/leitura no cache.
4.  **Exibe o resultado final:**
    Mostra no terminal se todas as comunicações foram bem-sucedidas.

**Resultado esperado:**
O script deve reportar sucesso em todas as etapas ("Web funcionando", "DB OK", "Redis SET OK", "Redis GET: sucesso").

## Como Funciona a Orquestração
O Docker Compose cria um ambiente isolado onde:

1.  Uma **Rede Virtual** é criada automaticamente.
2.  O **DNS Interno** do Docker resolve os nomes dos serviços (`db`, `cache`) para seus respectivos IPs internos.
3.  O **Volume** `pgdata` garante que, mesmo se o serviço `db` cair, os dados do banco não sejam perdidos.

## Passo a Passo Para Executar (WSL recomendado)

1.  **Entre no diretório do desafio**
    ```bash
    cd Projeto-FCCPD/desafio3
    ```

2.  **Dê permissão ao script**
    ```bash
    chmod +x run.sh
    ```

3.  **Execute o teste completo**
    ```bash
    ./run.sh
    ```

4.  **Observe o resultado no terminal**
    Você verá a confirmação de que o container Web conseguiu falar com o Banco e com o Cache sem erros.

## Conclusão
Este desafio demonstra um cenário real de microserviços, provando que:
* O Docker Compose simplifica drasticamente a subida de múltiplos containers.
* A comunicação via *hostnames* na rede interna elimina a complexidade de configuração de rede.
* É possível integrar diferentes tecnologias (Python, Postgres, Redis) em um único comando.