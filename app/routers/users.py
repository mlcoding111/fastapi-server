from fastapi import APIRouter, Depends, HTTPException, status, Form

router = APIRouter()

@router.get("/users/")
def get_users():
    return {"message": "Hello World"}