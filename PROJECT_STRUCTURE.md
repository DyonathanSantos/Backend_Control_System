# Project Structure - Backend_Control_System

## Directory Layout

```
Backend_Control_System/
│
├── 📄 Documentation
│   ├── README.md
│   ├── QUICKSTART.md
│   ├── DEPLOYMENT.md
│   └── PROJECT_STRUCTURE.md
│
├── 🐳 Docker & Production
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── 🔧 Configuration
│   ├── requirements.txt
│   ├── .env
│   └── .env.example
│
├── 📜 Other
│   ├── LICENSE
│   └── pre-push-check.sh
│
└── 💻 Application
    └── app/
        ├── __init__.py
        ├── main.py                 # FastAPI application & routes setup
        ├── config.py               # Configuration management
        ├── database.py             # Database connection & session
        │
        ├── models/                 # SQLAlchemy ORM Models
        │   ├── __init__.py
        │   ├── all_models.py       # Import all models
        │   ├── user.py             # User model
        │   ├── bill.py             # Bill/Comanda model
        │   ├── billitem.py         # Bill item model
        │   ├── stock.py            # Stock/Product model
        │   ├── itemsales.py        # Item sales model
        │   └── sales.py            # Sales model
        │
        ├── schemas/                # Pydantic request/response models
        │   ├── __init__.py
        │   ├── stock_schema.py     # Stock validation schemas
        │   ├── bill_schema.py      # Bill validation schemas
        │   └── billitem_schema.py  # BillItem validation schemas
        │
        ├── crud/                   # CRUD operations (business logic)
        │   ├── __init__.py
        │   ├── stock_crud.py       # Stock CRUD functions
        │   ├── bill_crud.py        # Bill CRUD functions
        │   └── billitem_crud.py    # BillItem CRUD functions
        │
        └── routers/                # API endpoints (routes)
            ├── __init__.py
            ├── stock_routes.py     # Stock endpoints
            ├── bill_router.py      # Bill endpoints
            └── billitem_router.py  # BillItem endpoints
```

---

## Module Descriptions

### 🔵 Core Application

#### `main.py`

- FastAPI application initialization
- Router registration with API versioning (`/api/v1/`)
- Logging configuration
- CORS middleware setup
- Global exception handlers
- Health check endpoints

#### `config.py`

- Environment variable management
- Application settings
- Database configuration
- CORS origins configuration

#### `database.py`

- SQLAlchemy engine setup
- Database session management
- ORM base class definition

---

### 🔴 Models (`models/`)

Data layer - SQLAlchemy ORM models

#### `bill.py`

- Bill/Comanda entity
- Fields: id, table_number, customer_name, created_at, status
- Relationships: items (BillItem), sales (Sales)

#### `billitem.py`

- Bill item entity (join table between Bill and Stock)
- Fields: id, bill_id, stock_id, quantity, unit_price, created_at
- Relationships: bill, stock

#### `stock.py`

- Product/Stock entity
- Fields: id, name, quantity, price, created_at, created_by
- Relationships: bill_items (BillItem), sales (Sales)

#### `user.py`

- User entity
- Fields: id, username, email, password (hashed)

#### `sales.py` & `itemsales.py`

- Sales tracking entities
- Track sales history and item sales

#### `all_models.py`

- Central import file for all models
- Ensures all models are registered with SQLAlchemy

---

### 🟢 Schemas (`schemas/`)

Validation layer - Pydantic models for request/response validation

#### `stock_schema.py`

- `StockBase` - Base fields for stock
- `StockCreate` - Input validation for creation
- `StockUpdate` - Input validation for updates
- `StockResponse` - Output response model

#### `bill_schema.py`

- `BillBase` - Base fields for bill
- `BillCreate` - Input validation for creation
- `BillUpdate` - Input validation for updates
- `BillResponse` - Output response model with nested items

#### `billitem_schema.py`

- `BillItemBase` - Base fields for bill item
- `BillItemCreate` - Input validation for creation
- `BillItemResponse` - Output with nested stock info
- `StockInfo` - Nested stock information in response

---

### 🟡 CRUD (`crud/`)

Business logic layer - Database operations

#### `stock_crud.py`

