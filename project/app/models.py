from typing import Optional

from pydantic import BaseModel
from sqlalchemy import Integer, Column, String
from app.db import Base


class Items(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Integer, default=0)


class Item(BaseModel):
    id: int
    name: str
    price: int


class AddItem(BaseModel):
    name: str
    price: int
