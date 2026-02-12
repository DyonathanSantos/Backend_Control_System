# Quick Reference - BillItem API

## Quick Start

### 1. Create a Stock Item

```bash
curl -X POST http://localhost:8000/stocks \
  -H "Content-Type: application/json" \
  -d '{
    "product": "Laptop",
    "category": "Electronics",
    "quantity": 10,
    "product_price": 999.99,
    "product_buy": 500.00
  }'
```

### 2. Create a Bill

```bash
curl -X POST http://localhost:8000/bills \
  -H "Content-Type: application/json" \
  -d '{
    "customer_name": "John Doe"
  }'
```

### 3. Add Item to Bill

```bash
curl -X POST http://localhost:8000/bills/1/items \
  -H "Content-Type: application/json" \
  -d '{
    "stock_id": 1,
    "quantity": 2,
    "unit_price": 999.99
  }'
```

---

## API Endpoints

### Stocks

| Method | Endpoint       | Purpose         |
| ------ | -------------- | --------------- |
| POST   | `/stocks`      | Create stock    |
| GET    | `/stocks`      | List all stocks |
| GET    | `/stocks/{id}` | Get stock by ID |
| PATCH  | `/stocks/{id}` | Update stock    |
| DELETE | `/stocks/{id}` | Delete stock    |

### Bills

| Method | Endpoint      | Purpose        |
| ------ | ------------- | -------------- |
| POST   | `/bills`      | Create bill    |
| GET    | `/bills`      | List all bills |
| GET    | `/bills/{id}` | Get bill by ID |
| PUT    | `/bills/{id}` | Update bill    |
| DELETE | `/bills/{id}` | Delete bill    |

### BillItems

| Method | Endpoint                 | Purpose          |
| ------ | ------------------------ | ---------------- |
| POST   | `/bills/{bill_id}/items` | Add item to bill |

---

## Response Examples

### Stock Response

```json
{
  "id": 1,
  "product": "Laptop",
  "category": "Electronics",
  "quantity": 8,
  "product_price": 999.99,
  "product_buy": 500.0
}
```

### Bill Response

```json
{
  "id": 1,
  "customer_name": "John Doe",
  "status": "Aberto",
  "created_at": "2026-02-11T10:30:00+00:00"
}
```

### BillItem Response

```json
{
  "id": 1,
  "bill_id": 1,
  "stock_id": 1,
  "quantity": 2,
  "unit_price": 999.99,
  "created_at": "2026-02-11T10:31:00+00:00",
  "stock": {
    "id": 1,
    "product": "Laptop",
    "product_price": 999.99
  }
}
```

---

## Status Codes

| Code | Meaning                        |
| ---- | ------------------------------ |
| 201  | Created successfully           |
| 200  | OK / Success                   |
| 204  | No Content (successful delete) |
| 400  | Bad Request (validation error) |
| 404  | Not Found                      |

---

## Common Errors

### Bill Not Found

```json
{ "detail": "Bill not found" }
```

### Stock Not Found

```json
{ "detail": "Stock item not found" }
```

### Insufficient Stock

```json
{ "detail": "Insufficient stock quantity. Available: 5, Requested: 10" }
```

### Duplicate Product

```json
{ "detail": "Product already exists in stock" }
```

---

## Python Example

```python
from sqlalchemy.orm import Session
from app.crud.billitem_crud import create_bill_item
from app.database import Sessao_

db = Sessao_()

# Create BillItem
bill_item = create_bill_item(
    db=db,
    bill_id=1,
    stock_id=5,
    quantity=2,
    unit_price=999.99
)

print(f"BillItem created: {bill_item.id}")
print(f"Stock updated: {bill_item.stock.quantity} remaining")
```

---

## Database Query Examples

```python
from sqlalchemy import select
from app.models.billitem import BillItem
from app.models.stock import Stock

# Get all items for a bill
items = db.query(BillItem).filter(BillItem.bill_id == 1).all()

# Get all bills for a stock
bills = db.query(BillItem).filter(BillItem.stock_id == 5).all()

# Get total quantity sold
total = db.query(BillItem).filter(BillItem.stock_id == 5).all()
quantity_sold = sum(item.quantity for item in total)

# Get stock by product name
stock = db.query(Stock).filter(Stock.product == "Laptop").first()
```

---

## File Overview

### Models

- `app/models/billitem.py` - BillItem model definition
- `app/models/bill.py` - Bill model (updated)
- `app/models/stock.py` - Stock model (updated)

### Schemas

- `app/schemas/billitem_schema.py` - BillItem validation schemas
- `app/schemas/bill_schema.py` - Bill validation schemas
- `app/schemas/stock_schema.py` - Stock validation schemas

### CRUD

- `app/crud/billitem_crud.py` - BillItem operations
- `app/crud/bill_crud.py` - Bill operations
- `app/crud/stock_crud.py` - Stock operations

### Routes

- `app/routers/billitem_router.py` - BillItem endpoints
- `app/routers/bill_router.py` - Bill endpoints
- `app/routers/stock_routes.py` - Stock endpoints

---

## Key Features

✅ **Automatic Stock Management**

- Stock quantity automatically decreased when item added to bill

✅ **Validation**

- Bill existence check
- Stock existence check
- Stock quantity validation

✅ **Nested Responses**

- BillItem response includes product info

✅ **Error Handling**

- Clear error messages
- Proper HTTP status codes

✅ **Transaction Safety**

- Atomic operations
- Proper rollback on errors

---

## Documentation

- `REFACTORING_SUMMARY.md` - Complete refactoring overview
- `BILLITEM_INTEGRATION_GUIDE.md` - Integration guide with examples
- `PROJECT_STRUCTURE.md` - Directory structure and organization
- `COMPLETION_CHECKLIST.md` - Requirements checklist

---

**Version:** 2.0.0  
**Status:** Production Ready ✅
