#!/usr/bin/env python3
"""Async module, generates list of floats"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Using asynchronous comprehension"""
    return [rf async for rf in async_generator()]
