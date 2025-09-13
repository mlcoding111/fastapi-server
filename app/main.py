from typing import Optional

from fastapi import FastAPI
from .routers.users import router as users_router
from .config import settings

# FastAPI instance
app = FastAPI()

# Debugging
print(f"DATABASE_URL: {settings.DATABASE_URL}")
print(f"SECRET_KEY: {settings.SECRET_KEY}")
print(f"ALGORITHM: {settings.ALGORITHM}")
print(f"ACCESS_TOKEN_EXPIRES_IN: {settings.ACCESS_TOKEN_EXPIRES_IN}")

# Routes
app.include_router(users_router, prefix="", tags=["users"])

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

# @app.get("/items/")
# def read_items(skip: int = 0, limit: int = 10):
#     return {"skip": skip, "limit": limit}