#!/usr/bin/python3
"""function that creates python object from json file"""
import json


def load_from_json_file(filename):
    """
    Args:
        filename: name of the json file
    Returns: the object
    """
    with open(filename) as file:
        return json.loads(file.read())
