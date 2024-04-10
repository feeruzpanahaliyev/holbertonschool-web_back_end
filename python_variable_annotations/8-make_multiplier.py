#!/usr/bin/env python3
"""This import statement imports the Callable type hint from the typing module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by the specified multiplier."""

    def multiply(num: float) -> float:
        return num * multiplier

    return multiply