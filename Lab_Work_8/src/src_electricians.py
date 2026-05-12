"""Модуль для обчислення максимальної довжини електрокабелю."""
import math
from typing import List

def calculate_max_wire_length(width: int, heights: List[int]) -> float:
    """Обчислює максимальну довжину дроту"""
    if not heights or len(heights) < 2:
        return 0.0

    prev_at_1 = 0.0
    prev_at_h = 0.0

    for i in range(1, len(heights)):
        h_prev = heights[i - 1]
        h_curr = heights[i]

        # Варіант, якщо поточна опора висотою 1
        curr_at_1 = max(
            prev_at_1 + width, prev_at_h + math.sqrt(width**2 + (h_prev - 1) ** 2)
        )

        # Варіант, якщо поточна опора максимальної висоти
        curr_at_h = max(
            prev_at_1 + math.sqrt(width**2 + (h_curr - 1) ** 2),
            prev_at_h + math.sqrt(width**2 + (h_prev - h_curr) ** 2),
        )

        prev_at_1, prev_at_h = curr_at_1, curr_at_h

    return float(f"{max(prev_at_1, prev_at_h):.2f}")