#!/usr/bin/env python3
"""Async coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Takes as argument, the max delay and random float is generated
    as the delay, and is waited on asynchronously"""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
