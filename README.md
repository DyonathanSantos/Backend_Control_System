# Sistema de Estoque e Comandas - Backend

Uma API REST moderna construída com FastAPI para gerenciamento de estoque, contas (comandas) e rastreamento de itens.

## 🚀 Características

- ✅ **API RESTful** com FastAPI
- ✅ **Banco de Dados** com SQLAlchemy e SQLite/PostgreSQL
- ✅ **Validação de Dados** com Pydantic
- ✅ **Documentação Automática** com Swagger UI e ReDoc
- ✅ **CORS** configurável
- ✅ **Logging** estruturado
- ✅ **Docker** pronto para produção
- ✅ **Tratamento de Erros** global

## 📋 Pré-requisitos

- Python 3.11+
- pip (gerenciador de pacotes Python)
- PostgreSQL 12+ (recomendado para produção)
- Docker & Docker Compose (opcional)

## ⚡ Instalação Rápida

### 1. Clonar Repositório

```bash
git clone https://github.com/seu-usuario/Backend_Control_System.git
cd Backend_Control_System
```

### 2. Criar e Ativar Ambiente Virtual

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar Ambiente

```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

### 5. Executar a API

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Acesse a documentação interativa em: **http://localhost:8000/docs**

## 🐳 Executar com Docker

```bash
# Build e iniciar
docker-compose up -d

# Ver logs
docker-compose logs -f api

# Parar serviços
docker-compose down
```

## 📚 Endpoints Principais

### Health Check

- `GET /` - Verificação básica da API
- `GET /api/v1/health` - Status detalhado

### Estoque (Stock)

- `GET /api/v1/stock/` - Listar todos os itens
- `POST /api/v1/stock/` - Criar novo item
- `GET /api/v1/stock/{id}` - Obter item específico
- `PUT /api/v1/stock/{id}` - Atualizar item
- `DELETE /api/v1/stock/{id}` - Deletar item

### Contas (Bills)

- `GET /api/v1/bills/` - Listar contas
- `POST /api/v1/bills/` - Criar conta
- `GET /api/v1/bills/{id}` - Obter conta específica
- `PUT /api/v1/bills/{id}` - Atualizar conta
- `DELETE /api/v1/bills/{id}` - Deletar conta

### Itens de Conta (Bill Items)

- `GET /api/v1/billitems/` - Listar itens de contas
- `POST /api/v1/billitems/` - Adicionar item à conta
- `PUT /api/v1/billitems/{id}` - Atualizar item de conta
- `DELETE /api/v1/billitems/{id}` - Remover item de conta

## 📖 Documentação

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **Deployment**: Veja [DEPLOYMENT.md](DEPLOYMENT.md)
- **Estrutura do Projeto**: Veja [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)

## 🏗️ Estrutura do Projeto

```
app/
├── __init__.py
├── main.py              # Aplicação FastAPI
├── config.py            # Configurações
├── database.py          # Conexão com BD
├── crud/                # Operações de BD
├── models/              # Modelos SQLAlchemy
├── routers/             # Rotas da API
└── schemas/             # Esquemas Pydantic
```

## ⚙️ Configuração de Ambiente

Crie um arquivo `.env` baseado em `.env.example`:

```env
ENVIRONMENT=production
DEBUG=False
DATABASE_URL=postgresql://user:password@localhost:5432/estoque_db
ALLOWED_ORIGINS=http://localhost:3000,https://seu-dominio.com
```

## 🚀 Deploy em Produção

### Opções de Hospedagem Suportadas:

- **Heroku**
- **Docker Hub + Docker Compose**
- **AWS (Elastic Beanstalk)**
- **DigitalOcean**
- **Render.com**

Veja [DEPLOYMENT.md](DEPLOYMENT.md) para instruções detalhadas.

## 🛠️ Desenvolvimento

### Instalar Dependências de Desenvolvimento

```bash
pip install -r requirements.txt
```

### Executar em Modo de Desenvolvimento

```bash
uvicorn app.main:app --reload
```

### Executar Testes (quando implementados)

```bash
pytest
```

## 📝 Variáveis de Ambiente

| Variável          | Padrão              | Descrição                         |
| ----------------- | ------------------- | --------------------------------- |
| `ENVIRONMENT`     | development         | Ambiente (development/production) |
| `DEBUG`           | False               | Ativar modo debug                 |
| `DATABASE_URL`    | sqlite:///./test.db | URL do banco de dados             |
| `ALLOWED_ORIGINS` | localhost:\*        | Origens CORS permitidas           |

## 🤝 Contribuindo

1. Fork o repositório
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 📞 Suporte

Para dúvidas ou problemas:

- Abra uma [Issue](https://github.com/seu-usuario/Backend_Control_System/issues)
- Consulte a [Documentação FastAPI](https://fastapi.tiangolo.com/)

## 🙏 Agradecimentos

- [FastAPI](https://fastapi.tiangolo.com/) - Framework web moderno
- [SQLAlchemy](https://www.sqlalchemy.org/) - ORM Python
- [Pydantic](https://docs.pydantic.dev/) - Validação de dados

---

**Versão**: 2.0.0  
**Status**: Production Ready ✅
