from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.stock import Stock
from app.schemas.stock_schema import StockCreate


def create_stock(db: Session, stock_data: StockCreate):
    existing = db.query(Stock).filter(Stock.product == stock_data.product).first()
    if existing:
        raise HTTPException(status_code=400, detail="Produto já existe.")
    stock = Stock(**stock_data.model_dump())
    db.add(stock)
    db.commit()
    db.refresh(stock)
    return stock

def get_stock_all(db: Session):
    return db.query(Stock).all()

def get_stock_by_id(stock_id: int, db: Session ):
    return db.query(Stock).filter_by(id=stock_id).first()

def update_stock(db: Session, stock_id: int, stock_data: StockUpdate):
    """Atualiza um estoque existente.

    Comportamento:
    - Busca o objeto no banco com `Session.get`.
    - Se não existir, lança HTTPException(404).
    - Aplica apenas os campos informados (suporta updates parciais via Pydantic `exclude_unset=True`).
    - Faz commit/refresh com tratamento de exceção e rollback em caso de erro.
    """
    # Buscando pelo id — Session.get é mais direto e eficiente
    stock = db.get(Stock, stock_id)

    if not stock:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    # Suporta updates parciais: somente os campos informados no payload serão atualizados
    update_data = stock_data.model_dump(exclude_unset=True)

    # Validações simples antes de aplicar
    if 'quantity' in update_data and update_data['quantity'] < 0:
        raise HTTPException(status_code=400, detail='Quantidade não pode ser negativa')
    if 'buy' in update_data and update_data['buy'] <= 0:
        raise HTTPException(status_code=400, detail='Preço de compra não pode ser negativo')
    if 'sell' in update_data and update_data['sell'] <= 0:
        raise HTTPException(status_code=400, detail='Preço de venda não pode ser negativo')

    # Aplicar atualizações dinamicamente
    for key, value in update_data.items():
        if hasattr(stock, key):
            setattr(stock, key, value)

    try:
        db.commit()
        db.refresh(stock)
        return stock
    except Exception as e:
        db.rollback()
        # Se for um erro de integridade (ex: unique constraint), retorna 400
        raise HTTPException(status_code=400, detail=str(e))

def delete_stock(stock_id: int, db: Session):
    stock = db.query(Stock).filter(Stock.id == stock_id).first()

    if not stock:
        return False

    db.delete(stock)
    db.commit()
    return True