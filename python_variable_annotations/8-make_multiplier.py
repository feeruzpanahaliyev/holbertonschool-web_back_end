#!/usr/bin/env python3
"""imports the Callable type hint from the typing module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a func that multiplies a float by the specified multi"""

    def multiply(num: float) -> float:
        return num * multiplier

    return multiply
