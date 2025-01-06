---
hide:
  - navigation
---


# User Stories
A partir de pesquisas e estudos de negócio realizados pela equipe, foi elaborado o seguinte documento contendo os requisitos do projeto, bem como seus critérios de aceitação e pontos de Sprint.

| Épico                    | User Stories                                                                                                    | Critério de aceitação                                                                                                                                                         | Pontos |
|--------------------------|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| *Acesso à dados gerais* | *US-01*           |Como usuário, quero entender o que são gastos públicos e licitações, para que eu possa compreender melhor os dados apresentados.<br> • Definir onde as explicações serão apresentadas (página inicial, seção de ajuda, tooltips). <br> • Garantir que a linguagem seja acessível a usuários leigos.              | 7      |
|                          | *US-02* |Como usuário, quero visualizar uma lista atualizada dos gastos do município, para que eu saiba quais despesas foram realizadas recentemente.<br> • Especificar o comportamento em caso de atrasos ou ausência de atualizações. <br> • Garantir que a data da última atualização seja visível para o usuário. <br> • Os dados devem ser atualizados de 1 em 1 semana. | 10     |
|                          | *US-03*        |Como usuário, quero acessar uma interface simples e intuitiva, para que eu possa visualizar os gastos públicos sem dificuldades.<br> • A interface deve apresentar, no máximo, 3 níveis de navegação, com textos de cabeçalho claros e ícones intuitivos. <br> • O layout deve ser responsivo e funcional em dispositivos com telas.                   | 9      |
| *Filtragem da pesquisa* | *US-04*                     |Como usuário, quero poder filtrar os fornecedores por recorrência e valor, para que eu identifique padrões de gasto.<br> • Especificar o formato de apresentação dos filtros (ex.: sliders, checkboxes). <br> • Incluir instruções claras para usuários ao aplicar múltiplos filtros.                | 9      |
|                          | *US-05* |Como usuário, quero uma barra de busca com filtros por categoria de gastos, para que eu encontre rapidamente as informações sobre a área que eu pesquisar.<br> • Detalhar a experiência do usuário ao utilizar o menu suspenso (ex.: número de categorias visíveis por vez). <br> • Garantir que o sistema retorne resultados relevantes rapidamente.                           | 8      |
|                          | *US-06*           |Como usuário, quero visualizar os contratos organizados por categorias, para que eu veja como os recursos estão distribuídos.<br> • Especificar se o resumo numérico inclui valores totais e quantidade de contratos. <br> • Detalhar como o campo de busca adicional será integrado às categorias.          | 8      |
| *Identificação de irregularidades* | *US-07* |Como usuário, quero visualizar gastos públicos que apresentem irregularidades, para que eu possa identificar possíveis problemas e acompanhá-los.<br> • Definir critérios claros para identificar irregularidades (ex.: limite percentual, atraso de pagamento). <br> • Garantir que os alertas visuais tenham contraste suficiente para acessibilidade.             | 10     |
|                          | *US-08* |Como usuário, quero acessar uma seção dedicada a despesas suspeitas, para que eu veja facilmente onde podem haver falhas ou má gestão.<br> • Indicar o layout da seção de despesas suspeitas (ex.: lista paginada ou infinita). <br> • Especificar a ordem padrão dos itens (por gravidade ou por data).              | 10     |
|                          | *US-09* |Como usuário, quero acessar uma página de "Despesas Suspeitas", para que eu possa ver facilmente onde podem haver falhas ou má gestão.<br> • A página deve exibir uma lista de despesas suspeitas com destaque visual. <br> • As despesas suspeitas devem ser organizadas por gravidade ou data. <br> • A página deve permitir filtros e pesquisa rápida. <br> • A descrição do motivo da suspeita deve ser visível. |        |
| *Representação gráfica* | *US-10* |Como usuário, quero receber alertas sobre irregularidades detectadas, para que eu me mantenha informado sobre desvios ou gastos atípicos.<br> • Definir como e quando as notificações em tempo real serão enviadas (ex.: imediatamente após detectar irregularidade). <br> • Permitir que o usuário escolha o método de notificação preferido (e-mail ou painel). | 3      |
|                          | *US-12* |Como usuário, quero acessar gráficos interativos que mostram padrões de despesas e contratos, para que eu compreenda melhor os dados apresentados.<br> • Definir os tipos de gráficos interativos (barras, pizza, etc.). <br> • Garantir que os filtros aplicados aos gráficos atualizem os dados dinamicamente.                  | 5      |
|                          | *US-13*                        |Como usuário, quero gráficos de fornecedores recorrentes, para que eu possa identificar padrões de contratação.<br> • O gráfico deve exibir claramente os fornecedores recorrentes, destacando aqueles com maior frequência de contratação. <br> • O gráfico deve ser interativo, permitindo ao usuário clicar para obter mais informações sobre os fornecedores. | 4      |



# Story Map e Mínimo Produto Viável (MVP):
Com base nos requisitos levantados, definimos dois MVPs para o projeto, priorizando entregas que
gerem valor rapidamente para os usuários. 

### Story Map
O Story Map encontra-se no seguinte link: [Link para o Story Map](https://www.figma.com/board/zxbXIqs4R1qCbUL5bejapG/User-story-mapping?node-id=1111-898&node-type=shape_with_text&t=tvNNdbYypqmcuZbr-0)

### MVP 1 – Entregas Iniciais

O **MVP 1** do *Monitoramento de Gastos Públicos de Maceió* focará nas funcionalidades essenciais para oferecer aos usuários acesso básico e intuitivo às informações sobre os gastos públicos. Este primeiro lançamento incluirá:

- **Página explicativa sobre licitações**: Conteúdo acessível para que os usuários compreendam o que são os gastos públicos e licitações.
- **Integração com a API "Querido Diário"**: Conectar à API para importar dados sobre os gastos municipais, com atualizações semanais.
- **Interface simples e intuitiva**: Layout responsivo e fácil de navegar, com filtros básicos para facilitar a busca de informações.
- **Testes de usabilidade**: Validação da usabilidade e interação com os dados.

O objetivo é garantir que os usuários consigam acessar e compreender os dados básicos de forma eficiente e clara.

### MVP 2 – Entrega Completa

O **MVP 2** expandirá as funcionalidades do sistema, oferecendo uma análise mais detalhada dos gastos públicos. Este lançamento incluirá:

- **Filtros avançados**: Mais opções para filtrar os dados por recorrência, valor e categorias específicas.
- **Identificação de irregularidades**: Detecção de gastos atípicos e alertas visuais sobre possíveis problemas.
- **Gráficos interativos**: Exibição de padrões de despesas e fornecedores recorrentes, com opções de filtragem dinâmica.
- **Despesas suspeitas**: Seção dedicada a exibir e filtrar despesas com possíveis irregularidades.

O **MVP 2** terá como foco oferecer uma análise mais profunda e ferramentas de visualização interativas para ajudar na compreensão dos padrões de gastos.

