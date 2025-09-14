from pydantic import BaseModel

class AskRequest(BaseModel):
    prompt: str

class AskResponse(BaseModel):
    answer: str