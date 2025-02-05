# 💻 Monitoramento de Gastos Públicos - backend

Este repositório contém a parte do backend do projeto Monitoramento de Gastos Públicos, desenvolvido para a disciplina Métodos de Desenvolvimento de Software na Universidade de Brasília (UnB) durante o segundo semestre de 2024.

## 🗂️ Sumário

- [💻 Monitoramento de Gastos Públicos - backend](#-monitoramento-de-gastos-públicos---backend)
  - [🗂️ Sumário](#️-sumário)
  - [📜 Descrição do backend](#-descrição-do-backend)
  - [🛠️ Ferramentas Utilizadas](#️-ferramentas-utilizadas)
  - [🚀 Como Executar o back](#-como-executar-o-back)
  - [📚 Documentação](#-documentação)
  - [👥 Colaboradores](#-colaboradores)
  - [📍 Licença](#-licença)

## 📜 Descrição do backend

O **backend do Monitoramento de Gastos Públicos** é responsável por interagir com a API Querido Diário, extraindo as informações relacionadas aos gastos públicos de Maceió, AL, e processar esses dados.O backend automatiza a coleta e a formatação dos dados, garantindo que o frontend sempre tenha acesso às informações atualizadas para o monitoramento dos gastos.

## 🛠️ Ferramentas Utilizadas

- **Python**:  Linguagem de programação utilizada para o desenvolvimento do backend e automações.
- **Django**: Framework utilizado para a criação do backend, gerenciamento de banco de dados e APIs REST.
- **Querido Diário**: Biblioteca utilizada para a extração automatizada de dados dos diários oficiais de Maceió, AL, facilitando o acesso a informações sobre gastos públicos municipais.

## 🚀 Como Executar o back

1. Execute na pasta raiz do projeto:

    ```bash
    docker compose up --build -d
    ```

2. Navegue até a pasta server:
   
    ```bash
    cd server
    ```

3. crie um arquivo .env e insira as seguintes linhas de código no arquivo :

    ```
    - DB_NAME=YOUR_DB_NAME
    - DB_USER=YOUR_DB_USER
    - DB_PASSWORD=YOUR_DB_PASSWORD
    - DB_HOST=YOUR_DB_HOST
    ```

4. Crie as migrações do banco de dados::

    ```bash
    python manage.py makemigrations
    ```

5. Aplique as migrações no banco de dados:

    ```bash
    python manage.py migrate
    ```


6. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

## 📚 Documentação

A documentação completa do projeto pode ser acessada [neste link](https://unb-mds.github.io/2024-2-Squad06/).

## 👥 Colaboradores

<center>
<table style="margin-left: auto; margin-right: auto;">
    <tr>
        <td align="center">
            <a href="https://github.com/Neoprot">
                <img style="border-radius: 50%;" src="https://github.com/Neoprot.png" width="150px;"/>
                <h5 class="text-center">Kauã<br>Seichi</h5>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/TiagoTeixeira-2005">
                <img style="border-radius: 50%;" src="https://github.com/TiagoTeixeira-2005.png" width="150px;"/>
                <h5 class="text-center">Tiago<br>Lemes</h5>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/Ana-Luiza-SC">
                <img style="border-radius: 50%;" src="https://github.com/Ana-Luiza-SC.png" width="150px;"/>
                <h5 class="text-center">Ana<br>Luiza</h5>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/ArthurGuilher62">
                <img style="border-radius: 50%;" src="https://github.com/ArthurGuilher62.png" width="150px;"/>
                <h5 class="text-center">Arthur<br>Guilherme</h5>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/NayraNery127">
                <img style="border-radius: 50%;" src="https://github.com/NayraNery127.png" width="150px;"/>
                <h5 class="text-center">Nayra</h5>
            </a>
        </td>
         <td align="center">
            <a href="https://github.com/alvesingrid">
                <img style="border-radius: 50%;" src="https://github.com/alvesingrid.png" width="150px;"/>
                <h5 class="text-center">Ingrid<br>Alves</h5>
            </a>
        </td>
</table>
</center>

## 📍 Licença

Este projeto está licenciado sob a [Licença MIT](https://github.com/unb-mds/2024-2-Squad06/blob/main/LICENSE).
