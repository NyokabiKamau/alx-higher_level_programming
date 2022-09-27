#!/usr/bin/python3
"""returns JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """Writes text in filename.
    Args:
        - filename: name of the file
        - text: string to write in the file
    Returns: number of characters written
    """
    return json.dumps(my_obj)
