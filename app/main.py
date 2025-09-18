from typing import Optional

from fastapi import FastAPI
from .routers.users import router as users_router
from .config import get_settings
from .routers.ai import router as ai_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi_sessions.middleware import SessionMiddleware
from .routers.auth import router as auth_router

# FastAPI instance
app = FastAPI(title="FastAPI Server", description="A FastAPI server for the FastAPI Server project")
app.add_middleware(SessionMiddleware, secret_key=get_settings().JWT_SECRET_KEY)
# Debugging
print(f"DATABASE_URL: {get_settings().DATABASE_URL}")
print(f"SECRET_KEY: {get_settings().SECRET_KEY}")
print(f"ALGORITHM: {get_settings().ALGORITHM}")
print(f"ACCESS_TOKEN_EXPIRES_IN: {get_settings().ACCESS_TOKEN_EXPIRES_IN}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
app.include_router(users_router, prefix="", tags=["users"])
app.include_router(ai_router, prefix="", tags=["ai"])
app.include_router(auth_router, prefix="", tags=["auth"])

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

# @app.get("/items/")
# def read_items(skip: int = 0, limit: int = 10):
#     return {"skip": skip, "limit": limit}