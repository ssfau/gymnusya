from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import Session
from backend.db import Base

class DailyNutritionLog(Base):
    __tablename__ = "nutrition_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)  # UUID same as UserSettings
    date = Column(Date, index=True)

    calories = Column(Float, default=0)
    protein = Column(Float, default=0)
    carbs = Column(Float, default=0)
    fats = Column(Float, default=0)

class MealEntry(Base):
    __tablename__ = "meal_entries"

    id = Column(Integer, primary_key=True)
    user_id = Column(String, index=True)
    date = Column(Date, index=True)

    name = Column(String)
    calories = Column(Float)
    protein = Column(Float)
    carbs = Column(Float)
    fats = Column(Float)

"""
def request_daily_nutrition(db: Session, data: schemas.DailyNutritionBase):
    nutritiontoday = DailyNutritionLog(**data.dict())
    db.query()
"""

def create_meal_entry(db: Session, data: schemas.MealEntryCreate):
    # meal entry update
    meal = MealEntry(**data.dict())
    db.add(meal)
    db.commit()
    db.refresh(meal)


    # updating daily nutrition log
    existing = (
        db.query(DailyNutritionLog)
        .filter_by(user_id=data.user_id, date=data.date)
        .first()
    )

    if existing:
        existing.calories += data.calories
        existing.protein += data.protein
        existing.carbs += data.carbs
        existing.fats += data.fats   # FIXED

        db.commit()
        db.refresh(existing)
    else:
        todays = DailyNutritionLog(
            user_id=data.user_id,
            date=data.date,
            calories=data.calories,
            protein=data.protein,
            carbs=data.carbs,
            fats=data.fats,    # FIXED
        )
        db.add(todays)
        db.commit()
        db.refresh(todays)
    
    return meal

