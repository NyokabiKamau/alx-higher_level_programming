#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    conv_rom = 0
    for i, c in enumerate(roman_string):
        if (i + 1) == len(roman_string) or num[c] >= num[roman_string[i + 1]]:
            conv_rom += num[c]
        else:
            conv_rom -= num[c]
    return conv_rom
