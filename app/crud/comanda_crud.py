from sqlalchemy.orm import Session
from app.models.comanda import Comanda
from app.schemas.comanda_schema import ComandaCreate


def create_comanda(db: Session, comanda_data: ComandaCreate):
    comanda = Comanda(**comanda_data.model_dump())
    db.add(comanda)
    db.commit()
    db.refresh(comanda)
    return comanda

def get_comanda_all(db: Session):
    return db.query(Comanda).all()

def get_comanda_by_id(db: Session, comanda_id: int):
    return db.query(Comanda).filter(Comanda.id == comanda_id).first()

def update_comanda(db: Session, comanda_id: int, comanda_data: ComandaCreate):
    comanda = db.query(Comanda).filter(Comanda.id == comanda_id).first()

    if not comanda:
        return None 
    
    comanda.Customer = comanda_data.Customer
    comanda.status = comanda_data.status

    db.commit()
    db.refresh(comanda)
    return comanda

def delete_comanda(db: Session, comanda_id: int):
    comanda = db.query(Comanda).filter(Comanda.id == comanda_id).first()

    if not comanda:
        return False

    db.delete(comanda)
    db.commit()
    return True 