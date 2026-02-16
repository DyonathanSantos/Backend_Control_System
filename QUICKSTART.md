# 🚀 Quick Start - Sistema de Estoque e Comandas

## Começar em 5 Minutos

### Opção 1: Desenvolvimento Local (Recomendado)

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/Backend_Control_System.git
cd Backend_Control_System

# 2. Crie ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Instale dependências
pip install -r requirements.txt

# 4. Rode a API
uvicorn app.main:app --reload

# 5. Acesse
# Swagger UI: http://localhost:8000/docs
# ReDoc: http://localhost:8000/redoc
```

### Opção 2: Com Docker

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/Backend_Control_System.git
cd Backend_Control_System

# 2. Inicie com Docker Compose
docker-compose up -d

# 3. Acesse
# API: http://localhost:8000
# Swagger: http://localhost:8000/docs
```

## 📝 Testando a API

### Health Check

```bash
curl http://localhost:8000/
```

### Criar Item de Estoque

```bash
curl -X POST http://localhost:8000/api/v1/stock/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Produto XYZ", "quantity": 100, "price": 25.50}'
```

### Listar Itens

```bash
curl http://localhost:8000/api/v1/stock/
```

## 🔧 Configurar Variáveis de Ambiente

Edite o arquivo `.env`:

```bash
# Banco de dados PostgreSQL (recomendado)
DATABASE_URL=postgresql://user:password@localhost:5432/estoque_db

# Ou SQLite (desenvolvimento)
DATABASE_URL=sqlite:///./estoque.db

# CORS - domínios permitidos
ALLOWED_ORIGINS=http://localhost:3000,https://seu-frontend.com
```

## 📚 Documentação Completa

- **Instalação Detalhada**: [README.md](README.md)
- **Deploy em Produção**: [DEPLOYMENT.md](DEPLOYMENT.md)
- **Estrutura do Projeto**: [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)

## ⚡ Comandos Úteis

```bash
# Rodar em modo desenvolvimento com auto-reload
uvicorn app.main:app --reload

# Rodar na porta 8080
uvicorn app.main:app --port 8080

# Rodar em todos os IPs (0.0.0.0)
uvicorn app.main:app --host 0.0.0.0

# Com workers
uvicorn app.main:app --workers 4

# Docker - rebuild
docker-compose build

# Docker - logs
docker-compose logs -f api

# Docker - shell
docker-compose exec api /bin/bash
```

## 🐛 Troubleshooting

| Erro                  | Solução                                               |
| --------------------- | ----------------------------------------------------- |
| `ModuleNotFoundError` | Rode `pip install -r requirements.txt`                |
| Porta 8000 em uso     | Use `--port 8080` ou `docker-compose up -p 8080:8000` |
| Erro de conexão BD    | Verifique `DATABASE_URL` no `.env`                    |
| CORS error            | Atualize `ALLOWED_ORIGINS` no `.env`                  |

## 🎯 Próximos Passos

1. ✅ API rodando
2. 📚 Explorar documentação em `/docs`
3. 🔌 Integrar com frontend
4. 🐳 Deploy com Docker
5. 🌍 Hospedar em nuvem

---

**Dúvidas?** Consulte a [documentação completa](README.md) ou abra uma [issue](https://github.com/seu-usuario/Backend_Control_System/issues)
