#!/usr/bin/env python3
"""Async coroutine"""
import asyncio
from typing import List

task_wait_random = __import__('3-task').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Task Based alt of wait_n from 1-concurrent_coroutines.py:
        Returns list of results of an async coroutine spawn n times
    """
    wait_list: List[float]
    coroutine_tasks: list = [task_wait_random(max_delay)
                             for _ in range(n)]
    wait_list = [await task for task in  asyncio.\
            as_completed(coroutine_tasks)]
    return wait_list
