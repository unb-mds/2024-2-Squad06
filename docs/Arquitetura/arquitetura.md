---
hide:
  - navigation
---

# Arquitetura

## Introdução
O projeto de **Monitoramento de Gastos Públicos** tem como objetivo coletar dados da API do “Querido Diário” sobre os gastos dos municípios do estado de Alagoas e organizá-los de maneira que o usuário possa filtrar as informações conforme o município de interesse. Além disso, o sistema permitirá a visualização dos setores envolvidos, dos fornecedores e das possíveis irregularidades.

## Diagrama da Arquitetura
![Diagrama de Aquitetura](arquitetura.png)

## Visão Geral
A arquitetura do sistema é dividida em duas aplicações: o backend e o frontend.

### Backend

O backend é responsável por fornecer uma API REST, que oferece as seguintes funcionalidades:

- **Web Scraping**: Responsável pela coleta de dados da API do “Querido Diário”. O scraping acessa a página web, extrai informações relevantes e as armazena no banco de dados.

- **Cronbot**: Responsável por automatizar a execução do processo de scraping em intervalos programados, de forma que não se tenha a necessidade de intervenção manual.

- **Banco de Dados**: O banco de dados é responsável por armazenar os dados coletados e processados pelo sistema. Ele garante que as informações sobre os gastos públicos, fornecedores e municípios sejam armazenadas de forma segura, organizada e eficiente, permitindo acessos rápidos para consultas futuras.

### Frontend

O frontend é responsável por consumir os dados disponibilizados pelo banco de dados e apresentar as informações para o usuário. O fluxo da aplicação se dá da seguinte forma:

1. **Acesso ao site**: Ao acessar o site do Monitoramento de Gastos Públicos, o usuário é apresentado com a opção de login e uma funcionalidade de pesquisa de gastos públicos.
2. **Busca por município**: O usuário pode realizar a busca pelo município desejado, inserindo seu nome na barra de pesquisa.
3. **Filtragem de dados**: Após localizar o município, o usuário pode refinar os resultados, filtrando os gastos por setor e fornecedor.
4. **Visualização dos gastos**: Após aplicar os filtros, o usuário poderá visualizar os dados detalhados sobre os gastos e verificar a legalidade ou possíveis infrações associadas a cada gasto.

## Fluxo de Trabalho

O fluxo de trabalho do projeto pode ser representado da seguinte maneira:

1. **Coleta de Dados**: O CronBot realiza a raspagem de dados diretamente da API do “Querido Diário”, extraindo as informações relevantes sobre os gastos públicos.
2. **Processamento e Organização**: Os dados coletados são processados e organizados de forma que se tornem acessíveis e estruturados, permitindo a consulta por município, setor ou fornecedor.
3. **Armazenamento**: Os dados processados e organizados são armazenados de maneira eficiente e segura no banco de dados, garantindo acessos rápidos e ordenados.
4. **Verificação**: Após o armazenamento, os dados passam por uma verificação para avaliar a legalidade dos gastos, identificando possíveis irregularidades ou infrações.
5. **Visualização**: Os dados organizados e verificados serão disponibilizados em nosso site.

## Tecnologias Utilizadas 

| Tecnologia    | Versão   |
|---------------|----------|
| Python        | 3.x      |
| Django        | 4.x      |
| HTML          | HTML5    |
| CSS           | CSS3     |
| React         | 18.x     |
| TypeScript    | 4.x      |


