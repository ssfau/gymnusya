from pydantic import BaseModel
from datetime import date
# FOR EVERY SCHEMA TO UPDATE: BASE, CREATE AND RESPONSE

# nutrition related
class DailyNutritionBase(BaseModel):
    calories: float
    protein: float
    carbs: float
    fats: float

class DailyNutritionCreate(DailyNutritionBase):
    user_id: str    # uuid from frontend
    date: date      # frontend usually sends today

class DailyNutritionResponse(DailyNutritionBase):
    id: int
    user_id: str
    date: date

    class Config:
        from_attributes = True

class MealEntryBase(BaseModel):
    meal_name: str
    food_name: str
    calories: float
    protein: float
    carbs: float
    fats: float

class MealEntryCreate(MealEntryBase):
    user_id: str
    date: date

class MealEntryResponse(MealEntryBase):
    id: int
    user_id: str
    date: date

    class Config:
        from_attributes = True


# settings related
class UserSettingsBase(BaseModel):
    height: float
    weight: float
    age: int
    sex: int
    goal: str
    activity: str
    experience: str

class UserSettingsCreate(UserSettingsBase):
    user_id: str     # front-end UUID

class UserSettingsResponse(UserSettingsBase):
    id: int
    user_id: str

    class Config:
        orm_mode = True
