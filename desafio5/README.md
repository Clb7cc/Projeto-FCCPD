# Desafio 5: Microsserviços com API Gateway

## Objetivo
Criar uma arquitetura de microsserviços utilizando um API Gateway como ponto único de entrada, centralizando o acesso a serviços independentes e orquestrando chamadas via HTTP.

## Descrição do Projeto
Uma arquitetura distribuída que isola os serviços de dados atrás de um gateway:
1.  **Gateway**: Recebe todas as requisições externas e as roteia.
2.  **Service Users**: Microserviço que fornece dados de usuários.
3.  **Service Orders**: Microserviço que fornece dados de pedidos.

## Estrutura dos Arquivos

### 1. `docker-compose.yml`
Configura a topologia da orquestração:
* **Services**:
    * `gateway`: Exposto na porta 8000. É o único acessível publicamente.
    * `service_users`: Roda na porta 5001 (interna).
    * `service_orders`: Roda na porta 5002 (interna).
* **Networks**: Define a rede para permitir que o Gateway resolva os nomes dos outros containers.

### 2. Pastas de Código (`gateway/`, `service_users/`, `service_orders/`)
* **`app.py` (Gateway)**:
    * Rota `/users`: Faz uma requisição HTTP interna para o container `service_users`.
    * Rota `/orders`: Faz uma requisição HTTP interna para o container `service_orders`.
* **`Dockerfile`**:
    * Cada pasta possui seu próprio Dockerfile para instalar Python, Flask e Requests, garantindo isolamento total das dependências.

### 3. `run.sh`
* Automação para o ciclo de vida. Executa a construção das imagens (`build`), sobe os containers (`up`) e realiza testes automáticos com `curl` para validar se o JSON está retornando corretamente através do Gateway.

## Funcionamento
Ao fazer uma requisição para o Gateway (`http://localhost:8000/users`), a aplicação Python dentro do Gateway atua como um "proxy".
Ela dispara uma nova chamada para `http://service_users:5001/users`, pega a resposta e devolve para quem chamou.
Isso comprova a comunicação entre containers distintos na rede Docker.

## Como Rodar
1.  Inicie o ambiente e os testes:
    ```bash
    ./run.sh
    ```
2.  Teste manualmente no navegador (ou via Postman):
    * Users via Gateway: `http://localhost:8000/users`
    * Orders via Gateway: `http://localhost:8000/orders`
