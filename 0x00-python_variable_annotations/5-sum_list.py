#!/usr/bin/env python3
"""Typed module sum_list"""


def sum_list(input_list: list[float]) -> float:
    sum = 0
    for flt in input_list:
        sum += flt
    return float(sum)
