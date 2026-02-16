import logging
import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.routers.stock_routes import router as stock_router
from app.routers.bill_router import router as bill_router
from app.routers.billitem_router import router as billitem_router
from app.database import engine, DBBase
from app.models import all_models
from app.config import settings

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Create tables once, after all models are imported
logger.info("Initializing database tables...")
DBBase.metadata.create_all(bind=engine)
logger.info("Database tables initialized successfully")

# Get allowed origins from environment variable
ALLOWED_ORIGINS = os.getenv(
    "ALLOWED_ORIGINS", 
    "http://localhost,http://localhost:3000,http://localhost:8000"
).split(",")

# Event handlers for startup and shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage app startup and shutdown events"""
    logger.info("Application starting up...")
    yield
    logger.info("Application shutting down...")

app = FastAPI(
    title="Sistema de Estoque e Comandas",
    description="API para gerenciamento de estoque e comandas com rastreamento de itens",
    version="2.0.0",
    lifespan=lifespan
)

# Add CORS middleware for cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add exception handler for general errors
@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected error occurred. Please try again later."}
    )

# Register routers
logger.info("Registering routers...")
app.include_router(stock_router, prefix="/api/v1")
app.include_router(bill_router, prefix="/api/v1")
# Mount bill-item routes under the bills path so endpoints look like:
# /api/v1/bills/{bill_id}/items
app.include_router(billitem_router, prefix="/api/v1/bills")
logger.info("Routers registered successfully")


@app.get("/", tags=["Health"])
def root():
    """Health check endpoint to verify API is running"""
    logger.info("Health check endpoint accessed")
    return {
        "message": "API funcionando corretamente!",
        "version": "2.0.0",
        "status": "online"
    }


@app.get("/api/v1/health", tags=["Health"])
def health_check():
    """Detailed health check endpoint"""
    return {
        "status": "healthy",
        "version": "2.0.0",
        "service": "Sistema de Estoque e Comandas"
    }


if __name__ == "__main__":
    import uvicorn
    # Run with: python -m app.main
    # Or: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    uvicorn.run(app, host="0.0.0.0", port=8000)