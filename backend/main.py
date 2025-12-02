from fastapi import FastAPI 
from backend.db import Base, engine
from backend.routers.nutrition import router as nutrition_router
from backend.routers.workout import router as workout_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(nutrition_router, prefix="/nutrition")
app.include_router(workout_router, prefix="/workout")

# Local development run
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)

@app.get("/")
def root():
    return {"Hello":"Main"}