#!/usr/bin/env python3
"""
coroutine called async_comprehension that takes no
"""
import random
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collects random 10 numbets from async_generator and return the random
    10 numbers
    """
    numbers = [i async for i in async_generator()]
    return numbers
