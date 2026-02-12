# BillItem Integration Guide

## Overview

This guide explains how the new BillItem model integrates with the existing Bill and Stock models.

## Database Schema

### Before Refactoring

```
Bill ──────(1:N)────── Stock
  id                      id
  customer_name           product
  status                  category
  created_at              quantity
                          product_price
                          product_buy
                          bill_id (FK)
                          created_by (FK)
```

### After Refactoring

```
Bill ──────(1:N)────── BillItem ──────(N:1)────── Stock
  id                     id                         id
  customer_name          bill_id (FK)               product
  status                 stock_id (FK)              category
  created_at             quantity                   quantity
                         unit_price                 product_price
                         created_at                 product_buy
                                                    created_at
                                                    created_by
```

## Key Features

### 1. Stock Quantity Management

When you add an item to a bill, the stock quantity is automatically decreased:

```python
# Example: Add 2 laptops to bill #1
POST /bills/1/items
{
    "stock_id": 5,
    "quantity": 2,
    "unit_price": 999.99
}

# Stock #5 quantity automatically reduced by 2
# BillItem created with the transaction data
```

### 2. Validation

The `create_bill_item()` function validates:

- ✅ Bill exists
- ✅ Stock item exists
- ✅ Stock has sufficient quantity
- ✅ All fields are properly provided

### 3. Transaction Safety

All operations are atomic:

- If bill doesn't exist → BillItem not created, stock not modified
- If stock insufficient → entire operation rolled back
- If commit fails → database consistency maintained

## API Endpoints

### Stock Management

```
POST   /stocks                    Create new stock
GET    /stocks                    List all stocks
GET    /stocks/{stock_id}         Get specific stock
PATCH  /stocks/{stock_id}         Update stock
DELETE /stocks/{stock_id}         Delete stock
```

### Bill Management

```
POST   /bills                     Create new bill
GET    /bills                     List all bills
GET    /bills/{bill_id}           Get specific bill
PUT    /bills/{bill_id}           Update bill
DELETE /bills/{bill_id}           Delete bill
```

### BillItem Management (NEW)

```
POST   /bills/{bill_id}/items     Add item to bill
```

## Request/Response Examples

### 1. Create Stock

**Request:**

```bash
POST /stocks
Content-Type: application/json

{
    "product": "Laptop Dell XPS 13",
    "category": "Computers",
    "quantity": 10,
    "product_price": 999.99,
    "product_buy": 750.00
}
```

**Response (201 Created):**

```json
{
  "id": 5,
  "product": "Laptop Dell XPS 13",
  "category": "Computers",
  "quantity": 10,
  "product_price": 999.99,
  "product_buy": 750.0
}
```

### 2. Create Bill

**Request:**

```bash
POST /bills
Content-Type: application/json

{
    "customer_name": "João Silva"
}
```

**Response (201 Created):**

```json
{
  "id": 1,
  "customer_name": "João Silva",
  "status": "Aberto",
  "created_at": "2026-02-11T10:30:00+00:00"
}
```

### 3. Add Item to Bill

**Request:**

```bash
POST /bills/1/items
Content-Type: application/json

{
    "stock_id": 5,
    "quantity": 2,
    "unit_price": 999.99
}
```

**Response (201 Created):**

```json
{
  "id": 1,
  "bill_id": 1,
  "stock_id": 5,
  "quantity": 2,
  "unit_price": 999.99,
  "created_at": "2026-02-11T10:31:00+00:00",
  "stock": {
    "id": 5,
    "product": "Laptop Dell XPS 13",
    "product_price": 999.99
  }
}
```

### 4. Get Bill with Items

**Request:**

```bash
GET /bills/1
```

**Note:** To get all items in a bill, you would need to query BillItem separately or implement a custom endpoint that includes items in the Bill response.

### 5. Update Stock Quantity

**Request:**

