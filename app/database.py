from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config import settings

engine = create_engine(settings.DATABASE_URL, echo= True)
Base = declarative_base()
Sessao_ = sessionmaker(engine, autocommit= False, autoflush= False)
Base.engine = engine
Base.Session = Sessao_

def get_db():
    db = Sessao_()
    try:
        yield db
    finally:
        db.close()
