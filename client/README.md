[![React version](https://img.shields.io/badge/react-18.2.0-blue)](https://reactjs.org/)
[![tailwind](https://img.shields.io/badge/tailwind-3.4.16-blue)](https://github.com/tailwindlabs/tailwindcss/releases/tag/v3.4.16)
[![TypeScript version](https://img.shields.io/badge/typescript-3.4.5-blue)](https://www.typescriptlang.org/)

# 💻 Monitoramento de Gastos Públicos - Frontend

Este repositório contém a parte do frontend do projeto Monitoramento de Gastos Públicos, desenvolvido para a disciplina Métodos de Desenvolvimento de Software na Universidade de Brasília (UnB) durante o segundo semestre de 2024.

## 🗂️ Sumário

- [💻 Monitoramento de Gastos Públicos - Frontend](#-monitoramento-de-gastos-públicos---frontend)
  - [🗂️ Sumário](#️-sumário)
  - [📜 Descrição do Frontend](#-descrição-do-frontend)
  - [🛠️ Ferramentas Utilizadas](#️-ferramentas-utilizadas)
  - [🚀 Como Executar o Front](#-como-executar-o-front)
  - [📚 Documentação](#-documentação)
  - [👥 Colaboradores](#-colaboradores)
  - [📍 Licença](#-licença)

## 📜 Descrição do Frontend

O **frontend do Monitoramento de Gastos Públicos** fornece uma interface interativa e acessível para exibir os dados do banco de dados de forma clara e eficiente. Ao acessar o site, o usuário pode realizar buscas por fornecedor e aplicar filtros, como valor mensal, data de assinatura e data de publicação. Os resultados filtrados são apresentados com detalhes sobre os gastos.

## 🛠️ Ferramentas Utilizadas

- **React (v18.2.0)**: Biblioteca JavaScript para a construção da interface do usuário, permitindo a criação de componentes dinâmicos e reativos para uma experiência fluida e interativa.
- **TailwindCSS (v3.4.16)**: Para a construção da estrutura e estilização das páginas web, garantindo uma interface visual atraente e responsiva.
- **Typescript (v3.4.5)**: Superset de JavaScript com tipagem estática, utilizado para aumentar a segurança e facilitar a manutenção do código no desenvolvimento frontend.

## 🚀 Como Executar o Front

1. Clone o repositório para sua máquina local utilizando o comando:

    ```bash
    git clone <https://github.com/unb-mds/2024-2-Squad06.git>
    ```

2. Navegue até a pasta client:
   
    ```bash
    cd client
    ```
3. Crie um .env na pasta `client/` desse jeito:

    ```.env
    REACT_APP_API_BASE_URL=YOUR_REACT_APP_API_BASE_URL
    ```

4. Instale as dependências necessárias utilizando o NPM:

    ```bash
    npm install
    ```

5. Inicie o servidor de desenvolvimento:

    ```bash
    npm start
    ```

5. Acesse o servidor no `http://localhost:8000/`.

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
