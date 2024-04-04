#!/usr/bin/env python3
"""a type-annotated function float typed"""
from typing import List


def sum_mixed_list(mxd_list: List[int, float]) -> float:
    """returns float sum of input list of floats and ints"""

    sum = 0

    for l in mxd_list:
        sum += l

    return sum
