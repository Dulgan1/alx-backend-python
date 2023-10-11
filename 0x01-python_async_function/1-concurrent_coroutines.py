#!/usr/bin/env python3
"""Async coroutine"""
import asyncio
from typing import List, Coroutine

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    wait_list: list
    coroutines: List[Coroutine] = [wait_random(max_delays) for i in range(n)]
    returns: list[float] = await asyncio.gather(*coroutines)
    wait_list = sorted(returns)
    return wait_list
