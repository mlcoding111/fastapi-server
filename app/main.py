from fastapi import FastAPI, Depends
from .config import get_settings
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated

from .routers.ai import router as ai_router
from .routers.auth import router as auth_router
from .routers.users import router as users_router

# FastAPI instance
app = FastAPI(title="FastAPI Server", description="A FastAPI server for the FastAPI Server project")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}

# Routes
app.include_router(users_router, prefix="", tags=["users"])
app.include_router(ai_router, prefix="", tags=["ai"])
# app.include_router(auth_router, prefix="", tags=["auth"])