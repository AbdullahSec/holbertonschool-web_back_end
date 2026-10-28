#!/usr/bin/env python3
"""Create and return a task for wait_random."""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Schedule wait_random and return its task."""
    return asyncio.create_task(wait_random(max_delay))
 