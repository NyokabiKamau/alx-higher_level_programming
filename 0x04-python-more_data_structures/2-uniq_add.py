#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_num = set(my_list)
    _result = 0

    for num in uniq_num:
         _result += num
    return _result
