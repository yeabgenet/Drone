from typing import Dict, List, Tuple

MISSIONS: Dict[str, List[Tuple[float, float]]] = {
    "straight_line": [
        (0.0, 0.0),
        (1.0, 0.0),
        (2.0, 0.0),
        (3.0, 0.0),
        (4.0, 0.0),
        (5.0, 0.0),
    ],
    "square": [
        (0.0, 0.0),
        (3.0, 0.0),
        (3.0, 3.0),
        (0.0, 3.0),
        (0.0, 0.0),
    ],
    "zigzag": [
        (0.0, 0.0),
        (1.0, 1.0),
        (2.0, 0.0),
        (3.0, 1.0),
        (4.0, 0.0),
    ],
}