```bash
PATCH /stocks/5
Content-Type: application/json

{
    "quantity": 15
}
```

**Response:**

```json
{
  "id": 5,
  "product": "Laptop Dell XPS 13",
  "category": "Computers",
  "quantity": 15,
  "product_price": 999.99,
  "product_buy": 750.0
}
```

## Error Handling

### Bill Not Found

```json
{
  "detail": "Bill not found"
}
```

Status: 404 Not Found

### Stock Not Found

```json
{
  "detail": "Stock item not found"
}
```

Status: 404 Not Found

### Insufficient Stock

```json
{
  "detail": "Insufficient stock quantity. Available: 5, Requested: 10"
}
```

Status: 400 Bad Request

### Duplicate Product

```json
{
  "detail": "Product already exists in stock"
}
```

Status: 400 Bad Request

### Duplicate Customer

```json
{
  "detail": "Customer already registered"
}
```

Status: 400 Bad Request

## Database Migration

To update your existing database:

1. **Backup your database** (important!)

2. **Create an Alembic migration** (if using Alembic):

```bash
alembic revision --autogenerate -m "Add BillItem model"
alembic upgrade head
```

3. **Or manually apply changes**:

```sql
-- Remove bill_id from stock table
ALTER TABLE stock DROP COLUMN bill_id;

-- Create new bill_item table
CREATE TABLE bill_item (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    bill_id BIGINT NOT NULL,
    stock_id BIGINT NOT NULL,
    quantity INT NOT NULL,
    unit_price FLOAT NOT NULL,
    created_at DATETIME(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    FOREIGN KEY (bill_id) REFERENCES bill(id),
    FOREIGN KEY (stock_id) REFERENCES stock(id)
);
```

## Architecture Pattern

This refactoring follows **Clean Architecture** principles:

```
Request
   ↓
Router (FastAPI)
   ↓
CRUD Function
   ↓
Model (SQLAlchemy)
   ↓
Database
   ↓
Response
```

Each layer has a single responsibility:

- **Router**: Handle HTTP requests/responses
- **CRUD**: Business logic and data operations
- **Model**: Database schema definition
- **Schema**: Data validation and serialization

## Type Safety

All functions include complete type hints:

```python
def create_bill_item(
    db: Session,
    bill_id: int,
    stock_id: int,
    quantity: int,
    unit_price: float
) -> BillItem:
    """Create BillItem with validation"""
    pass
```

This provides:

- IDE autocompletion
- Type checking with mypy
- Better documentation
- Runtime safety

## Testing Example

```python
# Create a stock
stock = create_stock(db, StockCreate(
    product="Mouse Wireless",
    category="Accessories",
    quantity=50,
    product_price=45.99,
    product_buy=20.00
))

# Create a bill
bill = create_bill(db, BillCreate(
    customer_name="Maria Santos"
))

# Add item to bill
bill_item = create_bill_item(
    db=db,
    bill_id=bill.id,
    stock_id=stock.id,
    quantity=3,
    unit_price=45.99
)

# Stock quantity is now 47
assert stock.quantity == 47
```

## Performance Considerations

1. **Indexing**: Foreign keys (bill_id, stock_id) are automatically indexed
2. **Query Optimization**: Use SQLAlchemy's relationship loading strategies if needed
3. **Pagination**: Consider adding pagination for list endpoints
4. **Caching**: Stock price data could be cached for fast lookups

## Future Enhancements

1. **Additional BillItem endpoints**:
   - GET /bills/{bill_id}/items - List all items in a bill
   - DELETE /bills/{bill_id}/items/{item_id} - Remove item from bill

2. **Bill status tracking**:
   - Paid, Pending, Cancelled status
   - Status transitions with validation

3. **Reports**:
   - Total bill amount calculation
   - Stock movement history
   - Sales analytics

4. **Inventory alerts**:
   - Low stock notifications
   - Reorder reminders

---

**Status:** Production Ready ✅
