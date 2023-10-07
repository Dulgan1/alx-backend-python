#!/usr/bin/env python3
"""Typed module sum_mixed_list"""
from typing import Union, List

def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Returns sum of floats and ints in list"""
    return float(sum(mxd_list))
