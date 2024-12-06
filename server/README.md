# Backend - Guia de Uso e Organização

Este documento descreve como inicializar e trabalhar com o backend deste projeto, desenvolvido com Django. Inclui orientações sobre estrutura, rotas e instruções de execução.

## **Como Executar o Backend**

Siga os passos abaixo para configurar e iniciar o servidor backend:

1. **Instale as dependências**:
   Certifique-se de que o ambiente virtual está ativado e instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

2. **Aplique as migrações**:
   Configure o banco de dados inicial executando:

   ```bash
   python manage.py migrate
   ```

3. **Execute o servidor**:
   Inicie o servidor de desenvolvimento:

   ```bash
    python manage.py runserver
   ```

4. **Acesse a aplicação**:
   O servidor estará disponível no endereço padrão:
   ```
    http://127.0.0.1:8000
   ```
   Nessa aplicação já tem uma rota pronta, que é :
   ```
    http://127.0.0.1:8000/api/example/
   ```
   Que ao acessa ou fazer requisição a ela deve-se retornar:
   ```
   message:"Hello from Django!"
   ```

## **Estrutura do Projeto**

A estrutura do backend segue o seguinte formato:

```
server/
├── apps/
│   ├── __init__.py
│   └── gastos_publicos/
│       ├── __init__.py
│       ├── apps.py
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       ├── routes/
│       │   ├── __init__.py
│       │   └── example_routes.py
│       ├── services/
│       │   ├── __init__.py
│       │   └── example_service.py
│       ├── middlewares/
│       │   ├── __init__.py
│       │   └── example_middleware.py
│       └── utils/
│           ├── __init__.py
│           └── example_util.py
├── manage.py
├── requirements.txt
└── settings/
    ├── __init__.py
    ├── base.py
    ├── development.py
    └── production.py
```

### **Descrição dos Diretórios**

- `apps/gastos_publicos/`:
  Diretório principal para o app `gastos_publicos`. Contém lógica de negócio, rotas, serviços, middlewares e utilitários.

- `routes/`:
  Arquivos para organização das rotas do app. Exemplo:

  ```python
  from django.urls import path
  from . import views

  urlpatterns = [
      path('example/', views.example_view, name='example'),
  ]
  ```

- `services/`:
  Contém classes e funções reutilizáveis para lógica de negócio mais complexa. Exemplo:

  ```python
  def process_data(data):
      # Lógica para processamento de dados
      return processed_data
  ```

- `middlewares/`:
  Arquivos de middlewares para interceptação e manipulação de requisições/respostas. Exemplo:

  ```python
  def example_middleware(get_response):
      def middleware(request):
          # Lógica antes da view
          response = get_response(request)
          # Lógica após a view
          return response

      return middleware
  ```

- `utils/`:
  Funções auxiliares e utilitárias para suporte ao restante do código. Exemplo:

  ```python
  def format_date(date):
      return date.strftime('%Y-%m-%d')
  ```

- `settings/`:
  Configurações do Django organizadas em módulos para diferentes ambientes (ex: desenvolvimento e produção).

## **Como Construir Novas Rotas**

Para adicionar uma nova rota ao projeto:

1. **Crie uma função de view**:
   No arquivo `views.py`, crie a lógica que será chamada pela rota:

   ```python
   from django.http import JsonResponse

   def new_view(request):
       return JsonResponse({'message': 'Hello, world!'})
   ```

2. **Adicione a rota**:
   No arquivo `urls.py`, registre a nova view:

   ```python
   from django.urls import path
   from .views import new_view

   urlpatterns = [
       path('new-endpoint/', new_view, name='new_endpoint'),
   ]
   ```

3. **Acesse a nova rota**:
   Após iniciar o servidor, acesse a rota no navegador:
   ```
    http://127.0.0.1:8000/new-endpoint/
   ```

## **Boas Práticas**

- Mantenha as funções pequenas e focadas em uma única responsabilidade.
- Organize o código utilizando serviços e utilitários sempre que possível.
- Documente as funções e rotas para facilitar a manutenção do projeto.
- Utilize middlewares para lógica que precisa ser executada em todas as requisições.
- Separe as configurações por ambiente no diretório `settings/`.
