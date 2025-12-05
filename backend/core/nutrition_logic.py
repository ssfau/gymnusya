from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import Session, Mapped, mapped_column
from backend.db import Base
from backend import schemas as schemas


class DailyNutritionLog(Base):
    __tablename__ = "nutrition_logs"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(index=True)
    date: Mapped[Date] = mapped_column(index=True)

    calories: Mapped[float] = mapped_column(default=0)
    protein: Mapped[float] = mapped_column(default=0)
    carbs: Mapped[float] = mapped_column(default=0)
    fats: Mapped[float] = mapped_column(default=0)


    

class MealEntry(Base):
    __tablename__ = "meal_entries"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(index=True)
    date: Mapped[Date] = mapped_column(index=True)

    name: Mapped[str] = mapped_column(default="")
    calories: Mapped[float] = mapped_column(default=0)
    protein: Mapped[float] = mapped_column(default=0)
    carbs: Mapped[float] = mapped_column(default=0)
    fats: Mapped[float] = mapped_column(default=0)

"""
def request_daily_nutrition(db: Session, data: schemas.DailyNutritionBase):
    nutritiontoday = DailyNutritionLog(**data.dict())
    db.query()
"""

def create_meal_entry(db: Session, data: schemas.MealCreate):
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
        existing.fat += data.fat   # FIXED

        db.commit()
        db.refresh(existing)
    else:
        todays = DailyNutritionLog(
            user_id=data.user_id,
            date=data.date,
            calories=data.calories,
            protein=data.protein,
            carbs=data.carbs,
            fat=data.fat,    # FIXED
        )
        db.add(todays)
        db.commit()
        db.refresh(todays)
    
    return meal

