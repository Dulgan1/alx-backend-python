#!/usr/bin/env python3
"""Tyoe annotated module"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return any or None from passed sequence"""
    if lst:
        return lst[0]
    else:
        return None
