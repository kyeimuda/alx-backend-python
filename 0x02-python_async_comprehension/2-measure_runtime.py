#!/usr/bin/env python3
"""
measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Execute async_comprehension four times in parallel using
    asyncio.gather and measures the total time to rum and return it.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for n in range(4)))
    end = time.time()
    return end - start
