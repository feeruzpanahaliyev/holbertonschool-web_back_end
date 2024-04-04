#!/usr/bin/env python3
"""a type-annotated function float typed"""
from typing import List, Union


def sum_list(input_list: List[Union[int, float]]) -> float:
    """returns float sum of input list of floats"""

    sum: float = 0

    for l in input_list:
        sum += l

    return sum
