#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    numerator = 0
    denominator = 0
    for _tuple in my_list:
        numerator += _tuple[0] * _tuple[1]
        denominator += _tuple[1]
    return numerator / denominator
