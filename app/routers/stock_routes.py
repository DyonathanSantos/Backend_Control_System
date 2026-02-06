from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud.stock_crud import (create_stock, get_all_stock, get_stock_one, update_stock_parcial, delete_stock)
from app.models.stock import Stock
from app.schemas.stock_schema import StockBase,StockCreate, StockUpdate ,StockOut

router = APIRouter( prefix="/stock",tags=["Stock"])

@router.post("/", response_model=StockOut, status_code=status.HTTP_201_CREATED)
def route_create_stock(data: StockCreate, db: Session = Depends(get_db)):
    return create_stock(db, data)

@router.get("/", response_model=list[StockOut])
def route_list_stock(db: Session = Depends(get_db)):
    return get_all_stock(db)

@router.get("/{stock_id}", response_model=StockOut)
def route_get_stock(stock_id: int, db: Session = Depends(get_db)):
    stock = get_stock_one(stock_id, db)
    if not stock:
        raise HTTPException(status_code=404, detail="Item não encontrado.")
    return stock

@router.put("/{stock_id}", response_model=StockOut)
def route_update_stock(stock_id: int, data: StockUpdate, db: Session = Depends(get_db)):
    return update_stock_parcial(db, stock_id, data)

@router.delete("/{stock_id}")
def route_delete_stock(stock_id: int, db: Session = Depends(get_db)):
    return delete_stock(stock_id, db)