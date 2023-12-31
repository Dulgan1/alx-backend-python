#!/usr/bin/env python3
"""Type annotated module"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of Tuple from passed iterable"""
    return [(i, len(i)) for i in lst]
