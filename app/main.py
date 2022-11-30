from typing import Union
from app.settings import Settings

from app.data import PredictionInput, PredictionOutput
from app.model import NewsgroupModel

from fastapi import FastAPI, Depends
from pydantic import BaseModel

import logging

setting = Settings()

app = FastAPI()

newgroups_model = NewsgroupModel()
logging.info('model class is created')


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.post("/predict")
async def prediction(
    output: PredictionOutput = Depends(newgroups_model.predict),
) -> PredictionOutput:
    return output

@app.on_event("startup")
async def startup():
    logging.info("model is loaded")

    newgroups_model.load_model()