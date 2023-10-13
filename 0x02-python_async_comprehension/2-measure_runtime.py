#!/usr/bin/env python3
"""Async Module: measures time to run multiple async tasks"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Returns time measured after running 4 tasks of async_comprehesion"""
    start: float = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end: float = time.time() - start
    return end
