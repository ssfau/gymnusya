from fastapi import APIRouter, Depends
from pydantic import BaseModel
from fastapi import HTTPException
from backend.core.nutrition_logic import create_meal_entry
import backend.schemas as schemas
from backend.db import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/")
def root():
    return {"Hello":"Nutrition"}

@router.post("/log_meal")
def post_meal_entry(meal_data: schemas.MealCreate, db: Session = Depends(get_db)):
    return create_meal_entry(db, meal_data)

@router.get("/get_todays_nutrition")
def get_todays_nutrition():
    return ""
