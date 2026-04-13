import math
from typing import List, Tuple


class ScoringEngine:
    def __init__(self, expected_path: List[Tuple[float, float]], tolerance: float = 0.7):
        self.expected_path = expected_path
        self.tolerance = tolerance
        self.path: List[Tuple[float, float]] = []
        self.violations = 0

    def add_position(self, x: float, y: float) -> float:
        self.path.append((x, y))
        index = min(len(self.path) - 1, len(self.expected_path) - 1)
        ex, ey = self.expected_path[index]
        error = math.sqrt((x - ex) ** 2 + (y - ey) ** 2)

        if error > self.tolerance:
            self.violations += 1

        return error

    def calculate_score(self) -> float:
        total_error = 0.0
        for i, (x, y) in enumerate(self.path):
            if i >= len(self.expected_path):
                break
            ex, ey = self.expected_path[i]
            total_error += math.sqrt((x - ex) ** 2 + (y - ey) ** 2)

        score = max(0.0, 100.0 - total_error * 10.0 - self.violations * 5.0)
        return score
