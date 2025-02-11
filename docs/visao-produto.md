---
hide:
  - navigation
---

# Visão do Produto

O **Monitoramento de Gastos Públicos de Maceió** é um projeto desenvolvido no contexto da disciplina de Métodos de Desenvolvimento de Software, com o objetivo de criar uma plataforma acessível e intuitiva para a visualização das contratações publicadas nos diários oficiais do município. A iniciativa busca facilitar o acesso a informações detalhadas sobre fornecedores e valores envolvidos, promovendo maior transparência na alocação dos recursos públicos. Além disso, a plataforma permitirá identificar os 10 fornecedores mais recorrentes e visualizar valores mensais ou anuais (quando disponíveis), contribuindo para o controle social e a fiscalização da gestão pública.

## Problema a Ser Resolvido

O projeto busca solucionar a dificuldade de acesso e compreensão dos dados sobre contratações e despesas públicas. Atualmente, os diários oficiais disponibilizam essas informações de forma fragmentada e pouco acessível para a maioria dos cidadãos. A ausência de ferramentas adequadas dificulta a análise dos dados, a identificação de fornecedores recorrentes e a verificação de padrões de gastos. O Monitoramento de Gastos Públicos de Maceió visa tornar essas informações mais acessíveis, organizadas e fáceis de interpretar, permitindo que cidadãos e pesquisadores tenham um panorama claro das contratações realizadas pelo município.

## Objetivo

O principal objetivo do projeto é desenvolver uma plataforma que exiba de forma clara e interativa as contratações presentes em cada diário oficial do município de Maceió. As metas incluem:

1. **Facilitar o acesso aos dados**: Disponibilizar informações estruturadas sobre fornecedores, valores e contratos de maneira acessível para qualquer cidadão.
2. **Identificação de fornecedores recorrentes**: Destacar os 10 fornecedores mais frequentes nas contratações do município.
3. **Interface simples e intuitiva**: Garantir uma experiência de navegação fluida e acessível para usuários sem conhecimentos técnicos.

## Tecnologias Utilizadas

- **Frontend**: React com TypeScript e TailwindCSS para uma interface dinâmica, responsiva e moderna. O deploy é realizado na **Vercel**.
- **Python**: Linguagem de programação empregada para o desenvolvimento do backend e para a automação de processos.
- **Backend**: Desenvolvido em Python com Django Rest Framework (DRF) para criação de APIs RESTful e gerenciamento eficiente dos dados. O deploy é feito na **Railway**.
- **Banco de Dados**: MySQL, utilizado para armazenar os dados das contratações e garantir consultas eficientes.
- **Extração de Dados**: Utilização da **API Querido Diário** para obter os diários oficiais e processar as informações.
- **Automação**: O carregamento diário dos dados é realizado automaticamente através de um **CronBot programado no GitHub Actions**.

## Posição do Produto

Este projeto se posiciona como uma ferramenta de transparência pública e controle social, voltada para o fortalecimento da cidadania e o incentivo à educação. Seu público-alvo inclui:

- **Cidadãos**: Pessoas interessadas em acompanhar as contratações do município e entender como os recursos estão sendo utilizados.
- **Estudantes e pesquisadores**: Indivíduos que utilizam a plataforma para análises sobre gestão pública, transparência e controle social.
- **Profissionais da área pública**: Servidores e gestores que precisam de uma visão estruturada das contratações para melhorar a fiscalização e a eficiência na gestão dos recursos.