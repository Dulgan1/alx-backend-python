#!/usr/bin/env python3
"""Type annotated module"""
from typing import TypeVar, Mapping, Any


def safely_get_value(dct: Mapping[Any], key: Any,
                     default: Union[Any, None]) -> Any:
    """Returns value of key in map-type object if exists"""
    if key in dct:
        return dct[key]
    else:
        return default
