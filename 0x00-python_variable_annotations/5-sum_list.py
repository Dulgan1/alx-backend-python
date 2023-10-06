#!/usr/bin/env python3
"""Typed module sum_list"""


def sum_list(input_list: list[float]) -> float:
    """Returns sum of floats un input list"""
    s: float = 0.0
    for flt in input_list:
        s += flt
    return float(s)
