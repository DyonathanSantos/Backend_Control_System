from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.stock import Stock
from app.schemas.stock_schema import StockCreate, StockUpdate, StockOut


def create_stock (db: Session, stock_data: StockCreate):

# Verification if exist the product in table
    try:
        existing = db.query(Stock).filter(Stock.product == stock_data.product).first()
    except HTTPException as e:   
            if existing:
                db.rollback()
                raise HTTPException(status_code=400, detail="Produto já existe")
            
# Unpacking the pydantic(stock_data) validation and returned in dict with values of schema key for commit and add
    stock = Stock(**stock_data.model_dump())
    db.add(stock)
    db.commit()
    db.refresh(stock)
    return stock


# Function for see all product (info) in Stock table.
def get_all_stock(db:Session):
    return db.query(Stock).all()


# Function for see product (info) by id.
def get_stock_one(db:Session, stock_id: int):
    return db.query(Stock).filter_by(id=stock_id).firts()

# function for Update parcial
def update_stock_parcial (db: Session, stock_data:StockUpdate, stock_id: int):
    
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
    except Exception as e:
        db.rollback()
        return f"Ocorreu um erro na tentativa de atualizar o item de ID {stock_id}, erro {e}"

    


def delete_stock(stock_id: int, db: Session):
    stock = db.query(Stock).filter(Stock.id == stock_id).first()

    if not stock:
        return False

    db.delete(stock)
    db.commit()
    return True