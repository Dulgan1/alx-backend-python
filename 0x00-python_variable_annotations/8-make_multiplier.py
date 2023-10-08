#!/usr/bin/env python3
"""Type annotated module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that accepts only float argument"""
    def f(n: float) -> float:
        return float(multiplier * n)
    return f
