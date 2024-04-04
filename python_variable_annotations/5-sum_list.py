#!/usr/bin/env python3
"""a type-annotated function float typed"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """returns float sum of input list of floats and ints"""

    sum: float = 0

    for l in mxd_list:
        sum += l

    return sum
