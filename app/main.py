from fastapi import FastAPI
from app.routes import items

app = FastAPI()

# Include routes
app.include_router(items.router)