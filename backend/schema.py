from pydantic import BaseModel


class ItemIn(BaseModel):
    name: str
    price: float
    image: str


class ItemOut(ItemIn):
    id: int
