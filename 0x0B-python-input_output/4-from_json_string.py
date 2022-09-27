#!/usr/bin/python3
"""returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """Return the object rep my my_str
    Args
        - my_str: json string to convert
    Returns: represented string
    """
    return json.loads(my_str)
