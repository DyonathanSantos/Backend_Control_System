import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    """Application configuration settings"""
    
    # Database configuration
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "sqlite:///./test.db"  # Default to SQLite for development
    )
    
    # Application settings
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    
    # API configuration
    API_TITLE: str = "Sistema de Estoque e Comandas"
    API_VERSION: str = "2.0.0"
    API_DESCRIPTION: str = "API para gerenciamento de estoque e comandas com rastreamento de itens"
    
    # CORS configuration
    ALLOWED_ORIGINS: list = os.getenv(
        "ALLOWED_ORIGINS",
        "http://localhost,http://localhost:3000,http://localhost:8000"
    ).split(",")
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()