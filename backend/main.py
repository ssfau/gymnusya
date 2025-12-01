from fastapi import FastAPI 
from routers.nutrition import router as nutrition_router
from routers.workout import router as workout_router

app = FastAPI()

app.include_router(nutrition_router, prefix="/nutrition")
app.include_router(workout_router, prefix="/workout")

# Local development run
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)

@app.get("/")
def root():
    return {"Hello":"Main"}