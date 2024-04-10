#!/usr/bin/env python3
"""a type-annotated function float typed"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of str and float"""

    return (k, v ** 2)
