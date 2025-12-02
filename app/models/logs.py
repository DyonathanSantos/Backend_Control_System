from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class Log(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    action = Column(String(100), nullable=False)
    timestamp = Column(String(50), server_default=func.now())