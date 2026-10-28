#!/usr/bin/env python3
"""Measure the average runtime of wait_n."""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average runtime per wait_n coroutine."""
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    average_time = end_time - start_time
    total_time = average_time / n
    return total_time
    