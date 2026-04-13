from fastapi import FastAPI
from app.api.training import router as training_router

app = FastAPI(title="Drone Training API")

app.include_router(
    training_router,
    prefix="/training",
    tags=["Training"]
)
