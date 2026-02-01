from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config import settings

engine = create_engine(settings.DATABASE_URL, echo= True)
DBBase = declarative_base()
Sessao_ = sessionmaker(autocommit= False, autoflush= False, bind=engine)

#Depends
def get_db():
    db = Sessao_()
    try:
        yield db
    finally:
        db.close()
