from fastapi import APIRouter
from app.models.item_model import Item

router = APIRouter()

@router.get("/")
def root():
    return {"message": "API is running"}

@router.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

@router.post("/items/")
def create_item(item: Item):
    return {"received": item}
