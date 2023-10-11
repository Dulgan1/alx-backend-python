#!/usr/bin/env python3
"""Async module"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates and return an asyncio task of async coroutine:
    wait_random accepting max_delat as arg"""
    return asyncio.create_task(wait_random(max_delay))
