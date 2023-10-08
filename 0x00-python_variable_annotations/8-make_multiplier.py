#!/usr/bin/env python3
"""Type annotated module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def f(n: float) -> float:
        mul = multiplier * n
        return float(mul)
    return f
