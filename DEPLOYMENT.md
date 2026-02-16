# Guia de Hospedagem - Sistema de Estoque e Comandas

## Pré-requisitos

- Python 3.11+
- PostgreSQL 12+ (para produção)
- Docker & Docker Compose (opcional)
- Git

## Instalação Local

### 1. Clonar Repositório

```bash
git clone https://github.com/seu-usuario/Backend_Control_System.git
cd Backend_Control_System
```

### 2. Criar Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar Variáveis de Ambiente

```bash
cp .env.example .env
# Editar .env com suas configurações
```

### 5. Executar Aplicação

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Acesse: http://localhost:8000

## Hospedagem com Docker

### 1. Build da Imagem

```bash
docker-compose build
```

### 2. Iniciar Serviços

```bash
docker-compose up -d
```

### 3. Verificar Logs

```bash
docker-compose logs -f api
```

### 4. Parar Serviços

```bash
docker-compose down
```

## Hospedagem em Servidores Cloud

### Heroku

1. Instale Heroku CLI
2. Execute:

```bash
heroku login
heroku create seu-app-name
git push heroku main
heroku config:set DATABASE_URL=seu_postgresql_url
```

### AWS/DigitalOcean/Render

1. Configure a imagem Docker
2. Defina variáveis de ambiente
3. Mapeie a porta 8000
4. Use PostgreSQL RDS/Managed Database

### Configurações Importantes de Produção

- `DEBUG=False`
- `ENVIRONMENT=production`
- Usar PostgreSQL em vez de SQLite
- Configurar ALLOWED_ORIGINS corretamente
- Usar HTTPS
- Configurar logs persistentes

## Endpoints Disponíveis

### Health Check

- `GET /` - Verificação básica
- `GET /api/v1/health` - Verificação detalhada

### Documentação

- `GET /docs` - Swagger UI
- `GET /redoc` - ReDoc

### Stock

- `GET /api/v1/stock/` - Listar itens
- `POST /api/v1/stock/` - Criar item
- `PUT /api/v1/stock/{id}` - Atualizar item
- `DELETE /api/v1/stock/{id}` - Deletar item

### Bills

- `GET /api/v1/bills/` - Listar contas
- `POST /api/v1/bills/` - Criar conta

### Bill Items

- `GET /api/v1/billitems/` - Listar itens de conta
- `POST /api/v1/billitems/` - Criar item de conta

## Troubleshooting

### Problema: Connection refused

**Solução**: Verifique se PostgreSQL está rodando e se DATABASE_URL está correto

### Problema: CORS Error

**Solução**: Atualize ALLOWED_ORIGINS no .env com o domínio correto

### Problema: Módulos não encontrados

**Solução**: Execute `pip install -r requirements.txt` novamente

## Suporte e Documentação

- FastAPI: https://fastapi.tiangolo.com/
- SQLAlchemy: https://docs.sqlalchemy.org/
- Pydantic: https://docs.pydantic.dev/
