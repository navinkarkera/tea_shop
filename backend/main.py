from typing import List

import databases
import sqlalchemy
from fastapi import FastAPI, Form, File, UploadFile

from .schema import ItemIn, ItemOut
from .model import metadata, items

DATABASE_URL = "sqlite:///./data.db"
app = FastAPI()
database = databases.Database(DATABASE_URL)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/item/", response_model=List[ItemOut])
async def read_item():
    query = items.select()
    return await database.fetch_all(query)


@app.post("/item/", response_model=ItemOut)
async def create_item(name: str = Form(...), price: float = Form(...), file: UploadFile = File(...)):
    image_path = f"data/{file.filename}"
    item = ItemIn(name=name, price=price, image=image_path)
    contents = await file.read()
    with open(image_path, "wb") as f:
        f.write(contents)
    query = items.insert().values(**item.dict())
    last_record_id = await database.execute(query)
    return {**item.dict(), "id": last_record_id}


@app.delete("/item/", status_code=204)
async def delete_item(id: int):
    query = items.delete().where(items.c.id==id)
    await database.execute(query)
