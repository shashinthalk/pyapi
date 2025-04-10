from fastapi import APIRouter
from app.models.item_model import Item
from app.models.insta_model import InstaLoginRequest
from app.services.insta_rpa import get_instagram_profile

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

@router.post("/instagram/")
def instagram_rpa(login_data: InstaLoginRequest):
    data = get_instagram_profile(login_data.username, login_data.password, login_data.target)
    return data
