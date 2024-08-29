# projeto_filas 🚀

Projeto de testes para filas.

## Estrutura do Projeto  📂

- `.env`: Arquivo de configuração de variáveis de ambiente.
- `.gitignore`: Arquivo que especifica quais arquivos e diretórios devem ser ignorados pelo Git.
- `anotacoes.txt`: Arquivo de anotações diversas.
- `docker-compose.yml`: Arquivo de configuração do Docker Compose.
- `Dockerfile`: Arquivo de configuração para construção da imagem Docker.
- `entrypoint.sh`: Script de entrada para inicialização do container Docker.
- `Makefile`: Arquivo de automação de tarefas.
- `queue_module/`: Diretório contendo os módulos de fila.
  - `messager.py`: Script responsável por enviar mensagens para a fila.
  - `worker.py`: Script responsável por processar as mensagens da fila.
- `README.md`: Este arquivo.
- `requirements.txt`: Arquivo que lista as dependências do projeto.
- `run_messager.sh`: Script para executar o `messager.py`.

## Componentes Utilizados

### Docker

O projeto utiliza Docker para criar um ambiente isolado e consistente para execução dos serviços.

- **Dockerfile**: Define a imagem base e as instruções para construir a imagem Docker do projeto.
- **docker-compose.yml**: Define os serviços, redes e volumes necessários para a aplicação.

### Makefile

O `Makefile` contém comandos para facilitar a execução de tarefas comuns:

- `dcbuild`: Constrói as imagens Docker definidas no `docker-compose.yml`.
- `dcup`: Sobe os containers definidos no `docker-compose.yml` em modo destacado.
- `dcstop`: Para os containers em execução.
- `prune`: Remove todos os containers, imagens e volumes não utilizados.
- `dclogs`: Exibe os logs dos containers em tempo real.
- `remake`: Executa uma sequência de comandos para parar, limpar e reiniciar os containers.

### queue_module

O diretório `queue_module` contém os scripts principais do projeto:

- **messager.py**: Script responsável por enviar mensagens para a fila.
- **worker.py**: Script responsável por processar as mensagens da fila.

## Bibliotecas Utilizadas

As bibliotecas necessárias para o projeto estão listadas no arquivo `requirements.txt`. Certifique-se de instalar todas as dependências antes de executar os scripts.

## Propósito de Cada Container

- **messager**: Container responsável por enviar mensagens para a fila. Utiliza o script `messager.py`.
- **worker**: Container responsável por processar as mensagens da fila. Utiliza o script `worker.py`.

## Como Executar

1. Construa as imagens Docker:
    ```sh
    make dcbuild
    ```

2. Suba os containers:
    ```sh
    make dcup
    ```

3. Para visualizar os logs:
    ```sh
    make dclogs
    ```

4. Para parar os containers:
    ```sh
    make dcstop
    ```

5. Para limpar e reiniciar os containers:
    ```sh
    make remake
    ```
