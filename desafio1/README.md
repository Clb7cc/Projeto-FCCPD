# Desafio 1 - Comunicação entre Containers com Docker

Este projeto resolve o "Desafio 1" de Containers em Rede. O objetivo é demonstrar a comunicação entre dois serviços isolados (um cliente e um servidor) através de uma rede Docker customizada (bridge), utilizando DNS interno para resolução de nomes.

## 🏗️ Arquitetura e Decisões Técnicas

A solução foi orquestrada utilizando **Docker Compose**. A escolha se deu pela facilidade em definir a infraestrutura como código (IaC), garantindo que a rede e os containers subam na ordem correta com um único comando.

### Componentes:
1.  **Servidor (Server):**
    * **Tecnologia:** Python com Flask.
    * **Decisão:** Utilizei uma imagem `python:3.10-slim` para manter o container leve. O Flask foi escolhido pela simplicidade de criar um endpoint HTTP rápido.
    * **Porta:** O serviço escuta na porta `8080`.

2.  **Cliente (Client):**
    * **Tecnologia:** Alpine Linux + cURL + Shell Script.
    * **Decisão:** O Alpine foi escolhido por ser extremamente leve (aprox. 5MB). Criei um script shell (`run_tests.sh`) para gerenciar as requisições, permitindo customizar a URL de destino e o intervalo via variáveis de ambiente, sem necessidade de recompilar a imagem.

3.  **Rede (Networking):**
    * **Tipo:** Bridge (Customizada).
    * **Nome:** `minha-rede-customizada`.
    * **Funcionamento:** Ao colocar ambos os containers na mesma rede definida no Docker Compose, o Docker habilita a resolução de DNS automática. Isso permite que o `client` acesse o `server` apenas pelo nome do serviço, sem precisar saber o endereço IP.

---

## 📂 Estrutura do Projeto

```text
/
├── docker-compose.yml   # Orquestração dos serviços e rede
├── README.md            # Documentação
├── client/
│   ├── Dockerfile       # Receita da imagem do cliente
│   └── run_tests.sh     # Script de loop de requisições
└── server/
    ├── Dockerfile       # Receita da imagem do servidor
    └── app.py           # Código da aplicação Flask