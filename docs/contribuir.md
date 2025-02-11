---
hide:
  - navigation
---

# Contribuir e Rodar Projeto

## Como Contribuir

Quer contribuir com o projeto? Siga estas etapas:

### Criação de Issues
Antes de implementar qualquer mudança, verifique se já existe uma issue relacionada. Caso contrário, crie uma nova issue descrevendo o problema ou a melhoria proposta.

### Criando um Pull Request
1.Faça um fork do repositório e clone-o localmente
```bash
git clone https://github.com/unb-mds/2024-2-Squad06.git
cd 2024-2-Squad06
```

2. Crie uma branch para a sua contribuição:
```bash
git checkout -b minha-nova-feature
```

3. Implemente as mudanças e siga as boas práticas de código.

4. Formate o código com Black:
```bash
black .
```

5. Adicione e faça o commit das mudanças:
```bash
git add .
git commit -m "Descrição breve da mudança"
```

6. Envie as alterações para o seu fork:
```bash
git push origin minha-nova-feature
```

7. Crie um Pull Request no repositório principal e aguarde a revisão.

## Como Rodar o Projeto

1. Clone o repositório:
```bash
git checkout -b minha-nova-feature
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente (se necessário).

5. Aplique as migrações:
```bash
python manage.py migrate
```

6. Inicie o servidor:
```bash
python manage.py runserver
```