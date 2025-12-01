from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import HTTPException

router = APIRouter()

@router.get("/")
def root():
    return {"Hello":"Workout"}