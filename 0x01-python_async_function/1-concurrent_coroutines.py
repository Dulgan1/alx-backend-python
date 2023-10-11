#!/usr/bin/env python3
"""Async coroutine"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns list of results of an async coroutine spawn n times"""
    wait_list: list
    coroutines: list = [wait_random(max_delay) for i in range(n)]
    returns: list[float] = await asyncio.gather(*coroutines)
    wait_list = sorted(returns)
    return wait_list
