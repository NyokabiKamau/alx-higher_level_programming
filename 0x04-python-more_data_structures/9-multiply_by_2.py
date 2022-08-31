#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    _result = {}
    for i in a_dictionary:
        _result[i] = a_dictionary[i] * 2
    return _result
