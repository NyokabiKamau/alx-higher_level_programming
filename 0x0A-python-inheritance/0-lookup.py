#!/usr/bin/python3
"""function that returns the list of available attributes
and methods of an object"""


def lookup(obj):
    """
    returns list of attributes and methods of an object
    """
    return dir(obj)
