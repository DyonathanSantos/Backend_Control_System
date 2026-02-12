from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

import app.models
from app.database import get_db
from app.models import Stock
from app.schemas.stock_schema import StockCreate, StockUpdate, StockOut
from app.schemas.bill_schema import BillOut

router = APIRouter()


@router.post("", response_model=list[BillOut])
def create_stock (db: Annotated[Session, Depends(get_db)], stock_data: StockCreate):

# Verification if exist the product in table
    try:
        result = db.execute(select(Stock).where(Stock.product_name == stock_data.product_name))

        existing = result.scalars().first()
        if existing:
            raise HTTPException(status_code=400, detail="Produto já existe no estoque!")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Erro ao verificar o produto no estoque: {e}")
            
# Unpacking the pydantic(stock_data) validation and returned in dict with values of schema key for commit and add
    stock = Stock(**stock_data.model_dump())
    db.add(stock)
    db.commit()
    db.refresh(stock)
    return stock


# Function for see all product (info) in Stock table.
def get_all_stock(db: Annotated[Session, Depends(get_db)]):
    return db.query(Stock).all()


# Function for see product (info) by id.
def get_stock_one(db: Annotated[Session, Depends(get_db)], stock_id: int):
    return db.query(Stock).filter_by(id=stock_id).firts()

# function for Update parcial
def update_stock_parcial (db: Annotated[Session, Depends(get_db)], stock_data:StockUpdate, stock_id: int):
    
    # Checking if the ID exist 
    existing = db.get(Stock).filter_by(stock_id).first()
    if not existing:
        raise HTTPException(status_code= 404, detail="Produto não existe!")
    
    # Conversion to dict and verification of incorret values
    update_data = stock_data.model_dump(exclude_unset=True)

    if update_data["quantity"] < 0:
        raise Exception ("Número incorreto na quantidade, precisa ser maior que zero")
    if update_data["product_price"] < 0:
        raise Exception ("Valor incorreto no preço!")
    if update_data["product_buy"] < 0:
        raise Exception ("Valor incorreto no preço de compra")
    
    #  A Loop to update new information in the datebase and, if an error occurs, perform a rollback
    try:

        for field, value in update_data:
            setattr (Stock, field, value)

            db.add()
            db.commit()
            db.refresh(Stock)
            return Stock
    except Exception as e:
        db.rollback()
        return f"Ocorreu um erro na tentativa de atualizar o item de ID {stock_id}, erro {e}"

    


def delete_stock(stock_id: int, db: Annotated[Session, Depends(get_db)]):
    stock = db.query(Stock).filter_by(Stock.id == stock_id).first()

    if not stock:
        return status.HTTP_404_NOT_FOUND

    db.delete(stock)
    db.commit()
    return status.HTTP_204_NO_CONTENT