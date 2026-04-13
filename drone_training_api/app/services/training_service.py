import uuid
from typing import Dict, List, Tuple
from app.core.scoring import ScoringEngine
from app.data.missions import MISSIONS


class TrainingSession:
    def __init__(self, session_id: str, mission_id: str, expected_path: List[Tuple[float, float]]):
        self.session_id = session_id
        self.mission_id = mission_id
        self.engine = ScoringEngine(expected_path)

    def move(self, x: float, y: float) -> Tuple[float, int, str]:
        error = self.engine.add_position(x, y)
        score = self.engine.calculate_score()
        if error > 1.0:
            feedback = "Too far from path"
        elif error > 0.5:
            feedback = "Slight drift"
        else:
            feedback = "Good"
        return score, self.engine.violations, feedback

    def finish(self) -> Tuple[float, int, List[Tuple[float, float]]]:
        score = self.engine.calculate_score()
        return score, self.engine.violations, self.engine.path


class TrainingService:
    def __init__(self):
        self.sessions: Dict[str, TrainingSession] = {}

    def start(self, mission_id: str) -> str:
        if mission_id not in MISSIONS:
            raise ValueError("Mission not found")

        session_id = str(uuid.uuid4())
        session = TrainingSession(session_id, mission_id, MISSIONS[mission_id])
        self.sessions[session_id] = session
        return session_id

    def _get_session(self, session_id: str) -> TrainingSession:
        session = self.sessions.get(session_id)
        if session is None:
            raise KeyError(f"Session '{session_id}' not found")
        return session

    def move(self, session_id: str, x: float, y: float) -> Tuple[float, int, str]:
        session = self._get_session(session_id)
        return session.move(x, y)

    def finish(self, session_id: str) -> Tuple[float, int, List[Tuple[float, float]]]:
        session = self._get_session(session_id)
        result = session.finish()
        return result
