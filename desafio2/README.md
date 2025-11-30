$readmeContent = @'
# Desafio 2: Persistência de Dados com Docker + PostgreSQL + Volumes

## Objetivo
Demonstrar que containers Docker não mantêm dados após serem destruídos, mas volumes sim.

O teste mostra claramente que, mesmo apagando o container, os dados continuam preservados.

## Descrição do Projeto
O projeto consiste em:

* Um container PostgreSQL configurado pelo `docker-compose.yml`.
* Um script SQL (`init.sql`) que cria e popula uma tabela na primeira inicialização.
* Um script automatizado (`run.sh`) que executa todo o fluxo:
    * subir o container
    * consultar dados
    * destruir o container
    * subir novamente
    * consultar de novo para provar que os dados persistiram

## Estrutura do Projeto

### 1. docker-compose.yml
Contém:
* Serviço `db` usando a imagem oficial `postgres:15`.
* Variáveis de ambiente para usuário, senha e nome do banco.
* **Dois volumes:**
    1.  Um volume nomeado `pgdata`, onde o banco armazena os dados permanentemente.
    2.  Um bind para `init.sql`, executado automaticamente apenas na primeira inicialização do volume.

**O que isso garante?**
Quando o container é recriado, o PostgreSQL não roda o `init.sql` novamente — apenas reaproveita os dados já gravados no volume.

### 2. init.sql
Arquivo SQL puro executado apenas na primeira criação do volume.
Ele:
* Cria a tabela `clientes` (se não existir).
* Insere dados iniciais (ex: João, Maria, Pedro).

Assim garantimos um estado inicial conhecido para testar a persistência.

### 3. run.sh
Script shell automatizado que executa todo o ciclo de teste:

1.  **Sobe o banco de dados:**
    ```bash
    docker compose up -d
    ```
2.  **Executa uma consulta SQL dentro do container:**
    ```bash
    docker exec -it desafio2_db psql -U postgres -d desafio2 -c "SELECT * FROM clientes;"
    ```
3.  **Derruba o container (mas não o volume):**
    ```bash
    docker compose down
    ```
4.  **Sobe o banco novamente:**
    ```bash
    docker compose up -d
    ```
5.  **Executa a mesma consulta para provar que os dados continuam lá.**

**Resultado esperado:**
Os dados aparecem antes e depois da destruição do container, provando a persistência.

## Como Funciona a Persistência
O volume `pgdata` funciona como um “armazenamento externo” do banco.

1.  Quando o container é destruído, o volume **não** é apagado.
2.  Quando um novo container é criado, o volume é reutilizado, incluindo:
    * tabelas
    * dados
    * configurações internas do PostgreSQL

Dessa forma, o estado do banco permanece intacto entre recriações do container.

## Passo a Passo Para Executar (WSL recomendado)

1.  **Entre no diretório do desafio**
    ```bash
    cd Projeto-FCCPD/desafio2
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
    Você verá:
    * Primeira consulta → dados aparecem
    * Container destruído
    * Container recriado
    * Segunda consulta → os mesmos dados permanecem

## Conclusão
Este desafio prova claramente que:
* Containers são descartáveis por natureza.
* Volumes Docker mantêm os dados independentemente da vida útil do container.
* O PostgreSQL, ao reiniciar usando o mesmo volume, mantém exatamente o mesmo estado anterior.
'@

Set-Content -Path "README.md" -Value $readmeContent -Encoding UTF8
Write-Host "Arquivo README.md criado com sucesso!" -ForegroundColor Green