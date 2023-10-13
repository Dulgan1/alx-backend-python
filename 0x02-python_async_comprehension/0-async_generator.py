#!/usr/bin/env python3
"""Async generator of random int"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[int, None, None]:
    """Generates a random number between 0 to 10"""
    for _ in range(10):
        asyncio.sleep(1)
        yield random.randint(0, 10)
