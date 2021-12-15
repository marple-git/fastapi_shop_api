import asyncio

from fastapi import Depends, FastAPI
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from typing import List

from app.models import Items, Item

from app.models import AddItem


app = FastAPI()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get("/items", response_model=List[Item])
async def get_items(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Items))
    items = result.scalars().all()
    return [Item(id=item.id, name=item.name, price=item.price) for item in items]


@app.post("/items")
async def add_item(item: AddItem, session: AsyncSession = Depends(get_session)):
    item = Items(name=item.name, price=item.price)
    session.add(item)
    await session.commit()
    await session.refresh(item)
    return item