- `create_stock()` - Create new stock item
- `get_all_stock()` - List all stock items with pagination
- `get_stock_by_id()` - Get single stock item
- `update_stock_partial()` - Update specific fields
- `delete_stock()` - Delete stock item

#### `bill_crud.py`

- `create_bill()` - Create new bill/comanda
- `get_all_bills()` - List all bills
- `get_bill_by_id()` - Get single bill with items
- `update_bill()` - Update bill details
- `delete_bill()` - Delete bill

#### `billitem_crud.py`

- `create_bill_item()` - Add item to bill with inventory validation
- Validates: bill exists, stock exists, sufficient quantity
- Decreases stock quantity automatically

---

### 🟣 Routers (`routers/`)

API endpoint layer - HTTP request handling

#### `stock_routes.py`

```
POST   /api/v1/stock/           - Create stock item
GET    /api/v1/stock/           - List all stock items
GET    /api/v1/stock/{id}       - Get specific stock
PUT    /api/v1/stock/{id}       - Update stock
DELETE /api/v1/stock/{id}       - Delete stock
```

#### `bill_router.py`

```
POST   /api/v1/bills/           - Create bill
GET    /api/v1/bills/           - List all bills
GET    /api/v1/bills/{id}       - Get specific bill
PUT    /api/v1/bills/{id}       - Update bill
DELETE /api/v1/bills/{id}       - Delete bill
```

#### `billitem_router.py`

```
POST   /api/v1/billitems/       - Add item to bill
GET    /api/v1/billitems/       - List all bill items
PUT    /api/v1/billitems/{id}   - Update bill item
DELETE /api/v1/billitems/{id}   - Delete bill item
```

---

## Data Flow Architecture

```
HTTP Request
    ↓
Router (@app.get, @app.post, etc)
    ↓
Schema Validation (Pydantic)
    ↓
CRUD Function (Business Logic)
    ↓
SQLAlchemy Model (ORM)
    ↓
Database
    ↓
SQLAlchemy Model (Query Result)
    ↓
Schema Serialization (Pydantic)
    ↓
HTTP Response
```

---

## Database Relationships

### Bill ↔ BillItem

- One Bill has many BillItems
- BillItem belongs to one Bill

### Stock ↔ BillItem

- One Stock has many BillItems
- BillItem references one Stock (inventory tracking)

### Bill ↔ Sales

- One Bill has many Sales
- Sales belong to one Bill

### Stock ↔ Sales

- One Stock has many Sales
- Sales reference one Stock

---

## API Endpoints Summary

| Method | Endpoint                 | Purpose           |
| ------ | ------------------------ | ----------------- |
| POST   | `/api/v1/stock/`         | Create stock item |
| GET    | `/api/v1/stock/`         | List stock items  |
| GET    | `/api/v1/stock/{id}`     | Get stock details |
| PUT    | `/api/v1/stock/{id}`     | Update stock      |
| DELETE | `/api/v1/stock/{id}`     | Delete stock      |
| POST   | `/api/v1/bills/`         | Create bill       |
| GET    | `/api/v1/bills/`         | List bills        |
| GET    | `/api/v1/bills/{id}`     | Get bill details  |
| PUT    | `/api/v1/bills/{id}`     | Update bill       |
| DELETE | `/api/v1/bills/{id}`     | Delete bill       |
| POST   | `/api/v1/billitems/`     | Add item to bill  |
| GET    | `/api/v1/billitems/`     | List bill items   |
| PUT    | `/api/v1/billitems/{id}` | Update bill item  |
| DELETE | `/api/v1/billitems/{id}` | Delete bill item  |

---

## Documentation Endpoints

- **Swagger UI** - `GET /docs`
- **ReDoc** - `GET /redoc`
- **Health Check** - `GET /`
- **Detailed Health** - `GET /api/v1/health`

---

## Architecture Principles

✅ **Separation of Concerns**

- Models handle data structure
- Schemas handle validation
- CRUD handles business logic
- Routers handle HTTP layer

✅ **Clean Code**

- Type hints on all functions
- Descriptive variable names
- Clear error handling
- Well-organized imports

✅ **Best Practices**

- DRY (Don't Repeat Yourself)
- SOLID principles
- RESTful API design
- Proper HTTP status codes

✅ **Production Ready**

- Input validation at all layers
- Error handling and logging
- Database transaction safety
- CORS security
- Environment-based configuration
