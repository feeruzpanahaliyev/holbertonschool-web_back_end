#!/usr/bin/env python3
'''async await'''
import asyncio, random


async def wait_random(max_delay: int = 10) -> float:
    """Returns max_delay"""

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
