#!/usr/bin/env python3
"""Type annotated module"""
from typing import TypeVar, Mapping, Any, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """Returns value of key in map-type object if exists"""
    if key in dct:
        return dct[key]
    else:
        return default
