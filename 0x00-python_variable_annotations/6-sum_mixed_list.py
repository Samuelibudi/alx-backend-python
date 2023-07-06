#!/usr/bin/env python3

"""
A function that takes a list and returns sum of list.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """
    A function that takes a list parameters and returns
    sum.

    @Params:
        input_list (list): List argument

    Returns:
        float: Returning value

    """
    return sum(mxd_lst)
