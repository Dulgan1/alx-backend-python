#!/usr/bin/env python3
"""Typed module sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns sum of floats un input list"""
    s: float = 0.0
    for flt in input_list:
        s += flt
    return float(s)
