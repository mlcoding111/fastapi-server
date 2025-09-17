from fastapi import APIRouter, Depends, HTTPException, status, Form

router = APIRouter()

mock_users = [
    {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com"
    },
    {
        "id": 2,
        "name": "Jane Doe",
        "email": "jane.doe@example.com"
    }
]

@router.get("/users/")
def get_users():
    x: str = 3

    print(x)
    return mock_users