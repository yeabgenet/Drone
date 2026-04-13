from fastapi import APIRouter, HTTPException
from app.models.training_models import (
    DroneMoveRequest,
    FinishResponse,
    FinishTrainingRequest,
    StartTrainingRequest,
    StartTrainingResponse,
    TrainingResponse,
)
from app.services.training_service import TrainingService

router = APIRouter()
service = TrainingService()


@router.post("/start", response_model=StartTrainingResponse)
def start_training(request: StartTrainingRequest):
    try:
        session_id = service.start(request.mission_id)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc))

    return {
        "session_id": session_id,
        "message": "training started",
    }


@router.post("/move", response_model=TrainingResponse)
def move_drone(request: DroneMoveRequest):
    try:
        score, violations, feedback = service.move(request.session_id, request.x, request.y)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc))

    return {
        "score": score,
        "violations": violations,
        "feedback": feedback,
    }


@router.post("/finish", response_model=FinishResponse)
def finish_training(request: FinishTrainingRequest):
    try:
        score, violations, path = service.finish(request.session_id)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail=str(exc))

    return {
        "final_score": score,
        "violations": violations,
        "path": path,
    }
