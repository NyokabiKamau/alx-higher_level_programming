#!/usr/bin/python3
"""function that returns True if the object
is an instance of a class that inherited
(directly or indirectly) from the specified class;
otherwise False.
"""


def inherits_from(obj, a_class):
    """instance of a class inherited directly/indirectly"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
