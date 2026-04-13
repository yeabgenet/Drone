from pydantic import BaseModel
from typing import List, Optional, Tuple


class StartTrainingRequest(BaseModel):
    mission_id: str
    session_name: Optional[str] = None


class StartTrainingResponse(BaseModel):
    session_id: str
    message: str


class DroneMoveRequest(BaseModel):
    session_id: str
    x: float
    y: float
    z: float = 0.0


class FinishTrainingRequest(BaseModel):
    session_id: str


class TrainingResponse(BaseModel):
    score: float
    violations: int
    feedback: str


class FinishResponse(BaseModel):
    final_score: float
    violations: int
    path: List[Tuple[float, float]]
