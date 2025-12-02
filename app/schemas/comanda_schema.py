from pydantic import BaseModel

class ComandaBase(BaseModel):
    Customer: str
    status: str
    create_at: str


class ComandaCreate(ComandaBase):
    pass

class ComandaOut(ComandaBase):
    id: int

    class Config:
        orm_mode = True