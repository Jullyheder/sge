# Sistema de Gestão de Estoque (SGE)

Projeto Django desenvolvido durante o curso PycodeBR, com modificações próprias para praticar cadastro, movimentação e métricas de estoque.

## Sobre o projeto

O SGE é uma aplicação web para controle de estoque com autenticação, painel inicial com indicadores e operações de CRUD para as entidades básicas do domínio. O projeto também expõe endpoints REST protegidos por JWT e possui comandos para importação de dados via CSV.

## Funcionalidades atuais

- Autenticação de usuários com login/logout do Django.
- Usuário customizado com campos adicionais de cargo, raça/etnia e gênero.
- Dashboard inicial com métricas de produtos, vendas e gráficos por período, categoria e marca.
- Cadastro, listagem, detalhamento, edição e exclusão de:
  - marcas;
  - categorias;
  - fornecedores;
  - produtos.
- Cadastro, listagem e detalhamento de:
  - entradas de estoque;
  - saídas de estoque.
- Atualização automática da quantidade do produto:
  - entradas aumentam o estoque;
  - saídas reduzem o estoque.
- API REST com Django REST Framework.
- Autenticação JWT com `djangorestframework_simplejwt`.
- Importação de dados CSV para marcas, categorias, fornecedores, produtos, entradas e saídas.
- Suporte à execução local com SQLite ou em contêiner com PostgreSQL.

## Tecnologias

- Python 3.12
- Django 6.0.4
- Django REST Framework
- Simple JWT
- SQLite, para o ambiente local
- PostgreSQL, para o ambiente de desenvolvimento via Docker
- Docker e Docker Compose

## Estrutura principal

```text
.
+-- accounts/          # Usuário customizado
+-- app/               # Configurações, rotas principais, templates base e métricas
+-- authentication/    # Rotas de token JWT
+-- brands/            # Cadastro e API de marcas
+-- categories/        # Cadastro e API de categorias
+-- inflows/           # Entradas de estoque e signals
+-- outflows/          # Saídas de estoque, signals e notificação externa
+-- products/          # Cadastro e API de produtos
+-- services/          # Serviços auxiliares
+-- suppliers/         # Cadastro e API de fornecedores
+-- Dockerfile
+-- docker-compose.yml
+-- manage.py
+-- requirements.txt
```

## Configuração do ambiente

Crie um arquivo `.env` na raiz do projeto. Você pode usar `.env.example` como base:

```env
DJANGO_ENV=local
SECRET_KEY=sua-chave-secreta
ALLOWED_HOSTS=127.0.0.1,localhost
DEBUG=True

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=sge
POSTGRES_HOST=sge_db
POSTGRES_PORT=5432
```

Quando `DJANGO_ENV=local`, o projeto usa SQLite em `db.sqlite3`. Quando `DJANGO_ENV=development`, o projeto usa PostgreSQL com as variáveis `POSTGRES_*`.

## Como rodar localmente

Crie e ative um ambiente virtual:

```bash
python -m venv venv
```

No Windows:

```bash
venv\Scripts\activate
```

No Linux/macOS:

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute as migrações:

```bash
python manage.py migrate
```

Crie um superusuário:

```bash
python manage.py createsuperuser
```

Inicie o servidor:

```bash
python manage.py runserver
```

Acesse:

- Aplicação: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`
- Login: `http://127.0.0.1:8000/login/`

## Como rodar com Docker

Com Docker e Docker Compose instalados:

```bash
docker compose up --build
```

A aplicação ficará disponível em:

```text
http://127.0.0.1:8000/
```

O PostgreSQL do Compose fica exposto localmente na porta `5435` e usa, por padrão, o banco `sge`, usuário `postgres` e senha `postgres`.

## Rotas web

| Recurso | Rota base |
| --- | --- |
| Home/dashboard | `/` |
| Login | `/login/` |
| Logout | `/logout/` |
| Admin | `/admin/` |
| Marcas | `/brands/` |
| Categorias | `/categories/` |
| Fornecedores | `/suppliers/` |
| Produtos | `/products/` |
| Entradas | `/inflows/` |
| Saídas | `/outflows/` |

Os recursos de marcas, categorias, fornecedores e produtos possuem telas de criação, detalhe, edição e exclusão. Entradas e saídas possuem criação, listagem e detalhe.

## API REST

As APIs usam JWT e permissões do Django REST Framework. Primeiro, obtenha um token:

```http
POST /auth/token/api/v1/
```

Renove ou valide tokens em:

```http
POST /auth/token/refresh/api/v1/
POST /auth/token/verify/api/v1/
```

Endpoints disponíveis:

| Recurso | Listar/criar | Detalhar/alterar/excluir |
| --- | --- | --- |
| Marcas | `/brands/api/v1/` | `/brands/<id>/api/v1/` |
| Categorias | `/categories/api/v1/` | `/categories/<id>/api/v1/` |
| Fornecedores | `/suppliers/api/v1/` | `/suppliers/<id>/api/v1/` |
| Produtos | `/products/api/v1/` | `/products/<id>/api/v1/` |
| Entradas | `/inflows/api/v1/` | `/inflows/<id>/api/v1/` |
| Saídas | `/outflows/api/v1/` | `/outflows/<id>/api/v1/` |

No momento, entradas e saídas expõem detalhe via API, mas não possuem endpoints de atualização/exclusão.

## Importação de dados CSV

O projeto possui arquivos CSV de exemplo nas pastas `data/` de cada app e comandos de importação. Os arquivos usam o delimitador `|`.

Exemplos:

```bash
python manage.py import_brands --filename brands/data/brands.csv
python manage.py import_categories --filename categories/data/categories.csv
python manage.py import_suppliers --filename suppliers/data/suppliers.csv
python manage.py import_products --filename products/data/products.csv
python manage.py import_inflows --filename inflows/data/inflows.csv
python manage.py import_outflows --filename outflows/data/outflows.csv
```

Alguns comandos procuram um usuário com username `admin` para preencher os campos de auditoria. Crie esse usuário antes de importar os dados.

## Notificação de saídas

Ao criar uma saída de estoque, o projeto tenta enviar um evento HTTP para:

```text
http://127.0.0.1:8001/api/v1/webhooks/order/
```

Se esse serviço não estiver disponível, a criação da saída continuará funcionando e a falha será apenas registrada no console.

## Qualidade e desenvolvimento

Dependências de desenvolvimento:

```bash
pip install -r requirements_dev.txt
```

Verificação com Flake8:

```bash
flake8 .
```

No estado atual, não há uma suíte de testes automatizados versionada no projeto.

## Observações

- O projeto ainda está em evolução e acompanha o aprendizado do curso.
- O arquivo `db.sqlite3` é usado para desenvolvimento local.
- Permissões de acesso são aplicadas nas views web com `LoginRequiredMixin` e `PermissionRequiredMixin`.
- As APIs exigem usuário autenticado e respeitam permissões de modelo do Django.
