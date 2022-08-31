#!/usr/bin/python3
def uniq_add(my_list=[]):
    _result = 0
    for uniq_num in set(my_list):
        _result += uniq_num
    return _result
