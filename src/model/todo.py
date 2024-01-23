from sqlalchemy import Column, Integer, Boolean, DateTime, func, String
from database import Base


class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
