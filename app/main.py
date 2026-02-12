from fastapi import FastAPI
from app.routers.stock_routes import router as stock_router
from app.routers.bill_router import router as bill_router
from app.routers.billitem_router import router as billitem_router

# Ensure all models are imported and registered in metadata
from app.database import engine, DBBase
from app.models import all_models

# Create tables once, after all models are imported
DBBase.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema de Estoque e Comandas",
    description="API for managing stock and bills with item tracking",
    version="2.0.0"
)

# Register routers
app.include_router(stock_router)
app.include_router(bill_router)
app.include_router(billitem_router)


@app.get("/")
def root():
    """Health check endpoint"""
    return {"message": "API funcionando!", "version": "2.0.0"}


# Run with: uvicorn app.main:app --reload