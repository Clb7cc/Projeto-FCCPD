# Desafio 4 — Microsserviços Independentes com Comunicação via HTTP

## Objetivo
Criar dois microsserviços independentes que se comunicam via HTTP, cada um com seu próprio Dockerfile, e orquestrados pelo Docker Compose.

---

## Arquitetura do Projeto

```
PROJETO-FCCPD/desafio4
│
├── service_a/     → Produtor de dados (lista usuários)
│   ├── app.py
│   └── Dockerfile
│
├── service_b/     → Consumidor (chama service A)
│   ├── app.py
│   └── Dockerfile
│
├── docker-compose.yml
└── run.sh         → Teste automatizado
```

---

## Descrição dos Microsserviços

### **Service A (Produtor)**
- Porta interna: **5001**
- Endpoint: **/users**
- Retorna JSON com usuários:
```json
[
  {"id": 1, "nome": "Caio"},
  {"id": 2, "nome": "Julia"},
  {"id": 3, "nome": "João"}
]
```

### **Service B (Consumidor)**  
- Porta interna: **5002**
- Endpoint: **/process**
- Consome o Service A e monta frases:
```
Usuário Caio ativo desde 2024
Usuário Julia ativo desde 2024
Usuário João ativo desde 2024
```

---

## Execução com Docker Compose

Dentro da pasta `desafio4`:

```bash
docker compose up -d
```

Para parar:

```bash
docker compose down
```

---

## Teste Automático (run.sh)

Execute:

```bash
bash run.sh
```

O script testa:

1. Service A → `/users`
2. Service B → `/process`
3. Confirma a comunicação entre eles

Saída esperada:

```
[Service A] lista de usuários json
[Service B] Usuário Caio ativo desde 2024 ...
```

---

## Conclusão

Este desafio demonstra:
- Microsserviços isolados
- Comunicação HTTP direta
- Dockerfiles independentes para cada serviço
- Orquestração com Docker Compose
- Teste automatizado validando ambos os serviços
