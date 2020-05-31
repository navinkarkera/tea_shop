import os
from typing import List, Optional

import databases
import sqlalchemy
from fastapi import APIRouter, FastAPI, File, Form, HTTPException, UploadFile, status
from fastapi.staticfiles import StaticFiles
from sqlalchemy import desc, select

from .model import items, metadata
from .schema import ItemDetail, ItemIn, ItemOut

app = FastAPI()
api_router = APIRouter()
app.mount("/static", StaticFiles(directory="data"), name="static")

if os.getenv("TEA_TESTING"):
    DATABASE_URL = "sqlite:///./data-test.db"
else:
    DATABASE_URL = "sqlite:///./data.db"

database = databases.Database(DATABASE_URL)
engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

metadata.create_all(engine)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@api_router.get("/items/", response_model=List[ItemOut])
async def read_item():
    query = select([items.c.id, items.c.name, items.c.price, items.c.image]).order_by(
        desc(items.c.id)
    )
    return await database.fetch_all(query)


@api_router.get("/items/{id}", response_model=ItemDetail)
async def read_item(id: int):
    query = items.select().where(items.c.id == id)
    resp = await database.fetch_one(query)
    if resp:
        return resp
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with id: {id} not found"
    )


@api_router.post("/items/", response_model=ItemDetail, status_code=status.HTTP_201_CREATED)
async def create_item(
    name: str = Form(...),
    price: float = Form(...),
    description: str = Form(...),
    file: Optional[UploadFile] = File(default=None),
):
    item = ItemIn(name=name, price=price, description=description)
    if file:
        image_path = f"data/{file.filename}"
        image_url = f"static/{file.filename}"
        item.image = image_url
        contents = await file.read()
        with open(image_path, "wb") as f:
            f.write(contents)
    query = items.insert().values(**item.dict())
    last_record_id = await database.execute(query)
    return {**item.dict(), "id": last_record_id}


@api_router.delete("/items/", status_code=204)
async def delete_item(id: int):
    query = items.delete().where(items.c.id == id)
    await database.execute(query)


app.include_router(api_router, prefix="/api/v1", tags=["item"])
app.mount("/", StaticFiles(directory="frontend/dist", html=True), name="main")
