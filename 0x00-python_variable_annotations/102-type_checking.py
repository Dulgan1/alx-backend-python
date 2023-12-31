#!/usr/bin/env python3
"""Type annotated, to test with mypy"""
from typing import List, Union


def zoom_array(lst: List, factor: Union[int, float] = 2) -> List:
    """Returns zoomed list of passed list by factor of factor passed
    argument"""
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
