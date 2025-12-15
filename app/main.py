from fastapi import FastAPI
from app.routers.stock_routes import router as stock_router

# garantir que todos os modelos sejam importados e registrados no metadata
from app.database import engine, Base
import app.models.stock
import app.models.comanda
import app.models.item_comanda
import app.models.sell
import app.models.user
import app.models.logs

# criar tabelas uma única vez, depois que todos os modelos estiverem importados
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Estoque e Comandas")

# Registrar rotas
app.include_router(stock_router)

@app.get("/")
def root():
    return {"message": "API funcionando!"}

# Iniciar o servidor com: uvicorn app.main:app --reload