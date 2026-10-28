#!/usr/bin/env python3
"""Run task_wait_random coroutines concurrently."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Run tasks and return delays in completion order."""
    tasks = [
        task_wait_random(max_delay)
        for _ in range(n)
    ]
    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
