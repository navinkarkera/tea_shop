from typing import Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    price: float
    image: Optional[str]


class ItemIn(ItemBase):
    description: str


class ItemOut(ItemBase):
    id: int


class ItemDetail(ItemIn, ItemOut):
    pass
