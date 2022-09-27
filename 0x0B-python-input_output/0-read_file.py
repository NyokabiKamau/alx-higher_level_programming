#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """ reads and prints textfile of UTF8 encoding using the with statement"""
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
