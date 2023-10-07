#!/usr/bin/env python3
"""Typed annotated module"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns tuple of passed string k with square of v in float"""
    return k, float(v**2)
