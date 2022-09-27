#!/usr/bin/python3
"""function that writes an object to a text file,
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes the representation of my_obj to filename
    Args
        my_obj: object to write
        filename: file to write into
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
