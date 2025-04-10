from fastapi import APIRouter
from app.models.insta_model import InstaLoginRequest
from app.services.insta_rpa import get_instagram_profile

router = APIRouter()

@router.post("/instagram/")
def instagram_rpa(login_data: InstaLoginRequest):
    data = get_instagram_profile(login_data.username, login_data.password)
    return data
