from pydantic import BaseModel

class InstaLoginRequest(BaseModel):
    username: str
    password: str
    target: str
