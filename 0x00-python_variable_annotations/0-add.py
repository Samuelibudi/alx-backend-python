#!/usr/bin/env python3

"""
A function that takes two floats and returns sum as a float.
"""

def add(a : float, b : float) -> float:
    """
    A function that takes two float parameters and returns
    sum as a float

    @Params:
        a (float) : First float argument.
        b (float) : Second float argument.

    Returns:
        float: Returning value

    """
    if a or b is instanceof(float):
        return a + b
    else:
        print("Arguments have to be float")
        return
