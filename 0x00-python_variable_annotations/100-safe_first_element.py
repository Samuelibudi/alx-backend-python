#!/usr/bin/env python3
"""Duck typing annotation"""
from typing import Union, Any, Sequence, List, Tuple, Iterable


def safe_first_element(lst: Sequence[Any]) -> Union[None, Any]:
    """Returns first element of a list if it exists,
       otherwise returns none.
    """
    if lst:
        return lst[0]
    else:
        return None
