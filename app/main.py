from fastapi import FastAPI
from app.routers.stock_routes import router as stock_router

# garantir que todos os modelos sejam importados e registrados no metadata
from app.database import engine, DBBase
from app.models import all_models
# criar tabelas uma única vez, depois que todos os modelos estiverem importados
DBBase.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Estoque e Comandas")

# Registrar rotas
app.include_router(stock_router)

@app.get("/")
def root():
    return {"message": "API funcionando!"}

# Iniciar o servidor com: uvicorn app.main:app --reload